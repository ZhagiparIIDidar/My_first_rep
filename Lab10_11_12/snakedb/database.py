import psycopg2
from config import load_config

def connect_db():
    params = load_config()
    return psycopg2.connect(**params)

def init_db():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username TEXT UNIQUE NOT NULL
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS user_scores (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        level INTEGER NOT NULL,
        score INTEGER NOT NULL,
        saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    cur.close()
    conn.close()

def get_or_create_user(username):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()

    if user:
        user_id = user[0]
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()

    cur.close()
    conn.close()
    return user_id

def save_score(user_id, level, score):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO user_scores (user_id, level, score)
    VALUES (%s, %s, %s)
    """, (user_id, level, score))

    conn.commit()
    cur.close()
    conn.close()
