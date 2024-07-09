import sqlite3
import config

sql = sqlite3.connect(config.DB,  check_same_thread=False)
db = sql.cursor()

db.execute('''CREATE TABLE IF NOT EXISTS guild(
           guild INTEGER PRIMARY KEY, 
           role INTEGER
)''')
sql.commit()

def insert(guild, role):
    db.execute('INSERT OR REPLACE INTO guild (guild, role) VALUES (?, ?)', (guild, role,))
    sql.commit()

def select(guild):
    db.execute('SELECT role FROM guild WHERE guild = ?', (guild,))
    return db.fetchone()[0]