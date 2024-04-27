import customtkinter as ctk
from tkinter import messagebox

app = ctk.CTk()
app.geometry("280x320")
app.title("BMI Calculator")
app.config(bg="#283618")

# fonts
font1 = ("Arial", 24, "bold")
font2 = ("Arial", 20, "bold")
font3 = ("Arial", 26, "bold")
font4 = ("Arial", 28, "bold")


# Functions
def classification_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Healthy"
    else:
        return "Overweight"


def calculate_bmi():
    try:
        height_cm = int(height_entry.get())
        weight = int(weight_entry.get())
        height_m = height_cm / 100
        bmi = round(weight / (height_m ** 2), 2)
        clas = classification_bmi(bmi)
        result_label.configure(text=f"Your BMI is: {bmi} \n You are {clas} ")
    except ValueError:
        messagebox.showerror("Error", "You need to enter a valid number.")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Your height cannot be 0.")


# Height
height_label = ctk.CTkLabel(app,
                            text="Height(CM)",
                            font=font1,
                            text_color="#dda15e",
                            bg_color="#283618")
height_label.grid(row=1, column=0, padx=5, pady=10)
height_entry = ctk.CTkEntry(app,
                            font=font2,
                            text_color="Black",
                            bg_color="#283618",
                            corner_radius=5)
height_entry.grid(row=2, column=0, padx=5, pady=5)

# Weight
weight_label = ctk.CTkLabel(app,
                            text="Weight(KG)",
                            font=font1,
                            text_color="#dda15e",
                            bg_color="#283618")
weight_label.grid(row=3, column=0, padx=5, pady=10)
weight_entry = ctk.CTkEntry(app,
                            font=font2,
                            text_color="Black",
                            bg_color="#283618",
                            corner_radius=5)
weight_entry.grid(row=4, column=0, padx=20, pady=5)

# Calculate button
calc_button = ctk.CTkButton(app,
                            command=calculate_bmi,
                            text="Calculate BMI",
                            text_color="Black",
                            font=font4,
                            fg_color="#fefae0",
                            width=50,
                            bg_color="#fefae0",
                            cursor="hand2")
calc_button.grid(row=5, column=0, padx=50, pady=10)

result_label = ctk.CTkLabel(app, text="",
                            font=font3,
                            text_color="#bc6c25",
                            bg_color="#283618")
result_label.grid(row=6, column=0, padx=5, pady=10)

# Running the app
app.mainloop()
