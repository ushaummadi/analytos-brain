# 🧠 Analytos Brain  
## Knowledge Graph + Hybrid RAG Context Layer using Omnigraph

Analytos Brain is a governed AI context layer built on top of the open-source **Omnigraph** engine.

The goal is to create a single source of truth where company knowledge can be:

- Ingested from documents
- Extracted into structured entities using LLMs
- Reviewed and approved by humans
- Stored in a governed Knowledge Graph
- Accessed by humans through a dashboard
- Accessed by AI agents through MCP

The system demonstrates the complete knowledge lifecycle:

```
Seed Documents
      |
      ↓
LLM Extraction Pipeline
      |
      ↓
Omnigraph Branch
      |
      ↓
Human Review (HITL)
      |
      ↓
Approve / Reject
      |
      ↓
Merge to Main
      |
      ↓
Dashboard + MCP Agents
```

---

# 🚀 Features

## ✅ Omnigraph Knowledge Graph

Implemented using:

- Omnigraph open-source engine
- Typed schemas
- Graph queries
- Branch-based governance


Supported entities:

- Product
- Feature
- Proof Point
- Persona
- ICP Segment
- Customer
- Industry
- Competitor
- Competitor Features


Supported relationships:

```
Product HAS_FEATURE Feature

Product PROVEN_BY ProofPoint

Product TARGETS Persona

Customer BELONGS_TO Industry

Product HAS_COMPETITOR Competitor
```

---

# 🏗️ Architecture


```
                 Seed Data
                    |
                    |
                    ↓

          Ingestion Pipeline
          -------------------
          Parse Documents
          LLM Extraction
          Normalize JSON
          Generate Mutations

                    |
                    ↓

          Omnigraph Branch
          ingest-stockly

                    |
                    ↓

            HITL Review UI

          +-------------+
          | Approve     |
          | Reject      |
          +-------------+

                    |
                    ↓

              Main Branch

              /        \

             /          \

            ↓            ↓

     Dashboard        MCP Server

     Humans          AI Agents

```

---

# 📂 Project Structure


```
analytos-brain/

│
├── app.py
│
├── auth.py
├── database.py
├── review.py
├── policy.py
│
├── mcp_server.py
│
├── pipeline/
│   │
│   ├── extract.py
│   ├── hybrid_search.py
│   ├── answer_generator.py
│   ├── query_router.py
│   ├── graph_stats.py
│   └── confidence.py
│
│
├── pages/
│   │
│   ├── Review.py
│   ├── Content_Agent.py
│   ├── GTM_Agent.py
│   └── MCP_Test.py
│
│
├── schema/
│   │
│   ├── Product.pg
│   ├── Feature.pg
│   ├── Customer.pg
│   ├── queries.gq
│
│
├── seed-data/
│
├── vector_db/
│
├── graph.omni
│
├── requirements.txt
│
└── README.md

```

---

# 🛠️ Tech Stack

## Knowledge Graph

- Omnigraph
- Graph Schema
- Typed Queries
- Branch Governance


## AI / LLM

- LangChain
- Groq LLM
- HuggingFace Embeddings


## Retrieval

Hybrid Retrieval:

- Knowledge Graph Search
- Vector Similarity Search
- ChromaDB


## Frontend

- Streamlit


## Database

- SQLite

Used for:

- User authentication
- Chat history
- Approval history


## Agent Communication

- MCP Server
- FastMCP

---

# 📥 Installation

Clone repository:


```bash
git clone <repository-url>

cd analytos-brain
```


Install dependencies:


```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Setup


Create:

```
.streamlit/secrets.toml
```


Add:


```toml
GROQ_API_KEY="your_api_key"
```

---

# ▶️ Running the Application


## Start Dashboard


```bash
streamlit run app.py
```


Open:


```
http://localhost:8501
```

---

# 🔄 Data Ingestion Pipeline


The ingestion pipeline converts unstructured documents into structured graph knowledge.


Run:


```bash
python pipeline/extract.py
```


Example extraction:


Input:

```
Stockly reduces stockouts by 35%
```


Output:


```json
{
 "product":"Stockly",

 "proof_points":[
    "Reduced stockouts by 35%"
 ],

 "features":[
    "Demand Forecasting",
    "Inventory Planning"
 ]
}
```


The pipeline creates graph mutations automatically.

---

# 🌿 Branch Governance


All ingestion happens on a separate branch.


Example:


```
main

 |
 |
