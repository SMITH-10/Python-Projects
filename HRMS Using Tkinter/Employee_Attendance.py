import tkinter as tk
from tkinter import ttk
import mysql.connector
import calendar
from datetime import date

# Function to fetch attendance data for a specific employee
def get_employee_attendance_data(employee_id, year, month):
    query = f"SELECT DATE, PRESENT, ABSENT FROM emp_data WHERE EMPID = '{employee_id}' " \
            f"AND YEAR(DATE) = {year} AND MONTH(DATE) = {month}"
    cursor.execute(query)
    return cursor.fetchall()

# Function to handle date selection
def select_date(day):
    global selected_date
    selected_date = (current_year, current_month, day)
    date_label.config(text=f"Selected Date: {selected_date}")

    # Add a box around the selected date and remove it from previously selected dates
    for date, label in calendar_labels.items():
        if date == day:
            label.configure(borderwidth=2, relief="solid")
        else:
            label.configure(borderwidth=1, relief="flat")

# Function to mark attendance for the selected date
def mark_attendance(is_present):
    if selected_date and entry_employee_id.get().strip():
        year, month, day = selected_date
        present_state = "Yes" if is_present else "No"
        absent_state = "Yes" if not is_present else "No"

        query = "INSERT INTO emp_data (EMPID, DATE, PRESENT, ABSENT) " \
                "VALUES (%s, %s, %s, %s) " \
                "ON DUPLICATE KEY UPDATE PRESENT = %s, ABSENT = %s"
        data = (entry_employee_id.get(), date(year, month, day), present_state, absent_state, present_state, absent_state)
        cursor.execute(query, data)
        conn.commit()

        day = day
        if day in calendar_labels:
            day_label = calendar_labels[day]
            day_label.configure(text=day)
            if present_state == "Yes":
                day_label.configure(style="Present.TLabel")
            else:
                day_label.configure(style="Absent.TLabel",background='red')

        display_employee_attendance()
    else:
        error_label.config(text="Employee ID is required")

# Function to display employee attendance
def display_employee_attendance():
    employee_id = entry_employee_id.get().strip()

    if not employee_id:
        error_label.config(text="Employee ID is required")
        return

    error_label.config(text="")

    attendance_data = get_employee_attendance_data(employee_id, current_year, current_month)

    for date, present, absent in attendance_data:
        day = date.day
        if day in calendar_labels:
            day_label = calendar_labels[day]
            day_label.configure(text=day)
            if present == "Yes":
                day_label.configure(style="Present.TLabel")
            elif absent == "Yes":
                day_label.configure(style="Absent.TLabel")

# Function to navigate to the previous month
def previous_month():
    global current_year, current_month
    if current_month == 1:
        current_month = 12
        current_year -= 1
    else:
        current_month -= 1
    month_label.config(text=f"{calendar.month_name[current_month]} {current_year}")
    display_employee_attendance()

# Function to navigate to the next month
def next_month():
    global current_year, current_month
    if current_month == 12:
        current_month = 1
        current_year += 1
    else:
        current_month += 1
    month_label.config(text=f"{calendar.month_name[current_month]} {current_year}")
    display_employee_attendance()

# Create a Tkinter window
root = tk.Tk()
root.title("Attendance Calendar")

# Database connection details
db_host = "localhost"
db_user = "root"
db_password = "root"
db_name = "nerd"

# Connect to your MySQL database
conn = mysql.connector.connect(host=db_host, user=db_user, password=db_password, database=db_name)
cursor = conn.cursor()

# Center the window on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - 800) // 2
y = (screen_height - 600) // 2
root.geometry("800x600+{}+{}".format(x, y))

# Create labels for day names
day_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for i, day_name in enumerate(day_names):
    ttk.Label(root, text=day_name).grid(row=0, column=i, sticky="nsew")
    root.grid_columnconfigure(i, weight=1)

# Create custom styles for absent and present labels
root.style = ttk.Style()
root.style.configure("Absent.TLabel")
root.style.configure("Present.TLabel", background="green")

# Create labels for the calendar days
calendar_labels = {}
current_year = 2023
current_month = 11
cal = calendar.monthcalendar(current_year, current_month)
for week_num, week in enumerate(cal, start=1):
    for day_num, day in enumerate(week):
        if day != 0:
            date_label = ttk.Label(root, text=day, style="Absent.TLabel", width=5, anchor="center")
            date_label.grid(row=week_num, column=day_num, sticky="nsew")
            calendar_labels[day] = date_label
            date_label.bind("<Button-1>", lambda event, day=day: select_date(day))

# Configure row and column weights for consistent spacing
for i in range(1, 7):
    root.grid_rowconfigure(i, weight=1)

# Create an input field for Employee ID
label_employee_id = ttk.Label(root, text="Enter Employee ID:")
entry_employee_id = ttk.Entry(root)
button_get_attendance = ttk.Button(root, text="Get Attendance", command=lambda: display_employee_attendance())
error_label = ttk.Label(root, text="", foreground="red")

# Create buttons to mark attendance for the selected date
button_mark_present = ttk.Button(root, text="Mark Present", command=lambda: mark_attendance(True))
button_mark_absent = ttk.Button(root, text="Mark Absent", command=lambda: mark_attendance(False))

# Create buttons to navigate between months
button_previous_month = ttk.Button(root, text="<", command=previous_month)
button_next_month = ttk.Button(root, text=">", command=next_month)
month_label = ttk.Label(root, text=f"{calendar.month_name[current_month]} {current_year}")

# Label to display the selected date
date_label = ttk.Label(root, text="Selected Date: None")

# Place the Employee ID input field, buttons, and date label on the screen
label_employee_id.grid(row=8, column=0)
entry_employee_id.grid(row=8, column=1)
button_get_attendance.grid(row=8, column=2)
error_label.grid(row=9, column=0, columnspan=3)
button_mark_present.grid(row=10, column=0)
button_mark_absent.grid(row=10, column=1)
button_previous_month.grid(row=11, column=0)
month_label.grid(row=11, column=1, columnspan=3)
button_next_month.grid(row=11, column=4)
date_label.grid(row=12, column=0, columnspan=5)

root.mainloop()
