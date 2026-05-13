from tkinter import *
from tkinter import messagebox

# ================= WINDOW =================

root = Tk()

root.title("Smart BMI Tracker")
root.geometry("520x760")
root.config(bg="#121212")
root.resizable(False, False)

# ================= FUNCTION =================

def calculate_bmi():

    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        age = int(age_entry.get())
        gender = gender_var.get()

        bmi = weight / (height ** 2)

        result_label.config(
            text=f"Your BMI: {bmi:.2f}",
            fg="white"
        )

        # BMI Categories
        if bmi < 18.5:

            category = "Underweight"
            color = "orange"

            suggestion = (
                "Eat nutritious food, increase protein intake, "
                "and maintain a healthy diet."
            )

        elif bmi < 25:

            category = "Normal Weight"
            color = "#00FF7F"

            suggestion = (
                "Great! Maintain your healthy lifestyle "
                "with balanced food and exercise."
            )

        elif bmi < 30:

            category = "Overweight"
            color = "yellow"

            suggestion = (
                "Regular exercise and balanced diet recommended."
            )

        else:

            category = "Obese"
            color = "red"

            suggestion = (
                "Consult a healthcare expert and follow "
                "a proper fitness plan."
            )

        category_label.config(
            text=category,
            fg=color
        )

        # Personalized Message
        personal_msg = (
            f"{gender}, Age {age}: {suggestion}"
        )

        suggestion_label.config(
            text=personal_msg
        )

    except:

        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numbers!"
        )


# ================= CLEAR FUNCTION =================

def clear_fields():

    weight_entry.delete(0, END)
    height_entry.delete(0, END)
    age_entry.delete(0, END)

    result_label.config(text="")
    category_label.config(text="")
    suggestion_label.config(text="")

    gender_var.set("Select")


# ================= HEADING =================

heading = Label(
    root,
    text="Smart BMI Tracker",
    font=("Poppins", 28, "bold"),
    bg="#121212",
    fg="#00FFD1"
)

heading.pack(pady=25)

# ================= WEIGHT =================

weight_label = Label(
    root,
    text="Enter Weight (kg)",
    font=("Poppins", 14),
    bg="#121212",
    fg="white"
)

weight_label.pack(pady=8)

weight_entry = Entry(
    root,
    font=("Poppins", 14),
    width=24,
    bg="#2A2A2A",
    fg="white",
    insertbackground="white",
    border=0
)

weight_entry.pack(ipady=8)

# ================= HEIGHT =================

height_label = Label(
    root,
    text="Enter Height (m)",
    font=("Poppins", 14),
    bg="#121212",
    fg="white"
)

height_label.pack(pady=12)

height_entry = Entry(
    root,
    font=("Poppins", 14),
    width=24,
    bg="#2A2A2A",
    fg="white",
    insertbackground="white",
    border=0
)

height_entry.pack(ipady=8)

# ================= AGE =================

age_label = Label(
    root,
    text="Enter Age",
    font=("Poppins", 14),
    bg="#121212",
    fg="white"
)

age_label.pack(pady=12)

age_entry = Entry(
    root,
    font=("Poppins", 14),
    width=24,
    bg="#2A2A2A",
    fg="white",
    insertbackground="white",
    border=0
)

age_entry.pack(ipady=8)

# ================= GENDER =================

gender_label = Label(
    root,
    text="Select Gender",
    font=("Poppins", 14),
    bg="#121212",
    fg="white"
)

gender_label.pack(pady=12)

gender_var = StringVar()
gender_var.set("Select")

gender_menu = OptionMenu(
    root,
    gender_var,
    "Male",
    "Female"
)

gender_menu.config(
    font=("Poppins", 12),
    bg="#00FFD1",
    fg="black",
    width=12,
    border=0
)

gender_menu.pack(pady=5)

# ================= BUTTON FRAME =================

btn_frame = Frame(
    root,
    bg="#121212"
)

btn_frame.pack(pady=25)

# ================= CALCULATE BUTTON =================

calculate_btn = Button(
    btn_frame,
    text="Calculate BMI",
    font=("Poppins", 13, "bold"),
    bg="#00FFD1",
    fg="black",
    activebackground="#00c9a7",
    activeforeground="white",
    padx=15,
    pady=10,
    border=0,
    cursor="hand2",
    command=calculate_bmi
)

calculate_btn.grid(row=0, column=0, padx=10)

# ================= CLEAR BUTTON =================

clear_btn = Button(
    btn_frame,
    text="Clear",
    font=("Poppins", 13, "bold"),
    bg="#ff4d4d",
    fg="white",
    activebackground="#ff1a1a",
    activeforeground="white",
    padx=20,
    pady=10,
    border=0,
    cursor="hand2",
    command=clear_fields
)

clear_btn.grid(row=0, column=1, padx=10)

# ================= RESULT =================

result_label = Label(
    root,
    text="",
    font=("Poppins", 20, "bold"),
    bg="#121212",
    fg="white"
)

result_label.pack(pady=12)

# ================= CATEGORY =================

category_label = Label(
    root,
    text="",
    font=("Poppins", 18, "bold"),
    bg="#121212"
)

category_label.pack(pady=5)

# ================= SUGGESTION =================

suggestion_label = Label(
    root,
    text="",
    font=("Poppins", 12),
    bg="#121212",
    fg="white",
    wraplength=420,
    justify="center"
)

suggestion_label.pack(pady=18)

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