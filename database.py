import sqlite3

conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()

def init_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chats(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        role TEXT,
        message TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS approvals(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        branch TEXT,
        approved_by TEXT,
        approved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()

# Create tables automatically
init_db()
# -----------------------------------------
# Approval Functions
# -----------------------------------------

def save_approval(branch, approved_by):
    """
    Save approval information after a branch is merged.
    """

    cursor.execute(
        """
        INSERT INTO approvals
        (branch, approved_by)
        VALUES (?, ?)
        """,
        (branch, approved_by)
    )

    conn.commit()


def get_approvals():
    """
    Get all approvals ordered by latest first.
    """

    cursor.execute(
        """
        SELECT
            branch,
            approved_by,
            approved_at
        FROM approvals
        ORDER BY approved_at DESC
        """
    )

    return cursor.fetchall()


# -----------------------------------------
# Optional Utility
# -----------------------------------------

def clear_approvals():
    """
    Delete all approval history.
    """

    cursor.execute("DELETE FROM approvals")

    conn.commit()
