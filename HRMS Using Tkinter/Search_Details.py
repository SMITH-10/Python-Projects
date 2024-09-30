import tkinter as tk
from tkinter import ttk
import mysql.connector as sc

# Define tree globally
tree = None

def search():
    search_criteria = search_var.get()
    search_text = entry.get()

    if search_criteria == "Name":
        sql_query = f"SELECT * FROM HR WHERE name LIKE '%{search_text}%'"
    elif search_criteria == "EMPID":
        sql_query = f"SELECT * FROM HR WHERE EMPID = '{search_text}'"

    cursor.execute(sql_query)
    result = cursor.fetchall()
    
    for i in tree.get_children():
        tree.delete(i)

    for row in result:
        # Append "Click Here" as a button in the last column
        tree.insert("", "end", values=row + ("Click Here",))

def show_more_info(emp_id):
    # Function to display more info
    more_info_query = f"SELECT * FROM emp_info WHERE EMPID = '{emp_id}'"
    cursor.execute(more_info_query)
    more_info = cursor.fetchone()

    # Display more info in a new window
    more_info_window = tk.Toplevel(root)
    more_info_window.title("More Info")
    
    info_label = tk.Label(more_info_window, text="Additional Info:", font=("Helvetica", 14))
    info_label.pack()

    # Create a table for additional info
    info_table = ttk.Treeview(more_info_window, columns=("Attribute", "Value"), show="headings")
    info_table.heading("Attribute", text="Attribute")
    info_table.heading("Value", text="Value")
    info_table.pack()

    info_table.insert("", "end", values=("EMPID:", more_info[0]))
    info_table.insert("", "end", values=("Name:", more_info[1]))
    info_table.insert("", "end", values=("DOB:", more_info[2]))
    info_table.insert("", "end", values=("Address:", more_info[3]))
    info_table.insert("", "end", values=("Mobile No:", more_info[4]))

    # Center the text in the table
    info_table.heading("Attribute", anchor="center")
    info_table.heading("Value", anchor="center")

    # Create the "More Details" button
    more_details_button = tk.Button(more_info_window, text="Previous Company Records", command=lambda: show_more_details(emp_id))
    more_details_button.pack()

def show_more_details(emp_id):
    # Function to display more details from the "emp_his" table
    more_details_query = f"SELECT COMPANY_NAME, DESIGNATION FROM emp_his WHERE EMPID = '{emp_id}'"
    cursor.execute(more_details_query)
    more_details = cursor.fetchall()

    # Display more details in a new window
    more_details_window = tk.Toplevel(root)
    more_details_window.title("More Details")

    details_label = tk.Label(more_details_window, text="Previous Company Records", font=("Helvetica", 14))
    details_label.pack()

    # Create a table for more details
    details_table = ttk.Treeview(more_details_window, columns=("Company Name", "Designation"), show="headings")
    details_table.heading("Company Name", text="Company Name")
    details_table.heading("Designation", text="Designation")
    details_table.pack()

    for detail in more_details:
        company_name, designation = detail
        details_table.insert("", "end", values=(company_name, designation))

    # Center the text in the table
    details_table.heading("Company Name", anchor="center")
    details_table.heading("Designation", anchor="center")

conn = sc.connect(host="localhost", user="root", password="root", database="nerd")
cursor = conn.cursor()

root = tk.Tk()
root.title("Search Database")

# Calculate the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size
window_width = 800
window_height = 400

# Calculate the window's position to be centered on the screen
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

search_var = tk.StringVar()
search_var.set("Name")

entry_label = tk.Label(frame, text="Search:")
entry_label.grid(row=0, column=0)
entry = tk.Entry(frame)
entry.grid(row=0, column=1)

search_label = tk.Label(frame, text="Search by:")
search_label.grid(row=1, column=0)
search_option = ttk.Combobox(frame, textvariable=search_var, values=["Name", "EMPID"])
search_option.grid(row=1, column=1)

search_button = tk.Button(frame, text="Search", command=search)
search_button.grid(row=0, column=2, rowspan=2)

columns = ("EMPID", "Name", "Department","Designation","Salary", "EmailID", "More Info")
tree = ttk.Treeview(frame, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.grid(row=2, column=0, columnspan=3)

def on_tree_select(event):
    # Get the selected row
    selected_item = tree.selection()[0]
    
    # Check if the selected row has "Click Here" in it
    if tree.item(selected_item, "values")[-1] == "Click Here":
        # Extract EMPID from the selected row
        emp_id = tree.item(selected_item, "values")[0]
        show_more_info(emp_id)

tree.bind("<<TreeviewSelect>>", on_tree_select)

root.mainloop()

cursor.close()
conn.close()
