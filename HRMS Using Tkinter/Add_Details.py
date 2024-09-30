import tkinter as tk
from tkinter import ttk
import mysql.connector as sc

def add_employee():
    empid = empid_entry.get()
    name = name_entry.get()
    designation = designation_entry.get()
    department = department_entry.get()
    salary = salary_entry.get()
    emailid = emailid_entry.get()
    dob = dob_entry.get()
    address = address_entry.get()
    mobile_no = mobile_no_entry.get()

    # Check if any of the required fields are empty
    if not (empid and name and designation and department and salary and emailid and dob and address and mobile_no):
        # If any field is empty, display a warning and return
        warning_label.config(text="Please fill in all fields.")
        return
    else:
        warning_label.config(text="")

    # Add data to the 'hr' table
    hr_query = f"INSERT INTO hr (EMPID, NAME, DEPARTMENT, DESIGNATION, SALARY, EMAILID) VALUES ('{empid}', '{name}', '{department}', '{designation}', '{salary}', '{emailid}')"
    # Add data to the 'emp_info' table
    emp_info_query = f"INSERT INTO emp_info (EMPID, NAME, DOB, ADDRESS, MOBILE_NO) VALUES ('{empid}', '{name}', '{dob}', '{address}', '{mobile_no}')"

    conn = sc.connect(host="localhost", user="root", password="root", database="nerd")
    cursor = conn.cursor()

    cursor.execute(hr_query)
    cursor.execute(emp_info_query)

    conn.commit()
    conn.close()

    # Clear the entry fields after adding
    empid_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    department_entry.delete(0, tk.END)
    designation_entry.delete(0, tk.END)
    salary_entry.delete(0, tk.END)
    emailid_entry.delete(0, tk.END)
    dob_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    mobile_no_entry.delete(0, tk.END)

# Create the main application window
root = tk.Tk()
root.title("Add Employee")

# Calculate the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size and position to be centered on the screen
window_width = 700
window_height = 500
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

frame = ttk.LabelFrame(root, text="Employee Details", padding=(20, 10))
frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

# Entry fields for employee details
empid_label = ttk.Label(frame, text="Employee ID:", font=("Arial", 19))
empid_label.grid(row=0, column=0)
empid_entry = ttk.Entry(frame, width=40)
empid_entry.grid(row=0, column=1)

name_label = ttk.Label(frame, text="Name:", font=("Arial", 19))
name_label.grid(row=1, column=0)
name_entry = ttk.Entry(frame, width=40)
name_entry.grid(row=1, column=1)

designation_label = ttk.Label(frame, text="Designation:", font=("Arial", 19))
designation_label.grid(row=2, column=0)
designation_entry = ttk.Entry(frame, width=40)
designation_entry.grid(row=2, column=1)

department_label = ttk.Label(frame, text="Department", font=("Arial", 19))
department_label.grid(row=3, column=0)
department_entry = ttk.Entry(frame, width=40)
department_entry.grid(row=3, column=1)

salary_label = ttk.Label(frame, text="Salary:", font=("Arial", 19))
salary_label.grid(row=4, column=0)
salary_entry = ttk.Entry(frame, width=40)
salary_entry.grid(row=4, column=1)

emailid_label = ttk.Label(frame, text="Email ID:", font=("Arial", 19))
emailid_label.grid(row=5, column=0)
emailid_entry = ttk.Entry(frame, width=40)
emailid_entry.grid(row=5, column=1)

dob_label = ttk.Label(frame, text="DOB:", font=("Arial", 19))
dob_label.grid(row=6, column=0)
dob_entry = ttk.Entry(frame, width=40)
dob_entry.grid(row=6, column=1)

address_label = ttk.Label(frame, text="Address:", font=("Arial", 19))
address_label.grid(row=7, column=0)
address_entry = ttk.Entry(frame, width=40)
address_entry.grid(row=7, column=1)

mobile_no_label = ttk.Label(frame, text="Mobile No:", font=("Arial", 19))
mobile_no_label.grid(row=8, column=0)
mobile_no_entry = ttk.Entry(frame, width=40)
mobile_no_entry.grid(row=8, column=1)

# Create a label for displaying warnings
warning_label = ttk.Label(root, text="", foreground="red")
warning_label.grid(row=9, column=0, columnspan=2, pady=10)

style = ttk.Style()
style.configure("TButton", font=("Arial Black", 14))

b3 = ttk.Button(root, text="ADD EMPLOYEE", style="TButton", command=add_employee)
b3.grid(row=10, column=0, columnspan=2, padx=20, pady=20)

root.mainloop()