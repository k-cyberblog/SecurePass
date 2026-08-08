import tkinter as tk
from tkinter import messagebox

from password_checker import check_password
from password_generator import generate_password


def analyze_password():

    password = password_entry.get()

    if not password:
        messagebox.showwarning(
            "Warning",
            "Please enter a password."
        )
        return

    score, strength, entropy, suggestions = check_password(password)

    result_label.config(
        text=f"Strength: {strength}\nScore: {score}/100"
    )

    entropy_label.config(
        text=f"Estimated Entropy: {entropy} bits"
    )

    if suggestions:

        suggestion_text = "\n".join(
            "• " + suggestion
            for suggestion in suggestions
        )

        suggestions_label.config(
            text=suggestion_text
        )

    else:

        suggestions_label.config(
            text="✓ Excellent password! No major weaknesses detected."
        )


def toggle_password():

    if password_entry.cget("show") == "":

        password_entry.config(show="*")
        show_button.config(text="Show")

    else:

        password_entry.config(show="")
        show_button.config(text="Hide")


def generate_new_password():

    try:

        length = int(length_entry.get())

        if length < 6 or length > 64:

            messagebox.showwarning(
                "Invalid Length",
                "Password length must be between 6 and 64."
            )

            return

        password = generate_password(
            length,
            uppercase_var.get(),
            lowercase_var.get(),
            numbers_var.get(),
            special_var.get()
        )

        generated_password_entry.delete(0, tk.END)

        generated_password_entry.insert(
            0,
            password
        )

    except ValueError as error:

        messagebox.showwarning(
            "Error",
            str(error)
        )


def copy_password():

    password = generated_password_entry.get()

    if not password:

        messagebox.showwarning(
            "Warning",
            "Generate a password first."
        )

        return

    window.clipboard_clear()
    window.clipboard_append(password)

    messagebox.showinfo(
        "Copied",
        "Password copied to clipboard."
    )


# --------------------------------------------------
# MAIN WINDOW
# --------------------------------------------------

window = tk.Tk()

window.title(
    "SecurePass - Password Security Tool"
)

window.geometry(
    "650x750"
)

window.resizable(False, False)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

title_label = tk.Label(
    window,
    text="SecurePass",
    font=("Arial", 26, "bold")
)

title_label.pack(pady=(20, 5))


subtitle_label = tk.Label(
    window,
    text="Password Strength Analyzer & Secure Generator",
    font=("Arial", 11)
)

subtitle_label.pack(pady=(0, 20))


# --------------------------------------------------
# PASSWORD ANALYZER
# --------------------------------------------------

analyzer_frame = tk.LabelFrame(
    window,
    text=" Password Strength Analyzer ",
    font=("Arial", 12, "bold"),
    padx=15,
    pady=15
)

analyzer_frame.pack(
    fill="x",
    padx=25,
    pady=10
)


password_entry = tk.Entry(
    analyzer_frame,
    width=40,
    font=("Arial", 13),
    show="*"
)

password_entry.grid(
    row=0,
    column=0,
    padx=5,
    pady=10
)


show_button = tk.Button(
    analyzer_frame,
    text="Show",
    command=toggle_password
)

show_button.grid(
    row=0,
    column=1,
    padx=5
)


check_button = tk.Button(
    analyzer_frame,
    text="Analyze",
    command=analyze_password
)

check_button.grid(
    row=1,
    column=0,
    columnspan=2,
    pady=10
)


result_label = tk.Label(
    analyzer_frame,
    text="Strength: --\nScore: --/100",
    font=("Arial", 15, "bold")
)

result_label.grid(
    row=2,
    column=0,
    columnspan=2,
    pady=5
)


entropy_label = tk.Label(
    analyzer_frame,
    text="Estimated Entropy: -- bits",
    font=("Arial", 11)
)

entropy_label.grid(
    row=3,
    column=0,
    columnspan=2,
    pady=5
)


suggestions_label = tk.Label(
    analyzer_frame,
    text="Enter a password to analyze it.",
    wraplength=500,
    justify="left"
)

suggestions_label.grid(
    row=4,
    column=0,
    columnspan=2,
    pady=10
)


# --------------------------------------------------
# PASSWORD GENERATOR
# --------------------------------------------------

generator_frame = tk.LabelFrame(
    window,
    text=" Secure Password Generator ",
    font=("Arial", 12, "bold"),
    padx=15,
    pady=15
)

generator_frame.pack(
    fill="x",
    padx=25,
    pady=15
)


length_label = tk.Label(
    generator_frame,
    text="Password Length:"
)

length_label.grid(
    row=0,
    column=0,
    sticky="w",
    pady=5
)


length_entry = tk.Entry(
    generator_frame,
    width=10
)

length_entry.insert(
    0,
    "16"
)

length_entry.grid(
    row=0,
    column=1,
    sticky="w",
    pady=5
)


# Checkboxes

uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)


uppercase_check = tk.Checkbutton(
    generator_frame,
    text="Uppercase",
    variable=uppercase_var
)

uppercase_check.grid(
    row=1,
    column=0,
    sticky="w"
)


lowercase_check = tk.Checkbutton(
    generator_frame,
    text="Lowercase",
    variable=lowercase_var
)

lowercase_check.grid(
    row=1,
    column=1,
    sticky="w"
)


numbers_check = tk.Checkbutton(
    generator_frame,
    text="Numbers",
    variable=numbers_var
)

numbers_check.grid(
    row=2,
    column=0,
    sticky="w"
)


special_check = tk.Checkbutton(
    generator_frame,
    text="Special Characters",
    variable=special_var
)

special_check.grid(
    row=2,
    column=1,
    sticky="w"
)


generate_button = tk.Button(
    generator_frame,
    text="Generate Secure Password",
    command=generate_new_password
)

generate_button.grid(
    row=3,
    column=0,
    columnspan=2,
    pady=15
)


generated_password_entry = tk.Entry(
    generator_frame,
    width=45,
    font=("Arial", 12)
)

generated_password_entry.grid(
    row=4,
    column=0,
    padx=5,
    pady=5
)


copy_button = tk.Button(
    generator_frame,
    text="Copy",
    command=copy_password
)

copy_button.grid(
    row=4,
    column=1,
    padx=5
)


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

footer_label = tk.Label(
    window,
    text="SecurePass | Python Cybersecurity Mini Project",
    font=("Arial", 9)
)

footer_label.pack(
    pady=15
)


window.mainloop()
