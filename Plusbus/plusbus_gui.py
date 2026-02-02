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

    # region common functions
    def refresh_treeview(tree, class_):  # Refresh treeview table
        empty_treeview(tree)  # Clear treeview table
        read_table(tree, class_)  # Fill treeview from database

# region common widgets
main_window = tk.Tk()  # Define the main window
main_window.title('Plusbus')  # Text shown in the top window bar
main_window.geometry("500x500")  # window size

style = ttk.Style()  # Add style
style.theme_use('default')  # Pick theme

# region container widgets
# Define Labelframe which contains all container related GUI objects (data table, labels, buttons, ...)
frame_container = tk.LabelFrame(main_window, text="Container")  # https://www.tutorialspoint.com/python/tk_labelframe.htm
frame_container.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)  # https://www.tutorialspoint.com/python/tk_grid.htm

# Define data table (Treeview) and its scrollbar. Put them in a Frame.
tree_frame_container = tk.Frame(frame_container)  # https://www.tutorialspoint.com/python/tk_frame.htm
tree_frame_container.grid(row=0, column=0, padx=padx, pady=pady)
tree_scroll_container = tk.Scrollbar(tree_frame_container)
tree_scroll_container.grid(row=0, column=1, padx=0, pady=pady, sticky='ns')
tree_container = ttk.Treeview(tree_frame_container, yscrollcommand=tree_scroll_container.set, selectmode="browse")  # https://docs.python.org/3/library/tkinter.ttk.html#treeview
tree_container.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_container.config(command=tree_container.yview)

# Define the data table's formatting and content
tree_container['columns'] = ("id", "last name", "contact")  # Define columns
tree_container.column("#0", width=0, stretch=tk.NO)  # Format columns. Suppress the irritating first empty column.
tree_container.column("id", anchor=tk.E, width=40)  # "E" stands for East, meaning Right. Possible anchors are N, NE, E, SE, S, SW, W, NW and CENTER
tree_container.column("last name", anchor=tk.E, width=80)
tree_container.column("contact", anchor=tk.W, width=200)

if __name__ == "__main__":  # Executed when invoked directly. We use this so main_window.mainloop() does not keep our unit tests from running.
    refresh_treeview(tree_container, dcd.Container)  # Load data from database
    main_window.mainloop()  # Wait for button clicks and act upon them
