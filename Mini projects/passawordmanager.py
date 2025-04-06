import tkinter as tk
from tkinter import messagebox

master_password = "140320"

def check_password():
    entered_pw = password_entry.get()

    if entered_pw == master_password:
        login_window.destroy()
        open_main_app()
    else:
        messagebox.showerror("Access Denied", "Wrong master password!")

def open_main_app():
    app = tk.Tk()
    app.title("Password Manager")

    tk.Label(app, text="Website:").grid(row=0, column=0)
    website_entry = tk.Entry(app)
    website_entry.grid(row=0, column=1)

    tk.Label(app, text="Username:").grid(row=1, column=0)
    username_entry = tk.Entry(app)
    username_entry.grid(row=1, column=1)

    tk.Label(app, text="Password:").grid(row=2, column=0)
    password_entry_app = tk.Entry(app, show="*")
    password_entry_app.grid(row=2, column=1)

    def save_password():
        website = website_entry.get()
        username = username_entry.get()
        password = password_entry_app.get()

        if website and username and password:
            with open("password.txt", "a") as f:
                f.write(f"{website} | {username} | {password}\n")
            
            messagebox.showinfo("Saved", "Your password is saved!")

            website_entry.delete(0, tk.END)
            username_entry.delete(0, tk.END)
            password_entry_app.delete(0, tk.END)
        else:
            messagebox.showwarning("Missing info", "Fill in all fields!")
    
    tk.Button(app, text="Save Password", command=save_password).grid(row=3, column=0, columnspan=2, pady=10)

    app.mainloop()

# Create the login window
login_window = tk.Tk()
login_window.title("Login")

tk.Label(login_window, text="Enter Master Password:").pack(pady=10)
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()
tk.Button(login_window, text="Login", command=check_password).pack(pady=10)

login_window.mainloop()