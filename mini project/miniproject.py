import tkinter as tk
from tkinter import ttk
import sqlite3


# Create a main window
root = tk.Tk()
root.title("GUI Template")

# Define a function to clear the entry widgets
def clear_entry():
    name_entry.delete(0, tk.END)
    tel_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Define a function to show data on the listbox
def show_data():
    # Clear the listbox
    for record in listbox.get_children():
        listbox.delete(record)

    # Get the records from the database
    conn = sqlite3.connect(r'C:\Python311\py 101\mini project\project.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM person')
    records = cursor.fetchall()
    conn.close()

    # Add the records to the listbox
    for record in records:
        listbox.insert("", "end", values=(record[1], record[2], record[3]))


        
# Define a function to add a new record
def add_record():
    # Get the values from the entry widgets
    name = name_entry.get()
    tel = tel_entry.get()
    address = address_entry.get()
    
    # Clear the entry widgets
    clear_entry()

    conn = sqlite3.connect(r'C:\Python311\py 101\mini project\project.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO person VALUES (null,?, ?, ?)', (name, tel, address))
    conn.commit()
    conn.close()

# Define a function to edit a record
def edit_record():
    # Get the values from the entry widgets
    name = name_entry.get()
    tel = tel_entry.get()
    address = address_entry.get()
    
    # Get the selected item from the listbox
    selected_item = listbox.focus()

    
    # Clear the entry widgets
    clear_entry()


# Define a function to delete a record
def delete_record():
    # Get the selected item from the listbox
    selected_item = listbox.focus()
    
    # Delete the record from the database
    conn = sqlite3.connect(r'C:\Python311\py 101\mini project\project.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM person WHERE name=? AND tel=? AND address=?', tuple(values))
    conn.commit()
    conn.close()

# Create a notebook with three tabs
notebook = ttk.Notebook(root)
notebook.pack()

# Create a frame for the first tab
frame1 = ttk.Frame(notebook)
notebook.add(frame1, text="แสดงข้อมูล")

# Create a frame for the second tab
frame2 = ttk.Frame(notebook)
notebook.add(frame2, text="เพิ่มข้อมูล")

# Create a frame for the third tab
frame3 = ttk.Frame(notebook)
notebook.add(frame3, text="แก้ไขข้อมูล")

# Create a listbox and add it to the first tab
listbox = ttk.Treeview(frame1, columns=("name", "tel", "address"), show="headings")
listbox.heading("name", text="Name")
listbox.heading("tel", text="Tel")
listbox.heading("address", text="Address")
listbox.pack()

# Create a scrollbar for the listbox
scrollbar = ttk.Scrollbar(frame1, orient="vertical", command=listbox.yview)
listbox.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# Configure the scrollbar to scroll the listbox
listbox.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=listbox.yview)

show_button = ttk.Button(frame1, text="show data", command=show_data)
show_button.pack(padx=5, pady=5)



# Create entry widgets and a button for the second tab
name_label = ttk.Label(frame2, text="Name:")
name_label.grid(column=0, row=0, padx=5, pady=5)

name_entry = ttk.Entry(frame2)
name_entry.grid(column=1, row=0, padx=5, pady=5)

tel_label = ttk.Label(frame2, text="Tel:")
tel_label.grid(column=0, row=1, padx=5, pady=5)

tel_entry = ttk.Entry(frame2)
tel_entry.grid(column=1, row=1, padx=5, pady=5)

address_label = ttk.Label(frame2, text="Address:")
address_label.grid(column=0, row=2, padx=5, pady=5)

address_entry = ttk.Entry(frame2)
address_entry.grid(column=1, row=2, padx=5, pady=5)

insert_button = ttk.Button(frame2, text="Insert", command=add_record)
insert_button.grid(column=1, row=3, padx=5, pady=5)






