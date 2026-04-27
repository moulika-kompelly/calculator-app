import random
import string
import tkinter as tk
from tkinter import messagebox

# function to generate password
def generate_password():
    try:
        length = int(entry_length.get())

        characters = ""
        if var_letters.get():
            characters += string.ascii_letters
        if var_digits.get():
            characters += string.digits
        if var_symbols.get():
            characters += string.punctuation
            if characters == "":
               messagebox.showerror("Error", "Select at least one option!")
            return

        password = "".join(random.choice(characters) for _ in range(length))
        result_var.set(password)

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number!")

# create window
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x300")
# title
tk.Label(root, text="Password Generator", font=("Arial", 14)).pack(pady=10)

# length input
tk.Label(root, text="Password Length:").pack()
entry_length = tk.Entry(root)
entry_length.pack()

# options
var_letters = tk.IntVar(value=1)
var_digits = tk.IntVar(value=1)
var_symbols = tk.IntVar(value=1)

tk.Checkbutton(root, text="Include Letters", variable=var_letters).pack()
tk.Checkbutton(root, text="Include Numbers", variable=var_digits).pack()
tk.Checkbutton(root, text="Include Symbols", variable=var_symbols).pack()

# generate button
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)
# result
result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, width=30).pack()

# run app
root.mainloop()