ingest-stockly
```


No agent or pipeline write directly modifies main.


---

# 🧑 Human-in-the-Loop Review (HITL)


Review page:


```
pages/Review.py
```


Features:


- View branch diff
- Approve changes
- Reject changes
- Merge approved branch
- Track approval history


Workflow:


```
Ingestion

   ↓

Branch Created

   ↓

Human Review

   ↓

Approve

   ↓

Merge to Main

```

---

# 🔎 Hybrid Search


The assistant combines:


## Graph Search

Retrieves:

- Products
- Customers
- Competitors
- Features
- Industries


## Vector Search

Retrieves:

- Product documents
- Case studies
- Supporting context


Flow:


```
Question

 ↓

Query Router

 ↓

Omnigraph Query

 +

Chroma Similarity Search

 ↓

LLM Answer

```

---

# 💬 Dashboard Features


The Streamlit dashboard provides:


## Authentication

- Signup
- Login
- Logout


## Chat Features

- ChatGPT style interface
- Persistent chat history
- Previous conversations
- New Chat
- Clear Chat


## Knowledge Features

- Entity search
- Hybrid retrieval
- Source attribution
- Graph query tracking


## Analytics

- Graph statistics
- Response time
- Confidence score

---

# 🤖 AI Agents


## 1. Content Agent


Purpose:

Generate marketing content using only approved graph knowledge.


Example:


Input:

```
Write a blog about Stockly
```


Agent retrieves:


- Product features
- Proof points
- Metrics


Output:

A grounded blog draft.


Restrictions:

Content Agent cannot access:

```
EmailThread
Internal Documents
```

---

## 2. GTM Agent


Purpose:

Generate prospecting intelligence.


Example:


Input:

```
Who should we prospect for Stockly?
```


Output:


```
Target Industry:
Retail

Persona:
Supply Chain Manager

Use Case:
Inventory Optimization

Proof:
Reduced stockouts by 35%

```

---

# 🔐 Access Control


Role based access simulation:


## content-agent


Allowed:

```
Product
Feature
ProofPoint
```


Blocked:

```
EmailThread
Internal Data
```


---

## gtm-agent


Allowed:


```
Product
ICP Segment
Persona
ProofPoint
Customer
```

---

# 🔌 MCP Server


The graph is exposed through MCP.


Run:


```bash
python mcp_server.py
```


Available MCP tool:


```
search_graph(question)
```


Example:


```
Who are Stockly competitors?
```


Response:


```
Blue Yonder

Netstock
```

---

# 📊 Demo Queries


Try:


```
Who are Stockly competitors?
```


```
Who are Stockly customers?
```


```
Which industries use Stockly?
```


```
What features does Blue Yonder have?
```


```
How does Stockly reduce stockouts?
```

---

# 🧪 Evaluation Coverage


| Requirement | Status |
|---|---|
| Omnigraph Setup | ✅ |
| Schema | ✅ |
| Typed Queries | ✅ |
| LLM Extraction | ✅ |
| Branch Workflow | ✅ |
| HITL Review | ✅ |
| Dashboard | ✅ |
| Hybrid Search | ✅ |
| Vector Retrieval | ✅ |
| Graph Retrieval | ✅ |
| Login | ✅ |
| Chat History | ✅ |
| Content Agent | ✅ |
| GTM Agent | ✅ |
| MCP Server | ✅ |
| Role Based Access | ✅ |


---

# 🌐 Deployment


Dashboard:

```
(Add Streamlit URL)
```


MCP Endpoint:

```
(Add MCP URL)
```


---

# 🎥 Demo Flow


The demo shows:


1. Document ingestion

2. LLM extraction

3. Graph mutation creation

4. Branch creation

5. Human approval

6. Merge to main

7. Dashboard query

8. MCP agent access

9. Role based security


---

# 👩‍💻 Author


**Usha Rani Ummadi**

B.Tech CSE (AI)

AI / Generative AI Engineer


Skills:

- Python
- LangChain
- LangGraph
- RAG
- Omnigraph
- MCP
- Streamlit
- FastAPI


---

# 📄 License

MIT License
