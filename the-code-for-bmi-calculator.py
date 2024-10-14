import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *

#this function has the processing of the bmi
def calculate_bmi():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        age = int(age_entry.get())

        height_meters = height / 100

        bmi = weight / (height_meters ** 2)

        normal_range = (18.5, 24.9)

        if normal_range[0] <= bmi <= normal_range[1]:
            health_status = "you are healthy :)"
        elif bmi <= 18.4:
            health_status = "you are underweight"
        elif bmi  <= 29.9:
            health_status = "you are overweight"
        elif bmi <= 34.9:
            health_status = "FATASSSSS"

        
        result_label.config(text=f"Your BMI is: {bmi:.2f}\n{health_status}")

#error message 
    except ValueError:
        messagebox.showerror("ERROR!", "Please enter valid numeric values for height, weight and age.")

#designing the widget
window = tk.Tk()
window.title("BMI calcultor")

window.geometry("400x300")
window.resizable(False, False)
window.configure(bg="#def5ff")


font_style = ("Poppins", 12)

entry_style = ttk.Style()
entry_style.configure("TEntry",
                      fieldbackground = "white",
                      bordercolour = "#bad5ff",
                      borderwidth = 5,
                      relief = "flat",
                      font = font_style)

#making the indivisual text lables to show on the widget to get the values (label le harek row/column design garney kaam garcha)
title_label = tk.Label(window, text = "BMI CALCULATOR", font = ("Poppins", 16, "bold"), bg = "#def5ff")
title_label.grid(row = 0, column = 0, columnspan = 2, pady = 10)

#entry le imput lekhney box design garcha
age_label = tk.Label(window, text = "enter age:", font = font_style, bg = "#def5ff")
age_label.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = "e")
age_entry = ttk.Entry(window, font = font_style)
age_entry.grid(row = 1, column = 1, padx = 10, pady = 5)

height_label = tk.Label(window, text = f'''enter height (in "cm"):''', font = font_style, bg = "#def5ff")
height_label.grid(row = 2, column = 0, padx = 10, pady = 5, sticky = "e")
height_entry = ttk.Entry(window, font = font_style)
height_entry.grid(row = 2, column = 1, padx = 10, pady = 5)

weight_label = tk.Label(window, text = f'''enter weight (in "kg"):''', font = font_style, bg = "#def5ff")
weight_label.grid(row = 3, column = 0, padx = 10, pady = 5, sticky = "e")
weight_entry = ttk.Entry(window, font = font_style)
weight_entry.grid(row = 3, column = 1, padx = 10, pady = 5)


#button le well button design garcha
calculate_button = ttk.Button(window, text = "Calculate BMI", command = calculate_bmi, style = "TButton", cursor = "hand2")
calculate_button.grid(row = 5, column = 1, padx = 10, pady =5, sticky = "e")

result_label = tk.Label(window, text = "", font = font_style, bg = "#def5ff")
result_label.grid(row = 6, column = 0, columnspan = 2)

window.mainloop()




