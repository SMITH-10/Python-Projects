import matplotlib.pyplot as plt
import mysql.connector as sc
import numpy as np
import pandas as pd



def addemp():
    conn=sc.connect(host="localhost",user="root",password="root",database="nerd")
    mycursor=conn.cursor()
    
        
    empid=input("Enter Employee ID: ")
    name=input("Enter Employee Name:")
    designation=input("Enter Employee Designation:")
    salary=input("Enter Employee Salary:")
    emailid=input("Enter Employee Email ID:")

    query="insert into hr values('{}','{}','{}','{}','{}')".format(empid,name,designation,salary,emailid)

    mycursor.execute(query)
    conn.commit()
    print("SUCCESSFULLY ADDED HR DETAILS !!!!!!")

    dob=input("Enter Employee DOB:")
    address=input("Enter Employee Address:")
    mobile_no=input("Enter Employee Mobile No:")

    query="insert into emp_info values('{}','{}','{}','{}','{}')".format(empid,name,dob,address,mobile_no)

    mycursor.execute(query)
    conn.commit()
    print("SUCCESSFULLY ADDED EMPLOYEE DETAILS !!!!!!")
    conn.close()


import mysql.connector as sc

def uppemp():
    print("UPDATE EMPLOYEE DETAILS")

    # Create a connection to the MySQL database
    conn = sc.connect(host="localhost", user="root", password="root", database="nerd")
    mycursor = conn.cursor()

    empid = input("Enter Employee ID: ")
    name = input("Enter Employee Name:")
    dob = input("Enter Employee DOB:")
    address = input("Enter Employee Address:")
    mobile_no = input("Enter Employee Mobile No:")

    # Use placeholders for values in the SQL query
    query = "UPDATE emp_info SET name = %s , dob = %s, address = %s, mobile_no = %s WHERE empid = %s"
    values = (name,dob, address, mobile_no, empid)

    try:
        mycursor.execute(query, values)
        conn.commit()
        print("SUCCESSFULLY UPDATED EMPLOYEE DETAILS !!!!!!")
    except sc.Error as err:
        print(f"Error: {err}")
    finally:
        conn.close()

def update_hr_details():
    print("UPDATE HR DETAILS")

    # Create a connection to the MySQL database


    empid = input("Enter Employee ID: ")
    name = input("Enter Employee Name:")
    designation = input("Enter Employee Designation:")
    salary = input("Enter Employee Salary:")
    emailid = input("Enter Employee Email ID:")

    conn = sc.connect(host="localhost", user="root", password="root", database="nerd")
    mycursor = conn.cursor()
    # Use placeholders for values in the SQL query
    query = "UPDATE HR SET name = %s, designation = %s, salary = %s, emailid = %s WHERE empid = %s"
    values = (name, designation, salary, emailid, empid)

    try:
        mycursor.execute(query, values)
        conn.commit()
        print("SUCCESSFULLY UPDATED HR DETAILS !!!!!!")
    except sc.Error as err:
        print(f"Error: {err}")
    finally:
        conn.close()

# Now you can call the functions to update the employee and HR details
# uppemp()
# update_hr_details()


    
def rememp():

    print("REMOVE EMPLOYEE DETAILS")
    
    conn=sc.connect(host="localhost",user="root",password="root",database="nerd")
    mycursor=conn.cursor()
    empid=input("Enter Employee ID to be removed: ")
    query="delete from emp_info where empid='{}'".format(empid)
    mycursor.execute(query)
    conn.commit()
    print("\n\n")
    print("SUCCESSFULLY REMOVED EMPLOYEE DETAILS !!!!!!")
    

def reemp2():
    conn=sc.connect(host="localhost",user="root",password="root",database="nerd")
    mycursor=conn.cursor()
    empid=input("Enter Employee ID to be removed: ")
    query="delete from hr where empid='{}'".format(empid)
    mycursor.execute(query)
    conn.commit()
    
 
def seaemp():
 
    print ("1.Employee Info")
    print("2. HR Related Info")
    print("3. Employee History")
    ch=int(input("What you want to display"))

    if ch==1:

       

        # Establish a database connection
        conn = sc.connect(host="localhost", user="root", password="root", database="nerd")

        # Check if the connection is successful
        if conn is not None:
            print("Connected to the database.")
        else:
            print("Failed to connect to the database.")
            exit()

        # Execute the SQL query to fetch all rows from the table
        query = pd.read_sql('SELECT * FROM emp_info', conn)

        # Set the maximum number of displayed columns
        pd.set_option("display.max_columns", 20)

        # Display the results
        print(query)

        # Close the database connection when you're done
        conn.close()

    elif ch==2:
       

        # Establish a database connection
        conn = sc.connect(host="localhost", user="root", password="root", database="nerd")

        # Check if the connection is successful
        if conn is not None:
            print("Connected to the database.")
        else:
            print("Failed to connect to the database.")
            exit()

        # Execute the SQL query to fetch all rows from the table
        query = pd.read_sql('SELECT * FROM hr', conn)

        # Set the maximum number of displayed columns
        pd.set_option("display.max_columns", 20)

        # Display the results
        print(query)

        # Close the database connection when you're done
        conn.close()

    elif ch==3:
       

        # Establish a database connection
        conn = sc.connect(host="localhost", user="root", password="root", database="nerd")

        # Check if the connection is successful
        if conn is not None:
            print("Connected to the database.")
        else:
            print("Failed to connect to the database.")
            exit()

        # Execute the SQL query to fetch all rows from the table
        query = pd.read_sql('SELECT * FROM emp_his', conn)

        # Set the maximum number of displayed columns
        pd.set_option("display.max_columns", 20)

        # Display the results
        print(query)

        # Close the database connection when you're done
        conn.close()








#Definition for the Login ()
def Login():
    print("\n\n\n\n")
    print("*******************************")
    print('||                           ||')
    print("||    WELCOME TO KU HRMS     ||")
    print('||                           ||')
    print("*******************************")
    user=input("Enter User Name:")
    pas=input("Enter Password:")
    if user=='a' and pas=='y':
        print("SUCCESSFUULY LOGGED!!!!!!")
        R_Homepage()
    else:
        print("INCORRECT CREDENTIALS")
    Login()  


#DEFINITION FOR HOME PAGE
def R_Homepage():

    print('*********************************')
    print('*                               *')
    print("*      WELCOME TO KU HRMS       *")
    print('*                               *')
    print("*********************************")
    print("*   1. ADD EMPLOYEE DETAILS     *")
    print("*   2. UPDATE EMPLOYEE DETAILS  *")
    print("*   3. REMOVE EMPLOYEE DETAILS  *")
    print("*   4. SEARCH EMPLOYEE DETAILS  *")
    print("*********************************")


    op=int(input("Enter your option:"))
    if   op==1:
        addemp()
    elif op==2:
        uppemp()
        update_hr_details()
    elif op==3:
        rememp()
        reemp2()
    elif op==4:
        seaemp()
    elif op==5:
        TicketBooking()
    elif op==6:
        SearchBooking()
    elif op==7:
        CancelTicket()
    elif op==8:
        Report()
    else:
        print("Invalid Option")


    #loopfunction
def tryagain():
    print('\nWould you like to call main menu again?\nYes or No?')
    n=input()
    
    if n=='Yes' or n=='yes':
        R_Homepage()
        tryagain()
    elif n=='No' or n=='no':
        print('Okay')
    else:
        while n!='Yes' and n!='yes' and n!='No' and n!='no':
            print('Yes or No?')
            n1=input()
            n=n1
        R_Homepage()
        tryagain()
        
#calling main section
Login()
tryagain()



