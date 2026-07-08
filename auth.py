import sqlite3

conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()


def signup(username, password):

    try:
        cursor.execute(
            "INSERT INTO users(username,password) VALUES(?,?)",
            (username, password)
        )

        conn.commit()
        return True

    except:
        return False


def login(username, password):

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    return cursor.fetchone()


def save_message(username, role, message):

    cursor.execute(
        "INSERT INTO chats(username,role,message) VALUES(?,?,?)",
        (username, role, message)
    )

    conn.commit()


def load_messages(username):

    cursor.execute(
        "SELECT role,message FROM chats WHERE username=?",
        (username,)
    )

    return cursor.fetchall()