"""Opgave "Calculator with GUI"

Løs opgave S2070_calculator_exercise.py med en GUI

Kopier denne fil til din egen løsningsmappe. Skriv din løsning i kopien.

Hvis du går i stå, spørg Google, andre elever, en AI eller læreren.

Når dit program er færdigt, skub det til dit GitHub-repository.
"""

import tkinter as tk
import tkinter.font as tkfont

main_window = tk.Tk()
main_window.title("Calculator")
main_window.geometry("500x500")

def empty_entry(): #this lets the C button clear the entry field
    entry_1.delete(0, tk.END)

def calculate(): # this makes the calculator calculate the equation
    result =  str(eval(entry_1.get()))
    entry_1.delete(0, tk.END)
    entry_1.insert(100, result)

def insert_number(number): # this makes the number buttons insert text when pressed
    entry_1.insert(100, str(number))

def addition():
    entry_1.insert(100, "+")

def subtraction():
    entry_1.insert(100, "-")

def multiplication():
    entry_1.insert(100, "*")

def division():
    entry_1.insert(100, "/")

def equal():
    entry_1.insert(100, "=")

padx = 5
pady = 5
font = tkfont.Font(family="Helvetica", size=30, weight="bold")

labelframe = tk.LabelFrame(main_window) #this contains the frames
labelframe.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

frame_1 = tk.Frame(labelframe) #this contains the text field
frame_1.grid(row=1)

frame_2 = tk.Frame(labelframe) #this contains the buttons
frame_2.grid(row=2)

# Add an entry where the math questions should go and have it be at the top of the entry above the buttons.
entry_1 = tk.Entry(frame_1, justify="right", width=21, font=font) # the text field where numbers can be inserted
entry_1.grid(row=1, column=1, padx=padx, pady=pady)


# add one functional button then copy that to 13 other buttons. The buttons should have labels as 0-9, +, -, *, /.
# Set the buttons in rows of four with 3 numbers and one math symbol at the end and have the last row be 0 and =, 0 being centered and = being pushed to the right.
# Add a button that clears the entry labeled C
number_buttons = []
for number in range(10): # this creates buttons 0 to 9 without having to make seperate buttons manually for each number
    button = tk.Button(frame_2, text=str(number), width=3, font=font, command=lambda n=number: insert_number(n))
    button.grid(row=number//3+2, column=number%3, padx=padx, pady=pady)
    number_buttons.append(button)

button_c = tk.Button(frame_2, text="C", width=3, font=font, command=empty_entry)
button_c.grid(row=2,column=3, padx=padx, pady=pady)

button_addition = tk.Button(frame_2, text="+", width=3, font=font, command=addition)
button_addition.grid(row=5, column=3, padx=padx, pady=pady)

button_subtract = tk.Button(frame_2, text="-", width=3, font=font, command=subtraction)
button_subtract.grid(row=4, column=3, padx=padx, pady=pady)

button_multiply = tk.Button(frame_2, text="*", width=3, font=font, command=multiplication)
button_multiply.grid(row=5, column=1, padx=padx, pady=pady)

button_divide = tk.Button(frame_2, text="/", width=3, font=font, command=division)
button_divide.grid(row=5, column=2, padx=padx, pady=pady)

button_equal = tk.Button(frame_2, text="=", width=3, font=font, command=calculate)
button_equal.grid(row=3, column=3, padx=padx, pady=pady)

if __name__ == "__main__":
    main_window.mainloop()



# button_1 = tk.Button(frame_2, text="1", width=3, font=font, command=one)
# button_1.grid(row=2, column=1, padx=padx, pady=pady)
