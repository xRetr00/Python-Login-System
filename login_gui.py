import customtkinter
import socket
import tkinter.messagebox as messagebox
import webbrowser
import hashlib

# System Settings
customtkinter.set_appearance_mode("System")

# GUI Design
def show_message_box(title, message, icon=None, parent=None):
    messagebox.showinfo(title, message, icon=icon, parent=parent)

def show_error_box(title, message, icon=None, parent=None):
    messagebox.showerror(title, message, icon=icon, parent=parent)

def show_warning_box(title, message, icon=None, parent=None):
    messagebox.showwarning(title, message, icon=icon, parent=parent)

def buy_key():
    url = "https://github.com/ShereefX01" #Add  Here Your Keys Store Link!
    webbrowser.open(url)

server = 'localhost'
port = 9966

def login():
    key = Key_entry.get()
    version = 2.0  # This is To Prevent The User From Using Outdated Version From Your Tool

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((server, port))

            hashed_key = hashlib.sha512(key.encode()).hexdigest()

            message = f"{hashed_key}:{version}"
            client.send(message.encode())

            response = client.recv(1024).decode().strip()
            print(response)
            # Make Sure If You Edit SomeThing Here Don't Forget To Edit it On The Server Code Too!
            if response.startswith("Login Successful!"):
                show_message_box("Authentication Successfully :)", f"{response}")
                if remeber.get() == 1:
                    with open('credentials.txt', 'a') as f:
                        f.write(f"{key}\n")
                        # You Can Add The Main GUI Here!

            else:
                show_error_box("Authentication failed!", f"{response}")

    except socket.error:
        show_error_box("Connection Error", "Failed to connect to server")



app = customtkinter.CTk()
app.geometry("480x250")
app.title("Python Login System")
#app.iconbitmap("icon.ico")
app.resizable(False, False) # You Can Edit This As U Need!



frame = customtkinter.CTkFrame(master=app)
frame.pack(pady=12, padx=10, fill="both", expand=True)


label = customtkinter.CTkLabel(master=frame, text="Welcome To Login GUI", font=("Arial Black", 22))
label.pack(pady=10, padx=10)

label = customtkinter.CTkLabel(master=frame, text="By @ShereefX01 2023 ", font=("Arial Black", 12))
label.pack(side='bottom', anchor='e', pady=5, padx=5)

Key_entry = customtkinter.CTkEntry(master=frame, width=400, placeholder_text="Please Enter Your Key Here")
Key_entry.pack(pady=10, padx=10)

remeber = customtkinter.CTkCheckBox(master=frame, text="Remember Me", font=("Arial Black", 15))
remeber.pack(side='left', pady=10, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login, font=("Arial Black", 20))
button.pack(side='right', pady=10, padx=10)

button_buy_key = customtkinter.CTkButton(master=frame, text="Buy Key", font=("Arial Black", 20), command=buy_key)
button_buy_key.pack(side='right', pady=10, padx=10)

app.mainloop()

