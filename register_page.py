from tkinter import *
import mysql.connector

def register():
    # Establish connection to MySQL database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="albin@democracy@1234",
        database="sensex_db"
    )

    # Create cursor
    mycursor = mydb.cursor()

    # Get values from Entry widgets
    name = en1.get()
    email = en3.get()
    contact_number = en4.get()
    password = en6.get()

    # Check if email already exists in the table
    sql_check = "SELECT * FROM register_page WHERE email = %s"
    mycursor.execute(sql_check, (email,))
    result = mycursor.fetchone()

    if result:
        # Email already exists, display error label
        error_label=Label(base, text="Email already exist", width=20, font=("arial", 12), fg="red")
        error_label.place(x=170, y=450)
    else:
        # Insert values into the register_page table
        sql = "INSERT INTO register_page (name, email, contact_number, password) VALUES (%s, %s, %s, %s)"
        val = (name, email, contact_number, password)
        mycursor.execute(sql, val)

        # Commit changes
        mydb.commit()
        error_label = Label(base, text="Succesfully Registered", width=20, font=("arial", 12), fg="green")
        error_label.place(x=170, y=450)

        # Clear Entry widgets after registration
        en1.delete(0, END)
        en3.delete(0, END)
        en4.delete(0, END)
        en6.delete(0, END)
        en7.delete(0, END)

    # Close connection
    mydb.close()


base = Tk()
base.geometry("500x500")
base.title("registration form")
base.configure(bg="black")  # Set background color to black

lb1 = Label(base, text="Enter Name", width=10, font=("arial", 12), bg="black", fg="white")
lb1.place(x=20, y=120)
en1 = Entry(base)
en1.place(x=200, y=120)

lb3 = Label(base, text="Enter Email", width=10, font=("arial", 12), bg="black", fg="white")
lb3.place(x=19, y=160)
en3 = Entry(base)
en3.place(x=200, y=160)

lb4 = Label(base, text="Contact Number", width=13, font=("arial", 12), bg="black", fg="white")
lb4.place(x=19, y=200)
en4 = Entry(base)
en4.place(x=200, y=200)

lb6 = Label(base, text="Enter Password", width=13, font=("arial", 12), bg="black", fg="white")
lb6.place(x=19, y=320)
en6 = Entry(base, show='*')
en6.place(x=200, y=320)

lb7 = Label(base, text="Re-Enter Password", width=15, font=("arial", 12), bg="black", fg="white")
lb7.place(x=21, y=360)
en7 = Entry(base, show='*')
en7.place(x=200, y=360)

Button(base, text="Register", width=10, command=register).place(x=200, y=400)

base.mainloop()
