import sqlite3 as sq
conn = sq.connect("plantdb.db")
c = conn.cursor()
def find_details(label):
    c.execute("SELECT * FROM plantdb WHERE id=?",(label,))
    data=c.fetchall()
    return data
    conn.close()
