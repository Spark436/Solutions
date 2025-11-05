""" Opgave "GUI step 2":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

--------

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2020.png

Genbrug din kode fra "GUI step 1".

GUI-strukturen bør være som følger:
    main window
        labelframe
            frame
                labels and entries
            frame
                buttons

Funktionalitet:
    Klik på knappen "clear entry boxes" sletter teksten i alle indtastningsfelter (entries).

--------

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""

import tkinter as tk

def empty_entry():
    entry_1.delete(0, tk.END)
    entry_2.delete(0, tk.END)
    entry_3.delete(0, tk.END)
    entry_4.delete(0, tk.END)

padx = 10
pady = 7

main_window = tk.Tk()
main_window.title('My first GUI')
main_window.geometry("475x200")

labelframe = tk.LabelFrame(main_window, text="Container")
labelframe.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

frame_1 = tk.Frame(labelframe)
frame_1.grid()

frame_2 = tk.Frame(labelframe)
frame_2.grid()

label_1 = tk.Label(frame_1, text="Id")
label_1.grid(row=1, column=1, padx=padx, pady=pady)

label_2 = tk.Label(frame_1, text="Weight")
label_2.grid(row=1, column=2, padx=padx, pady=pady)

label_3 = tk.Label(frame_1, text="Destination")
label_3.grid(row=1, column=3, padx=padx, pady=pady)

label_4 = tk.Label(frame_1, text="Weather")
label_4.grid(row=1, column=4, padx=padx, pady=pady)

entry_1 = tk.Entry(frame_1, width=4)
entry_1.grid(row=2, column=1, padx=padx, pady=pady,)

entry_2 = tk.Entry(frame_1, width=8)
entry_2.grid(row=2, column=2, padx=padx, pady=pady)

entry_3 = tk.Entry(frame_1, width=18)
entry_3.grid(row=2, column=3, padx=padx, pady=pady)

entry_4 = tk.Entry(frame_1, width=14)
entry_4.grid(row=2, column=4, padx=padx, pady=pady)

button_1 = tk.Button(frame_2, text="Create")
button_1.grid(row=1, column=1, padx=padx, pady=pady)

button_2 = tk.Button(frame_2, text="Update")
button_2.grid(row=1, column=2, padx=padx, pady=pady)

button_3 = tk.Button(frame_2, text="Delete")
button_3.grid(row=1, column=3, padx=padx, pady=pady)

button_4 = tk.Button(frame_2, text="Clear entry boxes", command=empty_entry)
button_4.grid(row=1, column=4, padx=padx, pady=pady)

if __name__ == "__main__":
    main_window.mainloop()