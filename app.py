import time
import streamlit as st

import database
from auth import load_messages, login, save_message, signup
from pipeline.hybrid_search import ask
from pipeline.query_router import select_query
from pipeline.graph_stats import get_graph_stats
from pipeline.confidence import get_confidence
# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
database.init_db()
st.set_page_config(
    page_title="Analytos Brain",
    page_icon="🧠",
    layout="wide"
)

# -------------------------------------------------
# SESSION STATE INITIALIZATION
# -------------------------------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "messages" not in st.session_state:
    st.session_state.messages = []

if "question" not in st.session_state:
    st.session_state.question = ""

if "current_chat_id" not in st.session_state:
    st.session_state.current_chat_id = None

# -------------------------------------------------
# LOGIN / SIGNUP PAGE
# -------------------------------------------------

if not st.session_state.logged_in:

    st.title("🧠 Analytos Brain")
    st.subheader("Knowledge Graph + Hybrid RAG")

    login_tab, signup_tab = st.tabs(["Login", "Sign Up"])

    # ---------------- LOGIN ----------------
    with login_tab:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login", use_container_width=True):
            if login(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username

                # Load chat history on successful login
                chats = load_messages(username)
                st.session_state.messages = [
                    {"role": role, "content": message}
                    for role, message in chats
                ]

                st.rerun()
            else:
                st.error("Invalid username or password.")

    # ---------------- SIGNUP ----------------
    with signup_tab:
        new_user = st.text_input("Create Username")
        new_password = st.text_input("Create Password", type="password")

        if st.button("Create Account", use_container_width=True):
            if signup(new_user, new_password):
                st.success("Account created successfully. Please log in.")
            else:
                st.error("Username already exists.")

    st.stop()

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

with st.sidebar:
    st.title("🧠 Analytos Brain")
    st.success(f"Logged in as\n\n**{st.session_state.username}**")
    st.page_link(
        "pages/Review.py",
        label="Human Review"
    )
    # Dynamic Action Buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("➕ New Chat", use_container_width=True):
            st.session_state.messages = []
            st.session_state.question = ""
            st.rerun()

    with col2:
        if st.button("Clear Chat", use_container_width=True):
            st.session_state.messages = []
            # Optional: Add backend function call here if persistent messages need deletion
            # database.clear_user_chat_history(st.session_state.username)
            st.rerun()

    if st.button("Logout", use_container_width=True, type="secondary"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.messages = []
        st.session_state.question = ""
        st.rerun()

    st.divider()

    # Persistent Chat History Sidebar (ChatGPT style)
    st.markdown("### 💬 Chat History")
    all_chats = load_messages(st.session_state.username)
    user_queries = [msg for role, msg in all_chats if role == "user"]

    if user_queries:
        # Show last 10 unique prompts as conversational history buttons
        for past_q in list(dict.fromkeys(user_queries))[-10:]:
            if st.button(f"🗣️ {past_q[:25]}...", use_container_width=True, key=f"hist_{past_q}"):
                st.session_state.question = past_q
    else:
        st.caption("No past queries found.")

    st.divider()

    # Dynamic Graph Statistics
    st.markdown("## 📊 Graph Statistics")
    stats = get_graph_stats()

    for key, value in stats.items():
        st.metric(key, value)

    st.divider()

    st.markdown("## 💡 Suggested Questions")
    suggestions = [
        "Who are Stockly competitors?",
        "Who are Stockly customers?",
        "Which industries use Stockly?",
        "What features does Blue Yonder have?",
        "How does Stockly reduce stockouts?"
    ]

    for q in suggestions:
        if st.button(q, use_container_width=True):
            st.session_state.question = q

    st.divider()

    st.caption("Powered By")
    st.write("✅ Omnigraph")
    st.write("✅ ChromaDB")
    st.write("✅ LangChain")
    st.write("✅ Groq")

# -------------------------------------------------
# MAIN PAGE
# -------------------------------------------------

st.title("🧠 Analytos Brain")
st.subheader("Knowledge Graph + Hybrid RAG Assistant")

# -------------------------------------------------
# DISPLAY CHAT HISTORY
# -------------------------------------------------

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -------------------------------------------------
# CHAT INPUT & EXECUTION
# -------------------------------------------------

question = st.chat_input("Ask about Stockly...")

if question is None and st.session_state.question:
    question = st.session_state.question

if question:
    # Reset active state queue
    st.session_state.question = ""

    # Log user message
    st.session_state.messages.append({"role": "user", "content": question})
    save_message(st.session_state.username, "user", question)

    with st.chat_message("user"):
        st.markdown(question)

    query_used = select_query(question)

    # Process answer with timing metrics
    with st.spinner("Searching Knowledge Graph + RAG..."):
        start_time = time.time()
        
        # Support both standard ask signature and optional confidence score
        result = ask(question)
        if isinstance(result, tuple) and len(result) == 3:
            answer, context, confidence = result
        else:
            answer, context = result[0], result[1]
            confidence = get_confidence(context) # Computed default if not returned dynamically

        end_time = time.time()
        response_time = round(end_time - start_time, 2)

    # Save Assistant Response
    st.session_state.messages.append({"role": "assistant", "content": answer})
    save_message(st.session_state.username, "assistant", answer)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        text = ""

        # Stream text response to UI
        for word in answer.split():
            text += word + " "
            placeholder.markdown(text)
            time.sleep(0.02)

        st.success("Answer generated successfully.")

        # Performance Metrics Card
        m_col1, m_col2, m_col3 = st.columns(3)
        with m_col1:
            st.metric(
                "Graph Query",
                query_used
                )
        with m_col2:
            st.metric(
                "Response Time",
                f"{response_time}s"
                )
        with m_col3:
            st.caption(f"🎯 Confidence Score: **{confidence}**")

        st.markdown("---")

        # Enhanced Sources Card
        st.markdown("### 📚 Source Attribution & Metadata")
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
            **Primary Knowledge Retrieval:**
            * 📊 **Omnigraph DB:** Knowledge Graph Structure
            * 📄 **Stockly Vector Core:** Product Documentation
            """)
        with c2:
            st.markdown("### 📚 Sources")

            st.info("📊 Omnigraph Knowledge Graph")

            st.info("📄 Stockly Product Overview")

            st.info("📄 Customer Case Studies")

        with st.expander("🔍 Retrieved Context"):
            st.code(context)

        with st.expander("📝 Full Raw Output"):
            st.write(answer)
