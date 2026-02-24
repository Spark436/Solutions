import tkinter as tk
from tkinter import ttk
import plusbus_data as pbd
import plusbus_sql as pbsql

# Add buttons that can update, delete and create customers
# Add functions which will be called by the buttons

padx = 8  # Horizontal distance to neighboring objects
pady = 4  # Vertical distance to neighboring objects
rowheight = 24  # rowheight in treeview
treeview_background = "#eeeeee"  # color of background in treeview
treeview_foreground = "black"  # color of foreground in treeview
treeview_selected = "#206030"  # color of selected row in treeview
oddrow = "#dddddd"  # color of odd row in treeview
evenrow = "#cccccc"

def read_customer_entries():  # Read content of entry boxes
    return entry_customer_id.get(), entry_customer_last_name.get(), entry_customer_contact_info.get(),


def clear_customer_entries():  # Clear entry boxes
    entry_customer_id.delete(0, tk.END)  # Delete text in entry box, beginning with the first character (0) and ending with the last character (tk.END)
    entry_customer_last_name.delete(0, tk.END)
    entry_customer_contact_info.delete(0, tk.END)

def write_customer_entries(values):  # Fill entry boxes
        entry_customer_id.insert(0, values[0])
        entry_customer_last_name.insert(0, values[1])
        entry_customer_contact_info.insert(0, values[2])


def edit_customer(_, tree):  # Copy selected tuple into entry boxes. First parameter is mandatory but we don't use it.
        index_selected = tree.focus()  # Index of selected tuple
        values = tree.item(index_selected, 'values')  # Values of selected tuple
        clear_customer_entries()  # Clear entry boxes
        write_customer_entries(values)  # Fill entry boxes

def create_customer(tree, record):  # add new tuple to database
    customer = pbd.customer.convert_from_tuple(record)  # Convert tuple to customer
    pbsql.create_record(customer)  # Update database
    clear_customer_entries()  # Clear entry boxes
    refresh_treeview(tree, dcd.customer)  # Refresh treeview table

def read_table(tree, class_):  # fill tree from database
    count = 0  # Used to keep track of odd and even rows, because these will be colored differently.
    result = pbsql.select_all(class_)  # Read all customers from database
    for record in result:
        if record.valid():  # this condition excludes soft deleted records from being shown in the data table
            if count % 2 == 0:  # even
                tree.insert(parent='', index='end', iid=str(count), text='', values=record.convert_to_tuple(), tags=('evenrow',))  # Insert one row into the data table
            else:  # odd
                tree.insert(parent='', index='end', iid=str(count), text='', values=record.convert_to_tuple(), tags=('oddrow',))  # Insert one row into the data table
            count += 1

def refresh_treeview(tree, class_):  # Refresh treeview table
    empty_treeview(tree)  # Clear treeview table
    read_table(tree, class_)  # Fill treeview from database

def empty_treeview(tree):  # Clear treeview table
    tree.delete(*tree.get_children())

# region common widgets
main_window = tk.Tk()  # Define the main window
main_window.title('AspIT S2: DanskCargo')  # Text shown in the top window bar
main_window.geometry("1200x500")  # window size

style = ttk.Style()  # Add style
style.theme_use('default')  # Pick theme

# region customer widgets
# Define Labelframe which contains all customer related GUI objects (data table, labels, buttons, ...)
frame_customer = tk.LabelFrame(main_window, text="Customer")  # https://www.tutorialspoint.com/python/tk_labelframe.htm
frame_customer.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)  # https://www.tutorialspoint.com/python/tk_grid.htm

# Define data table (Treeview) and its scrollbar. Put them in a Frame.
tree_frame_customer = tk.Frame(frame_customer)  # https://www.tutorialspoint.com/python/tk_frame.htm
tree_frame_customer.grid(row=0, column=0, padx=padx, pady=pady)
tree_scroll_customer = tk.Scrollbar(tree_frame_customer)
tree_scroll_customer.grid(row=0, column=1, padx=0, pady=pady, sticky='ns')
tree_customer = ttk.Treeview(tree_frame_customer, yscrollcommand=tree_scroll_customer.set, selectmode="browse")  # https://docs.python.org/3/library/tkinter.ttk.html#treeview
tree_customer.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_customer.config(command=tree_customer.yview)

