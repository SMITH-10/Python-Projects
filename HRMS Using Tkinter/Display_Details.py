import tkinter as tk
from tkinter import ttk
import pandas as pd
import mysql.connector as mysql

def seaemp():
    ch = choice_var.get()
    
    # Database connection parameters
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "root",
        "database": "nerd"
    }

    try:
        conn = mysql.connect(**db_config)
    except mysql.Error as e:
        print("Error connecting to the database:", e)
        return

    cursor = conn.cursor(dictionary=True)

    if ch == 1:
        query = "SELECT * FROM emp_info"
    elif ch == 2:
        query = "SELECT * FROM hr"
    elif ch == 3:
        query = "SELECT * FROM emp_his"

    cursor.execute(query)
    result = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Display the results in a Pandas DataFrame
    df = pd.DataFrame(result)
    result_text.config(state='normal')
    result_text.delete(1.0, 'end')
    result_text.insert('insert', df)
    result_text.config(state='disabled')

app = tk.Tk()
app.title("Employee Info Viewer")

frame = ttk.Frame(app)
frame.grid(column=0, row=0)

choice_label = ttk.Label(frame, text="Choose Information:")
choice_label.grid(column=0, row=0)

choice_var = tk.IntVar()
choice_var.set(1)  # Default choice

choices = [
    ("Employee Info", 1),
    ("HR Related Info", 2),
    ("Employee History", 3)
]

for text, val in choices:
    choice_btn = ttk.Radiobutton(frame, text=text, variable=choice_var, value=val)
    choice_btn.grid(column=val, row=1, padx=10, pady=5)

display_btn = ttk.Button(frame, text="Display Info", command=seaemp)
display_btn.grid(column=0, row=2, columnspan=3, padx=20, pady=10)

result_text = tk.Text(frame, height=10, width=50)
result_text.grid(column=0, row=3, columnspan=3)
result_text.config(state='disabled')

app.mainloop()
