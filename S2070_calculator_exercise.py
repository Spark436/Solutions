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

def empty_entry():
    entry_1.delete(0, tk.END)

def one():
    entry_1.insert(0, "1")

padx = 5
pady = 5
font = tkfont.Font(family="Helvetica", size=30, weight="bold")

labelframe = tk.LabelFrame(main_window)
labelframe.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

frame_1 = tk.Frame(labelframe)
frame_1.grid(row=1)

frame_2 = tk.Frame(labelframe)
frame_2.grid(row=2)

# Add an entry where the math questions should go and have it be at the top of the entry above the buttons.
entry_1 = tk.Entry(frame_1, width=21, font=font)
entry_1.grid(row=1, column=1, padx=padx, pady=pady)


# add one functional button then copy that to 13 other buttons. The buttons should have labels as 0-9, +, -, *, /.
# Set the buttons in rows of four with 3 numbers and one math symbol at the end and have the last row be 0 and =, 0 being centered and = being pushed to the right.
# Add a button that clears the entry labeled C
button_1 = tk.Button(frame_2, text="1", width=3, font=font, command=one)
button_1.grid(row=2, column=1, padx=padx, pady=pady)
button_c = tk.Button(frame_2, text="C", width=3, font=font, command=empty_entry)
button_c.grid(row=2,column=2, padx=padx, pady=pady)
if __name__ == "__main__":
    main_window.mainloop()