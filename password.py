import string
import random
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def on_generate():
    try:
        length = int(entry_length.get())
        if length < 1:
            messagebox.showerror("Error", "Please enter a positive number.")
        else:
            password = generate_password(length)
            entry_password.delete(0, tk.END)
            entry_password.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Create the main application window
app = tk.Tk()
app.title("Password Generator")
app.geometry("400x200")

# Create and place the widgets in the window
label_length = tk.Label(app, text="Enter the desired length for the password:")
label_length.pack(pady=10)

entry_length = tk.Entry(app)
entry_length.pack(pady=5)

button_generate = tk.Button(app, text="Generate Password", command=on_generate)
button_generate.pack(pady=10)

label_password = tk.Label(app, text="Generated Password:")
label_password.pack(pady=10)

entry_password = tk.Entry(app, width=50)
entry_password.pack(pady=5)

# Start the main event loop
app.mainloop()
