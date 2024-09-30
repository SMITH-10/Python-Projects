import tkinter as tk
import mysql.connector as sc

def remove_employee_info():
    empid = empid_entry.get()

    # Remove from the emp_info table
    conn = sc.connect(host="localhost", user="root", password="root", database="nerd")
    mycursor = conn.cursor()
    query = "DELETE FROM emp_info WHERE empid = %s"
    mycursor.execute(query, (empid,))
    conn.commit()
    conn.close()
    result_label.config(text="Successfully removed employee details from emp_info")

def remove_hr_info():
    empid = empid_entry.get()

    # Remove from the hr table
    conn = sc.connect(host="localhost", user="root", password="root", database="nerd")
    mycursor = conn.cursor()
    query = "DELETE FROM hr WHERE empid = %s"
    query = "DELETE FROM emp_his WHERE empid = %s"
    mycursor.execute(query, (empid,))
    conn.commit()
    conn.close()
    result_label.config(text="Successfully removed employee details from hr")
    



# Create the main window
root = tk.Tk()
root.title("Remove Employee Details")

# Create and configure labels, entry fields, and buttons
empid_label = tk.Label(root, text="Enter Employee ID:")
empid_label.grid(row=0, column=0, padx=10, pady=10)
empid_entry = tk.Entry(root)
empid_entry.grid(row=0, column=1, padx=10, pady=10)
remove_emp_info_button = tk.Button(root, text="Remove from emp_info", command=remove_employee_info)
remove_emp_info_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
remove_hr_info_button = tk.Button(root, text="Remove from hr", command=remove_hr_info)
remove_hr_info_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the Tkinter main loop
root.mainloop()
