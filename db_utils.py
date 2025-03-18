# db_utils.py
import sqlite3
import os

DB_NAME = "bitcharge_users.db"

def init_db():
    """
    Создаёт файл базы (если не существует) и таблицу users.
    Поля (id, name, email, password, verified, confirm_code).
    """
    if not os.path.exists(DB_NAME):
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                verified INTEGER NOT NULL DEFAULT 0,
                confirm_code TEXT
            );
        """)
        conn.commit()
        conn.close()

def user_exists(email: str) -> bool:
    """Проверяет, есть ли пользователь с таким email."""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE email = ?", (email,))
    row = cur.fetchone()
    conn.close()
    return (row is not None)

def create_user(name: str, email: str, password: str, code: str):
    """
    Создаёт нового пользователя с code (код подтверждения),
    verified=0 (не подтверждён).
    """
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO users(name, email, password, verified, confirm_code)
        VALUES (?, ?, ?, 0, ?)
    """, (name, email, password, code))
    conn.commit()
    conn.close()

def get_confirm_code(email: str):
    """Возвращает confirm_code для заданного email, или None, если нет пользователя."""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT confirm_code FROM users WHERE email = ?", (email,))
    row = cur.fetchone()
    conn.close()
    if row:
        return row[0]
    return None

def verify_user(email: str):
    """Ставит verified=1 (подтверждён) у пользователя с данным email."""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("UPDATE users SET verified=1 WHERE email = ?", (email,))
    conn.commit()
    conn.close()

def check_login(email: str, password: str) -> bool:
    """
    Проверяет, верны ли email+password.
    Если совпадает — возвращает True, иначе False.
    """
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        SELECT id FROM users
         WHERE email = ? AND password = ?
    """, (email, password))
    row = cur.fetchone()
    conn.close()
    return (row is not None)

def is_verified(email: str) -> bool:
    """Проверяет, verified ли пользователь с данным email."""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        SELECT verified FROM users
         WHERE email = ?
    """, (email,))
    row = cur.fetchone()
    conn.close()
    if row:
        return (row[0] == 1)
    return False
