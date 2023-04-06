import sqlite3
import socket
import threading
import datetime
import hashlib

def handle_connection(c):
    try:
        data = c.recv(1024).decode().strip()
        hashed_key, version = data.split(":")
        print(data)

        latest_version = "2.0" # Replace with the latest version number
        if version < latest_version:
            c.send("Login Failed! Version outdated! Please update the application.".encode())
            return
        
        with sqlite3.connect("Keys.db") as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Keys WHERE hashed_key = ?", (hashed_key,))
            result = cur.fetchone()

            if result:
                key_status = result[3]
                key_expire_str = result[2]
                key_expire = datetime.datetime.strptime(key_expire_str, "%Y-%m-%d %H:%M:%S")
                
                if key_status == "Active" and datetime.datetime.now() <= key_expire:
                    c.send(f"Login Successful! Key Expires On {key_expire_str}".encode())
                elif key_status == "Banned":
                    c.send("Login Failed! Key IS Banned".encode())
                else:
                    c.send("Login Failed! Key Has Expired".encode())

            else:
                c.send("Login Failed! Invalid Key".encode())

            cur.close()
            
    except Exception as e:
        print(f"Error: {e}")
        c.send("Login Failed! An error occurred during login. Please try again later.".encode())

    finally:
        c.close()


# Edit The Server And Port As U Need!
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9966))
server.listen()

while True:
    client, addr = server.accept()
    threading.Thread(target=handle_connection, args=(client,)).start()