# Define the data table's formatting and content
tree_customer['columns'] = ("Id", "Last name", "Contact info")  # Define columns
tree_customer.column("#0", width=0, stretch=tk.NO)  # Format columns. Suppress the irritating first empty column.
tree_customer.column("Id", anchor=tk.E, width=40)  # "E" stands for East, meaning Right. Possible anchors are N, NE, E, SE, S, SW, W, NW and CENTER
tree_customer.column("Last name", anchor=tk.E, width=80)
tree_customer.column("Contact info", anchor=tk.W, width=200)
tree_customer.heading("#0", text="", anchor=tk.W)  # Create column headings
tree_customer.heading("Id", text="Id", anchor=tk.CENTER)
tree_customer.heading("Last name", text="Last name", anchor=tk.CENTER)
tree_customer.heading("Contact info", text="Contact info", anchor=tk.CENTER)
tree_customer.tag_configure('oddrow', background=oddrow)  # Create tags for rows in 2 different colors
tree_customer.tag_configure('evenrow', background=evenrow)

# Define Frame which contains labels, entries and buttons
controls_frame_customer = tk.Frame(frame_customer)
controls_frame_customer.grid(row=3, column=0, padx=padx, pady=pady)


# Define Frame which contains labels (text fields) and entries (input fields)
edit_frame_customer = tk.Frame(controls_frame_customer)  # Add tuple entry boxes
edit_frame_customer.grid(row=0, column=0, padx=padx, pady=pady)
# label and entry for customer id
label_customer_id = tk.Label(edit_frame_customer, text="Id")  # https://www.tutorialspoint.com/python/tk_label.htm
label_customer_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_customer_id = tk.Entry(edit_frame_customer, width=4, justify="right")  # https://www.tutorialspoint.com/python/tk_entry.htm
entry_customer_id.grid(row=1, column=0, padx=padx, pady=pady)
# label and entry for customer last_name
label_customer_last_name = tk.Label(edit_frame_customer, text="Last name")
label_customer_last_name.grid(row=0, column=1, padx=padx, pady=pady)
entry_customer_last_name = tk.Entry(edit_frame_customer, width=8, justify="right")
entry_customer_last_name.grid(row=1, column=1, padx=padx, pady=pady)
# label and entry for customer contact_info
label_customer_contact_info = tk.Label(edit_frame_customer, text="Contact info")
label_customer_contact_info.grid(row=0, column=2, padx=padx, pady=pady)
entry_customer_contact_info = tk.Entry(edit_frame_customer, width=20)
entry_customer_contact_info.grid(row=1, column=2, padx=padx, pady=pady)


# Define Frame which contains buttons
button_frame_customer = tk.Frame(controls_frame_customer)
button_frame_customer.grid(row=1, column=0, padx=padx, pady=pady)
# Define buttons
button_create_customer = tk.Button(button_frame_customer, text="Create", command=lambda: create_customer(tree_customer, read_customer_entries()))
button_create_customer.grid(row=0, column=1, padx=padx, pady=pady)
button_update_customer = tk.Button(button_frame_customer, text="Update", command=lambda: update_customer(tree_customer, read_customer_entries()))
button_update_customer.grid(row=0, column=2, padx=padx, pady=pady)
button_delete_customer = tk.Button(button_frame_customer, text="Delete", command=lambda: delete_customer(tree_customer, read_customer_entries()))
button_delete_customer.grid(row=0, column=3, padx=padx, pady=pady)
button_clear_boxes = tk.Button(button_frame_customer, text="Clear Entry Boxes", command=clear_customer_entries)
button_clear_boxes.grid(row=0, column=4, padx=padx, pady=pady)
# endregion customer widgets

# region main program
if __name__ == "__main__":  # Executed when invoked directly. We use this so main_window.mainloop() does not keep our unit tests from running.
    refresh_treeview(tree_customer, pbd.Customer)  # Load data from database
    main_window.mainloop()  # Wait for button clicks and act upon them
# endregion main program