import sqlite3

def save_to_db(records, db_path="data/osint.db"):
    """Save collected records into a SQLite database"""
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Create table if not exists
    cur.execute("""
    CREATE TABLE IF NOT EXISTS osint_data (
        platform TEXT,
        user TEXT,
        timestamp TEXT,
        text TEXT,
        url TEXT,
        sentiment REAL
    )
    """)

    for r in records:
        cur.execute("INSERT INTO osint_data VALUES (?, ?, ?, ?, ?, ?)",
                    (r.get("platform"), r.get("user"), r.get("timestamp"),
                     r.get("text"), r.get("url"), r.get("sentiment", 0)))
    conn.commit()
    conn.close()
