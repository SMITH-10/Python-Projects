from tkinter import *
from tkinter import messagebox
import pyttsx3
import webbrowser
import mysql.connector as con
from tkinter import Label
from PIL import Image, ImageTk
import tkinter as tk
global n1
global n2
global bg2 
def main():
    global n1
    global n2
    global window
    window = Tk()
    window.geometry("1400x1000")
    window.title("TuneShed")
    bg = PhotoImage(file="first_page.png")
    label1 = Label(window, image=bg)
    label1.place(x=0, y=0)
    n1 = Entry(window, font=("Arial", 13), bd=5)
    n1.place(x=1050, y=390)
    n2 = Entry(window, font=("Arial", 13), bd=5)
    n2.place(x=1050, y=480)
    p1 = Button(window, text="LOGIN", font=("nunito sans extended", 13), bg="cadetblue3", bd=5, command=login)
    p1.place(x=1120, y=550)
    engine = pyttsx3.init()
    engine.say("Welcome Guest")
    engine.runAndWait()
    window.mainloop()

def login():
    global n1
    global n2
    global bg2
    win = Tk()
    win.geometry("1400x1000")
    win.title("TuneShed")
    win.configure(bg="gainsboro")
    l1=Label(win, text="Nifty Nerd", font=("opensans", 50), bg="gainsboro" )
    l2=Label(win, text="Welcome ", font=("Arial Black", 20), bg="gainsboro")
    l1.place(x=500, y=100)
    l2.place(x=600, y=200)
    if(n1.get()=="n" and n2.get()=="s"):
        l1=Label(win, text="Welcome to Nifty Nerds HR Management System. At Nifty Nerds, we believe that every", font=("nunito sans extended", 20), bg="gainsboro")
        l2=Label(win, text="organization's success is built on the shoulders of its exceptional team members.", font=("nunito sans extended", 20), bg="gainsboro")
        l3=Label(win, text="Our HR system is the key to unlocking the true potential of your workforce. With our ", font=("nunito sans extended", 20), bg="gainsboro")
        l4=Label(win, text="cutting-edge technology and user-friendly interface, we empower you to streamline ", font=("nunito sans extended", 20), bg="gainsboro")
        l5=Label(win, text="your HR processes, from recruitment to employee development. Join us on a journey of ", font=("nunito sans extended", 20), bg="gainsboro")
        l5=Label(win, text="simplified HR management, where every employee is a valued asset, and every task is as", font=("nunito sans extended", 20), bg="gainsboro")
        l6=Label(win, text="easy as pie. Discover the future of HR with Nifty Nerds!", font=("nunito sans extended", 20), bg="gainsboro")
        l7=Label(win, text="Navigating HR, Elevating Success!", font=("open sans", 25), bg="gainsboro")
        l1.place(x=125, y=300)
        l2.place(x=125, y=345)
        l3.place(x=125, y=390)
        l4.place(x=125, y=435)
        l5.place(x=125, y=480)
        l6.place(x=125, y=525)
        l7.place(x=375, y=590)
        p1 = Button(win, text="NEXT", font=("nunito sans extended", 13), bg="azure2", bd=5, command=nextt)
        p1.place(x=600, y=650)
        engine = pyttsx3.init()
        engine.say("Here are some information about our application.... NIFTY NERD")
        engine.runAndWait() 
    else:
       messagebox.showwarning("Caution", "Invalid Password")
    

    win.mainloop()
global w
def nextt():
    global w
    window.destroy()
    w=Tk()
    w.geometry("1400x1000")
    w.title("Tuneed")
    bg2 = PhotoImage(file = 's1.png')
    lab = Label(w, image=bg2)
    lab.pack()
    b1=Button(w, text="      ADD        ", font=("nunito sans extended", 15 ),bg="azure2", bd=5)
    b2=Button(w, text="     UPDATE     ", font=("nunito sans extended", 15),bg="azure2", bd=5)
    b3=Button(w, text="     SEARCH     ", font=("nunito sans extended", 15),bg="azure2", bd=5)
    b4=Button(w, text="     DELETE      ", font=("nunito sans extended", 15),bg="azure2", bd=5)
    b5=Button(w, text="     DISPLAY     ", font=("nunito sans extended", 15),bg="azure2", bd=5)
    b6=Button(w, text=" ATTENDENCE ", font=("nunito sans extended", 15),bg="azure2", bd=5)
    b1.place(x=200,y=275)
    b2.place(x=200, y=350)
    b3.place(x=200, y=425)
    b4.place(x=200, y=495)
    b5.place(x=200, y=570)
    b6.place(x=200, y=645)
    engine = pyttsx3.init()
    engine.say("Here are some feature of our application.... NIFTY NERD")
    engine.runAndWait()
    w.mainloop()






main()