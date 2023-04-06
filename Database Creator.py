import sqlite3
import hashlib

conn = sqlite3.connect('Keys.db')

conn.execute('''CREATE TABLE Keys
       (id INTEGER PRIMARY KEY AUTOINCREMENT,
       hashed_key TEXT NOT NULL,
       expiration_date DATETIME NOT NULL,
       status TEXT NOT NULL);''')

# Add a sample key to the table
key = "TestKey"
hashed_key = hashlib.sha512(key.encode()).hexdigest() 
expiration_date = "2024-12-31 23:59:59"  # Keep the format yyyy-mm-dd hh:mm:ss
status = "Active"  #the status ("Active", "Banned") As Server Setup!

conn.execute('''INSERT INTO Keys (hashed_key, expiration_date, status)
                 VALUES (?, ?, ?)''', (hashed_key, expiration_date, status))

conn.commit()

conn.close()
