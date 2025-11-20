""" Opgave "GUI step 4":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

--------

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2040.png

Genbrug din kode fra "GUI step 3".

Fyld treeview'en med testdata.
Leg med farveværdierne. Find en farvekombination, som du kan lide.

Funktionalitet:
    Klik på knappen "clear entry boxes" sletter teksten i alle indtastningsfelter (entries).
    Hvis du klikker på en datarække i træoversigten, kopieres dataene i denne række til indtastningsfelterne.

--------

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""

import tkinter as tk
from tkinter import ttk

def empty_entry():
    entry_1.delete(0, tk.END)
    entry_2.delete(0, tk.END)
    entry_3.delete(0, tk.END)
    entry_4.delete(0, tk.END)

def read_table(tree):
    for record in test_data_list:
        tree.insert(parent='', index='end', text='', values=record)

def edit_record(event, tree):
    index_selected = tree.focus()
    values = tree.item(index_selected, 'values')
    entry_1.delete(0, tk.END)
    entry_2.delete(1, tk.END)
    entry_3.delete(2, tk.END)
    entry_1.insert(0, values[1])
    entry_2.insert(1, values[2])
    entry_3.insert(2, values[3])

padx = 10
pady = 7
rowheight = 24
treeview_background = "#f0f0f0"
treeview_foreground = "black"
treeview_selected = "#ff00d4"

main_window = tk.Tk()
main_window.title('My first GUI')
main_window.geometry("490x450")

test_data_list = []
test_data_list.append(("1", "1000", "oslo"))
test_data_list.append(("2", "2000", "chicago"))
test_data_list.append(("3", "3000", "milano"))
test_data_list.append(("4", "4000", "amsterdam"))

labelframe = tk.LabelFrame(main_window, text="Container")
labelframe.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

frame_1 = tk.Frame(labelframe)
frame_1.grid(row=1)

frame_2 = tk.Frame(labelframe)
frame_2.grid(row=2)

frame_3 = tk.Frame(labelframe)
frame_3.grid(row=0)

style = ttk.Style()
style.theme_use('default')
style.configure("Treeview", background=treeview_background, foreground=treeview_foreground, rowheight=rowheight, fieldbackground=treeview_background)
style.map('Treeview', background=[('selected', treeview_selected)])

tree_1_scrollbar = tk.Scrollbar(frame_3)
tree_1_scrollbar.grid(row=0, column=1, padx=padx, pady=pady, sticky='ns')
tree_1 = ttk.Treeview(frame_3, yscrollcommand=tree_1_scrollbar.set, selectmode="browse")
tree_1.grid(row=0, column=0, pady=pady)
tree_1_scrollbar.config(command=tree_1.yview)

tree_1['columns'] = ("col1", "col2", "col3")
tree_1.column("#0", width=0, stretch=tk.NO)
tree_1.column("col1", anchor=tk.E, width=90)
tree_1.column("col2", anchor=tk.W, width=130)
tree_1.column("col3", anchor=tk.W, width=180)

tree_1.heading("#0", text="", anchor=tk.W)
tree_1.heading("col1", text="Id", anchor=tk.CENTER)
tree_1.heading("col2", text="Weight", anchor=tk.CENTER)
tree_1.heading("col3", text="Destination", anchor=tk.CENTER)

tree_1.bind("<ButtonRelease-1>", lambda event: edit_record(event, tree_1))

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

read_table(tree_1)

if __name__ == "__main__":
    main_window.mainloop()