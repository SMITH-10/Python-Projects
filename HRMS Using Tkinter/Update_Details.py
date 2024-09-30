import tkinter as tk
from tkinter import ttk
import mysql.connector as sc

def update_emp_details():
    empid = empid_entry.get()
    name = name_entry.get()
    dob = dob_entry.get()
    address = address_entry.get()
    mobile_no = mobile_no_entry.get()

    if not empid or not name or not dob or not address or not mobile_no:
        result_label.config(text="Please fill in all fields.")
        return

    conn = sc.connect(host="localhost", user="root", password="root", database="nerd")
    mycursor = conn.cursor()

    query = "UPDATE emp_info SET name = %s, dob = %s, address = %s, mobile_no = %s WHERE empid = %s"
    values = (name, dob, address, mobile_no, empid)

    try:
        mycursor.execute(query, values)
        conn.commit()
        result_label.config(text="Successfully updated employee details!")
    except sc.Error as err:
        result_label.config(text=f"Error: {err}")
    finally:
        conn.close()

def update_hr_details():
    empid = empid_hr_entry.get()
    name = name_hr_entry.get()
    department = department_entry.get()
    designation = designation_entry.get()
    salary = salary_entry.get()
    emailid = emailid_entry.get()

    if not empid or not name or not department or not designation or not salary or not emailid:
        result_hr_label.config(text="Please fill in all fields.")
        return

    conn = sc.connect(host="localhost", user="root", password="root", database="nerd")
    mycursor = conn.cursor()

    query = "UPDATE HR SET name = %s, department = %s, designation = %s, salary = %s, emailid = %s WHERE empid = %s"
    values = (name, department, designation, salary, emailid, empid)

    try:
        mycursor.execute(query, values)
        conn.commit()
        result_hr_label.config(text="Successfully updated HR details!")
    except sc.Error as err:
        result_hr_label.config(text=f"Error: {err}")
    finally:
        conn.close()

# Create the main application window
root = tk.Tk()
root.title("Update Employee Details")

# Calculate the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size and position to be centered on the screen
window_width = 1400
window_height = 600
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

frame_emp = ttk.LabelFrame(root, text="Update Employee Info", padding=(20, 10))
frame_emp.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

frame_hr = ttk.LabelFrame(root, text="Update HR Info", padding=(20, 10))
frame_hr.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")  # Changed column to 1

# Entry fields for employee details
font_size = 16  # Set the font size

empid_label = ttk.Label(frame_emp, text="Employee ID")
empid_label.grid(row=0, column=0, padx=10, pady=10)
empid_entry = ttk.Entry(frame_emp, width=40, font=("Arial", font_size))
empid_entry.grid(row=0, column=1, padx=10, pady=10)

name_label = ttk.Label(frame_emp, text="Name")
name_label.grid(row=1, column=0, padx=10, pady=10)
name_entry = ttk.Entry(frame_emp, width=40, font=("Arial", font_size))
name_entry.grid(row=1, column=1, padx=10, pady=10)

dob_label = ttk.Label(frame_emp, text="DOB")
dob_label.grid(row=2, column=0, padx=10, pady=10)
dob_entry = ttk.Entry(frame_emp, width=40, font=("Arial", font_size))
dob_entry.grid(row=2, column=1, padx=10, pady=10)

address_label = ttk.Label(frame_emp, text="Address")
address_label.grid(row=3, column=0, padx=10, pady=10)
address_entry = ttk.Entry(frame_emp, width=40, font=("Arial", font_size))
address_entry.grid(row=3, column=1, padx=10, pady=10)

mobile_no_label = ttk.Label(frame_emp, text="Mobile No")
mobile_no_label.grid(row=4, column=0, padx=10, pady=10)
mobile_no_entry = ttk.Entry(frame_emp, width=40, font=("Arial", font_size))
mobile_no_entry.grid(row=4, column=1, padx=10, pady=10)

update_emp_button = ttk.Button(frame_emp, text="Update Employee Details", command=update_emp_details)
update_emp_button.grid(row=5, column=0, columnspan=2, padx=20, pady=20)

result_label = ttk.Label(frame_emp, text="", foreground="green", font=("Arial", font_size))
result_label.grid(row=6, column=0, columnspan=2)

# Entry fields for HR details
empid_hr_label = ttk.Label(frame_hr, text="Employee ID")
empid_hr_label.grid(row=0, column=0, padx=10, pady=10)
empid_hr_entry = ttk.Entry(frame_hr, width=40, font=("Arial", font_size))
empid_hr_entry.grid(row=0, column=1, padx=10, pady=10)

name_hr_label = ttk.Label(frame_hr, text="Name")
name_hr_label.grid(row=1, column=0, padx=10, pady=10)
name_hr_entry = ttk.Entry(frame_hr, width=40, font=("Arial", font_size))
name_hr_entry.grid(row=1, column=1, padx=10, pady=10)

designation_label = ttk.Label(frame_hr, text="Designation")
designation_label.grid(row=2, column=0, padx=10, pady=10)
designation_entry = ttk.Entry(frame_hr, width=40, font=("Arial", font_size))
designation_entry.grid(row=2, column=1, padx=10, pady=10)

department_label = ttk.Label(frame_hr, text="Department")
department_label.grid(row=3, column=0, padx=10, pady=10)
department_entry = ttk.Entry(frame_hr, width=40, font=("Arial", font_size))
department_entry.grid(row=3, column=1, padx=10, pady=10)

salary_label = ttk.Label(frame_hr, text="Salary")
salary_label.grid(row=4, column=0, padx=10, pady=10)
salary_entry = ttk.Entry(frame_hr, width=40, font=("Arial", font_size))
salary_entry.grid(row=4, column=1, padx=10, pady=10)

emailid_label = ttk.Label(frame_hr, text="Email ID")
emailid_label.grid(row=5, column=0, padx=10, pady=10)
emailid_entry = ttk.Entry(frame_hr, width=40, font=("Arial", font_size))
emailid_entry.grid(row=5, column=1, padx=10, pady=10)

update_hr_button = ttk.Button(frame_hr, text="Update HR Details", command=update_hr_details)
update_hr_button.grid(row=6, column=0, columnspan=2, padx=20, pady=20)

result_hr_label = ttk.Label(frame_hr, text="", foreground="green", font=("Arial", font_size))
result_hr_label.grid(row=7, column=0, columnspan=2)

root.mainloop()
