# === Modul db.py — SQLite Logging ===

import sqlite3
from datetime import datetime

DB_NAME = "emisi_minute.db"

def init_db():
    """Buat tabel database jika belum ada"""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS minute_avg (
            timestamp TEXT PRIMARY KEY,
            avg_co2 REAL
        )
    """)
    conn.commit()
    conn.close()

def simpan_avg_per_menit(avg_co2):
    """Simpan rata-rata CO2 per menit ke database"""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    ts = datetime.now().strftime("%Y-%m-%d %H:%M:00")
    cur.execute("INSERT OR REPLACE INTO minute_avg (timestamp, avg_co2) VALUES (?, ?)",
                (ts, avg_co2))

    conn.commit()
    conn.close()

def ambil_5_data_terakhir():
    """Ambil 5 data terakhir untuk ditampilkan"""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
        SELECT timestamp, avg_co2
        FROM minute_avg
        ORDER BY timestamp DESC
        LIMIT 5
    """)

    rows = cur.fetchall()
    conn.close()
    return rows


