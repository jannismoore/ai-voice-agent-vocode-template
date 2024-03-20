import sqlite3
import os
from typing import Optional

from config import DB_PATH

DB_FILE_PATH = DB_PATH + '/transcripts.db'

# Ensure the database and table are created when the script runs
def initialize_db():
    conn = sqlite3.connect(DB_FILE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transcripts (
            conversation_id TEXT PRIMARY KEY,
            user_id TEXT NOT NULL,
            transcript TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

initialize_db()

def add_transcript(conversation_id: str, user_id: int, transcript: str) -> None:
    conn = sqlite3.connect(DB_FILE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO transcripts (conversation_id, user_id, transcript) 
        VALUES (?, ?, ?)
        ON CONFLICT(conversation_id) DO UPDATE SET transcript = transcript || ?;
    ''', (conversation_id, user_id, transcript, transcript))
    conn.commit()
    conn.close()

def get_transcript(conversation_id: str) -> Optional[str]:
    conn = sqlite3.connect(DB_FILE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT transcript FROM transcripts WHERE conversation_id = ?;
    ''', (conversation_id,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None

def delete_transcript(conversation_id: str) -> bool:
    conn = sqlite3.connect(DB_FILE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM transcripts WHERE conversation_id = ?;
    ''', (conversation_id,))
    changes = conn.total_changes
    conn.commit()
    conn.close()
    return changes > 0