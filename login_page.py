import tkinter as tk
import customtkinter
import mysql.connector
import tkinter as tk
from Top50Companies import  topCompany, currentValue,currentProgess, topCompanyMargin
from  sensex_data import current_Sensex_value, current_date, current_percent_value
from average import  avg_List, news_List
from register_page import register

global USERNAME
USERNAME='Guest'

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="albin@democracy@1234",
    database="sensex_db"
)

mycursor = mydb.cursor()

def register_form():
    base = tk.Tk()
    base.geometry("1000x500")
    base.title("Registration Form")
    base.configure(bg="black")  # Set background color to black

    label_width = 20
    label_font = ("Arial", 14)
    entry_width = 40
    entry_font = ("Arial", 14)

    lb1 = tk.Label(base, text="Enter Name", width=label_width, font=label_font, bg="black", fg="white")
    lb1.place(x=20, y=120)
    en1 = tk.Entry(base, width=entry_width, font=entry_font)
    en1.place(x=240, y=120)

    lb3 = tk.Label(base, text="Enter Email", width=label_width, font=label_font, bg="black", fg="white")
    lb3.place(x=20, y=180)
    en3 = tk.Entry(base, width=entry_width, font=entry_font)
    en3.place(x=240, y=180)

    lb4 = tk.Label(base, text="Contact Number", width=label_width, font=label_font, bg="black", fg="white")
    lb4.place(x=20, y=240)
    en4 = tk.Entry(base, width=entry_width, font=entry_font)
    en4.place(x=240, y=240)

    lb6 = tk.Label(base, text="Enter Password", width=label_width, font=label_font, bg="black", fg="white")
    lb6.place(x=20, y=300)
    en6 = tk.Entry(base, show='*', width=entry_width, font=entry_font)
    en6.place(x=240, y=300)

    lb7 = tk.Label(base, text="Re-Enter Password", width=label_width, font=label_font, bg="black", fg="white")
    lb7.place(x=20, y=360)
    en7 = tk.Entry(base, show='*', width=entry_width, font=entry_font)
    en7.place(x=240, y=360)

    error_label = tk.Label(base, width=label_width, font=label_font, bg="black",fg="black")
    error_label.place(x=350, y=450)

    btn_register = tk.Button(base, text="Register", width=15, font=("Arial", 12), command=lambda: register(en1, en3, en4, en6, en7, error_label))
    btn_register.place(x=400, y=500)

    base.mainloop()

def register(en1, en3, en4, en6, en7, error_label):
    global mycursor
    # Get values from Entry widgets
    name = en1.get()
    email = en3.get()
    contact_number = en4.get()
    password = en6.get()
    repassword=en7.get()

    # Check if email already exists in the table
    sql_check = "SELECT * FROM register_page WHERE email = %s"
    mycursor.execute(sql_check, (email,))
    result = mycursor.fetchone()

    if result:
        # Email already exists, display error label
        error_label.config(text="Email already exists", fg="red")
    else:
        # Insert values into the register_page table
        if password==repassword:
            sql = "INSERT INTO register_page (name, email, contact_number, password) VALUES (%s, %s, %s, %s)"
            val = (name, email, contact_number, password)
            mycursor.execute(sql, val)

        # Commit changes
        mydb.commit()
        error_label.config(text="Successfully Registered", fg="green")

        # Clear Entry widgets after registration
        en1.delete(0, tk.END)
        en3.delete(0, tk.END)
        en4.delete(0, tk.END)
        en6.delete(0, tk.END)
        en7.delete(0, tk.END)

register_form()
