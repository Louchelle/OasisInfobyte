import random
import string
from tkinter import *
from tkinter import messagebox


def copy():
    password = password_label["text"]
    app.clipboard_clear()
    app.clipboard_append(password)
    app.update()
    message = messagebox.showinfo(title="Copied", message="Copied to clipboard")
    return message


# Generating password
def generator():
    small_alph = string.ascii_lowercase
    big_alph = string.ascii_uppercase
    nums = string.digits
    special = string.punctuation

    pass_length = int(length_box.get())

    password = ""

    if complexity.get() == 1:
        password = "".join(random.sample(small_alph, pass_length))
        password_label.config(text=password)
    if complexity.get() == 2:
        password = "".join(random.sample(small_alph + big_alph, pass_length))
        password_label.config(text=password)
    if complexity.get() == 3:
        password = "".join(
            random.sample(small_alph + big_alph + nums + special, pass_length))
        password_label.config(text=password)


font1 = ("Arial", 18, "bold")
font2 = ("Arial", 14, "bold")

app = Tk()
app.config(bg="#020B2D")
app.geometry("300x500")
app.title("Password Generator")

# Length of password
length = IntVar()
length_label = Label(app,
                     text="Password Length:",
                     font=font1,
                     bg="#020B2D",
                     fg="#CFBE10")
length_label.grid(pady=10)
length_box = Spinbox(app,
                     textvariable=length,
                     width=10,
                     from_=4,
                     to=25,
                     font=font2,
                     bg="#8F8F8F")
length_box.grid(pady=5)

# Complexity of Password
complexity = IntVar()
complexity_label = Label(app,
                         text="Password Strength:",
                         font=font1,
                         bg="#020B2D",
                         fg="#CFBE10")
complexity_label.grid(pady=10)

# Complexity buttons
okay_r_button = Radiobutton(app,
                            text="FAIR",
                            value="1",
                            variable=complexity,
                            font=font2,
                            bg="#020B2D",
                            fg="#CFBE10")
okay_r_button.grid(pady=5)

good_r_button = Radiobutton(app,
                            text="MODERATE",
                            value="2",
                            variable=complexity,
                            font=font2,
                            bg="#020B2D",
                            fg="#CFBE10")
good_r_button.grid(pady=5)

excellent_r_button = Radiobutton(app,
                                 text="PROTECTIVE",
                                 value="3",
                                 variable=complexity,
                                 font=font2,
                                 bg="#020B2D",
                                 fg="#CFBE10")
excellent_r_button.grid(pady=5)


# Generate Button
generate_button = Button(app,
                         command=generator,
                         text="Generate Password",
                         font=font1,
                         fg="#CFBE10",
                         bg="#8F8F8F")
generate_button.grid(pady=15, padx=25)

# Password Field
password_label = Label(app,
                       text="",
                       width=20,
                       bd=3,
                       font=font2,
                       bg="#8F8F8F")
password_label.grid(pady=5, padx=5)

# Copy Button
copy_button = Button(app,
                     command=copy,
                     text="Copy",
                     font=font1,
                     fg="#CFBE10",
                     bg="#8F8F8F")
copy_button.grid(pady=10, padx=5)

app.mainloop()
