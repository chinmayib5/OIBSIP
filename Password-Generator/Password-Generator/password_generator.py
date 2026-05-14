from tkinter import *
from tkinter import messagebox
import random
import string

# ================= WINDOW =================

root = Tk()

root.title("Password Generator")
root.geometry("500x500")
root.config(bg="#121212")
root.resizable(False, False)

# ================= FUNCTION =================

def generate_password():

    try:

        length = int(length_entry.get())

        if length <= 0:
            messagebox.showerror(
                "Error",
                "Enter positive number!"
            )
            return

        characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )

        password = ""

        for i in range(length):
            password += random.choice(characters)

        password_entry.delete(0, END)
        password_entry.insert(0, password)

    except:

        messagebox.showerror(
            "Error",
            "Enter valid number!"
        )

# ================= COPY FUNCTION =================

def copy_password():

    password = password_entry.get()

    root.clipboard_clear()
    root.clipboard_append(password)

    messagebox.showinfo(
        "Copied",
        "Password copied successfully!"
    )

# ================= HEADING =================

heading = Label(
    root,
    text="Password Generator",
    font=("Poppins", 26, "bold"),
    bg="#121212",
    fg="#00FFD1"
)

heading.pack(pady=30)

# ================= LENGTH =================

length_label = Label(
    root,
    text="Enter Password Length",
    font=("Poppins", 14),
    bg="#121212",
    fg="white"
)

length_label.pack(pady=10)

length_entry = Entry(
    root,
    font=("Poppins", 14),
    width=20,
    bg="#2A2A2A",
    fg="white",
    insertbackground="white",
    border=0
)

length_entry.pack(ipady=8)

# ================= BUTTON =================

generate_btn = Button(
    root,
    text="Generate Password",
    font=("Poppins", 14, "bold"),
    bg="#00FFD1",
    fg="black",
    activebackground="#00c9a7",
    activeforeground="white",
    padx=20,
    pady=10,
    border=0,
    cursor="hand2",
    command=generate_password
)

generate_btn.pack(pady=30)

# ================= PASSWORD BOX =================

password_entry = Entry(
    root,
    font=("Poppins", 14),
    width=28,
    bg="#2A2A2A",
    fg="#00FFD1",
    insertbackground="white",
    border=0,
    justify="center"
)

password_entry.pack(ipady=10)

# ================= COPY BUTTON =================

copy_btn = Button(
    root,
    text="Copy Password",
    font=("Poppins", 13, "bold"),
    bg="#ff4d4d",
    fg="white",
    activebackground="#ff1a1a",
    activeforeground="white",
    padx=20,
    pady=10,
    border=0,
    cursor="hand2",
    command=copy_password
)

copy_btn.pack(pady=25)

# ================= FOOTER =================

footer = Label(
    root,
    text="Developed by Chinmayi 💻",
    font=("Poppins", 10),
    bg="#121212",
    fg="gray"
)

footer.pack(side=BOTTOM, pady=10)

# ================= RUN =================

root.mainloop()