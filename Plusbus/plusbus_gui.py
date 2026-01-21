import tkinter as tk
from tkinter import ttk
import plusbus_data

padx = 8  # Horizontal distance to neighboring objects
pady = 4  # Vertical distance to neighboring objects
rowheight = 24  # rowheight in treeview
treeview_background = "#eeeeee"  # color of background in treeview
treeview_foreground = "black"  # color of foreground in treeview
treeview_selected = "#206030"  # color of selected row in treeview
oddrow = "#dddddd"  # color of odd row in treeview
evenrow = "#cccccc"

def read_customer_entries():  # Read content of entry boxes
    return entry_customer_id.get(), entry_customer_weight.get(), entry_customer_destination.get(),


def clear_customer_entries():  # Clear entry boxes
    entry_customer_id.delete(0, tk.END)  # Delete text in entry box, beginning with the first character (0) and ending with the last character (tk.END)
    entry_customer_weight.delete(0, tk.END)
    entry_customer_destination.delete(0, tk.END)
    entry_customer_weather.delete(0, tk.END)
