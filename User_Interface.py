from datetime import datetime

import customtkinter
import mysql.connector

import tkinter as tk
from Top50Companies import  topCompany, currentValue,currentProgess, topCompanyMargin
from  sensex_data import current_Sensex_value, current_percent_value
from average import  avg_List
from register_page import register
from  currentdate import current_time, current_date

global USERNAME
USERNAME='Guest'


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="albin@democracy@1234",
    database="sensex_db"
)

mycursor = mydb.cursor()

sql = "INSERT INTO sensex_value (date_, time_, sensex_val, sensex_percent) VALUES (%s, %s, %s, %s)"
val = (current_date, current_time, current_Sensex_value, current_percent_value)

mycursor.execute(sql, val)
mydb.commit()

# Close connection
# mydb.close()


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


import tkinter as tk

def register_form():
    base = tk.Tk()
    base.geometry("1000x700")
    base.title("Registration Form")
    base.configure(bg="black")  # Set background color to black

    label_width = 18
    label_font = ("Arial", 20, 'bold')
    entry_width = 30
    entry_font = ("Arial", 20,  'bold')

    lb1 = tk.Label(base, text="Enter Name", width=label_width, font=label_font, bg="black", fg="white")
    lb1.place(x=20, y=120)
    en1 = tk.Entry(base, width=entry_width, font=entry_font)
    en1.place(x=320, y=120)

    lb3 = tk.Label(base, text="Enter Email", width=label_width, font=label_font, bg="black", fg="white")
    lb3.place(x=20, y=180)
    en3 = tk.Entry(base, width=entry_width, font=entry_font)
    en3.place(x=320, y=180)

    lb4 = tk.Label(base, text="Contact Number", width=label_width, font=label_font, bg="black", fg="white")
    lb4.place(x=20, y=240)
    en4 = tk.Entry(base, width=entry_width, font=entry_font)
    en4.place(x=320, y=240)

    lb6 = tk.Label(base, text="Enter Password", width=label_width, font=label_font, bg="black", fg="white")
    lb6.place(x=20, y=300)
    en6 = tk.Entry(base, show='*', width=entry_width, font=entry_font)
    en6.place(x=320, y=300)

    lb7 = tk.Label(base, text="Re-Enter Password", width=label_width, font=label_font, bg="black", fg="white")
    lb7.place(x=20, y=360)
    en7 = tk.Entry(base, show='*', width=entry_width, font=entry_font)
    en7.place(x=320, y=360)

    error_label = tk.Label(base, width=label_width, font=label_font, bg="black",fg="black")
    error_label.place(x=350, y=450)

    btn_register = tk.Button(base, text="Register", width=15, font=("Arial", 12), command=lambda: register(en1, en3, en4, en6, en7, error_label))
    btn_register.place(x=400, y=500)

    base.mainloop()







def submit(user_name_entry, password_entry, app):
    UserName = user_name_entry.get()
    PassWord = password_entry.get()

    # Fetch username from the database if the credentials are valid
    mycursor.execute(f'SELECT name FROM register_page WHERE email = %s AND password = %s', (UserName, PassWord))
    result = mycursor.fetchone()

    if result:
        # Username exists in the database
        welcome_message = f'Welcome {result[0]} !'
        USERNAME=result[0]
        username_label.configure(text=f"Welcome {USERNAME}", fg="green")
    else:
        # Username does not exist or credentials are invalid
        welcome_label.configure(text="Invalid Username or Password", fg="red")


def sign_in_page():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")
    app = customtkinter.CTk()

    app.title("Sensex Management/login")
    app.geometry("500x500")

    frame = customtkinter.CTkFrame(master=app, width=500, height=450)
    frame.pack(padx=20, pady=20)

    user_name_entry = customtkinter.CTkEntry(master=frame,
                                             placeholder_text="email",
                                             placeholder_text_color="white",
                                             height=40,
                                             width=200)
    user_name_entry.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    password_entry = customtkinter.CTkEntry(master=frame,
                                            placeholder_text="password",
                                            height=40,
                                            width=200,
                                            placeholder_text_color="white")
    password_entry.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    submit_button = customtkinter.CTkButton(master=frame, text="Submit",
                                            command=lambda: submit(user_name_entry, password_entry, app))
    submit_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    global welcome_label
    welcome_message = "Welcome Guest!"
    # welcome_label = customtkinter.CTkLabel(app, width=450, height=40, font=("Arial", 23, 'bold'), text_color='white',
    #                                        text=welcome_message, fg_color='black', anchor='w')
    # welcome_label.place(relx=0.02, rely=0.03)

    app.mainloop()




customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
app=customtkinter.CTk()


app.title("Sensex Management")
app.geometry("1100x700")



#     --------------------------------------------------company frame starts --------------------------------------------------------

Company_frame=customtkinter.CTkFrame(master=app, width=750,height=454, fg_color='white', bg_color='grey')
Company_frame.place(relx=0.01, rely=0.35)


Industry_label=customtkinter.CTkLabel(Company_frame, width=50, height=2, font=("Arial", 16, 'bold'), text_color='black', text='Industry', fg_color='white' )
current_value_label=customtkinter.CTkLabel(Company_frame, width=60, height=2, font=("Arial", 16, 'bold'),fg_color='white', text_color='black', text='Current Value')
progress_label=customtkinter.CTkLabel(Company_frame, width=50, height=2, font=("Arial", 16, 'bold'),fg_color='white', text_color='black', text='Progress')
Margin_label=customtkinter.CTkLabel(Company_frame, width=50, height=2, font=("Arial", 16, 'bold'),fg_color='white', text_color='black', text="Margin")


# f'Industry\t\t\tCurrentValue\tProgress\t\t\tMargin\n'
Industry_label.place(relx=0.05, rely=0.01)
current_value_label.place(relx=0.45, rely=0.01)
progress_label.place(relx=0.64, rely=0.01)
Margin_label.place(relx=0.83, rely=0.01)

companyList_textbox=customtkinter.CTkTextbox(Company_frame, width=735, height=455, font=("Arial", 15, 'bold'))
companyList_textbox.place(relx=0.01, rely=0.09)


for i, j , k, l in zip(topCompany, currentValue,currentProgess, topCompanyMargin):
    kval="".join(k)
    if k[0] == '+':
        lval=f'+{l}'
        # print(f'{i} {j} {"".join(k)}, +{l}')
        companyList_textbox.insert('0.0', text=f'{i}\t\t\t\t\t{j}\t\t{kval}\t\t{lval}\n')
    else:
        lval = f'-{l}'
        companyList_textbox.insert('0.0', text=f'{i}\t\t\t\t\t{j}\t\t{kval}\t\t{lval}\n')
    # companyList_textbox.insert('0.0', text=f'\n')
#     --------------------------------------------------company frame ends --------------------------------------------------------

#     --------------------------------------------------user frame starts --------------------------------------------------------

user_frame=customtkinter.CTkFrame(master=app, width=750,height=180, fg_color='white')
user_frame.place(relx=0.01, rely=0.01)


username_label=customtkinter.CTkLabel(user_frame,width=450, height=40, font=("Arial", 23, 'bold'), text_color='black', text=f'Welcome Guest', fg_color='white', anchor='w')
username_label.place(relx=0.02, rely=0.03)

def logout():

    USERNAME="Guest"
    username_label = customtkinter.CTkLabel(app, width=450, height=40, font=("Arial", 23, 'bold'),
                                            text_color='black', text=f'Welcome {USERNAME} !', fg_color='white',
                                            anchor='w')
    username_label.place(relx=0.02, rely=0.03)

BSE_Sensex_label=customtkinter.CTkLabel(user_frame,width=450, height=5, font=("Arial", 13, 'bold'), text_color='black', text='BSE SENSEX', fg_color='white', anchor='w')
BSE_Sensex_label.place(relx=0.02, rely=0.4)
BSE_Sensex_Value_label=customtkinter.CTkLabel(user_frame,width=150, height=40, font=("Arial", 30, 'bold'), text_color='black', text=f'{current_Sensex_value}', fg_color="white", anchor='w')
BSE_Sensex_Value_label.place(relx=0.05, rely=0.5)

date_label=customtkinter.CTkLabel(user_frame,width=100, height=15, font=("Arial", 13, 'bold'), text_color='black', text=f'{current_date}', fg_color='white', anchor='w')
date_label.place(relx=0.05, rely=0.8)

current_percent_value_color='green'
current_percent_value_arrow = '▲'
if(current_percent_value<0):
    current_percent_value_arrow = '▼'
    current_percent_value_color='red'
current_percent_value_label=customtkinter.CTkLabel(user_frame,width=50, height=15, font=("Arial", 20, 'bold'), text_color=current_percent_value_color, text=f'{current_percent_value}', fg_color='white', anchor='w')
current_percent_value_label.place(relx=0.31, rely=0.55)

current_percent_arrow_label=customtkinter.CTkLabel(user_frame,width=10, height=5, font=("Arial", 21, 'bold'), text_color=current_percent_value_color,text=f'{current_percent_value_arrow}', fg_color='white', )
current_percent_arrow_label.place(relx=0.28, rely=0.55)
#     --------------------------------------------------user frame ends --------------------------------------------------------

#     --------------------------------------------------average frame starts --------------------------------------------------------
average_frame=user_frame=customtkinter.CTkFrame(master=app,width=300,height=300, fg_color='white', bg_color='grey')
user_frame.place(relx=0.71, rely=0.563)

averageList_textbox=customtkinter.CTkTextbox(average_frame, width=290, height=300, font=("Arial", 15, 'bold'))
averageList_textbox.place(relx=0.019, rely=0.01)
for i in avg_List:
    averageList_textbox.insert('0.0', text=f'\n{i}\n\n')
average_Label=customtkinter.CTkLabel(app,width=50, height=15, font=("Arial", 20, 'bold'), text_color='white', text='Averages',  anchor='w')
average_Label.place(relx=0.72, rely=0.5)
#     --------------------------------------------------average frame ends --------------------------------------------------------

#     --------------------------------------------------Register button start --------------------------------------------------------
register_Button = customtkinter.CTkButton(app, width=100, height=35, text="Register", text_color='black',
                                              fg_color='white', font=("Arial", 15, 'bold'), command=register_form)
signIN_Button = customtkinter.CTkButton(app, width=100, height=35, text="Sign in", text_color='black',
                                        fg_color='white', font=("Arial", 15, 'bold'), command=sign_in_page)

logout_Button = customtkinter.CTkButton(app, width=100, height=35, text="Logout", text_color='black',
                                        fg_color='white', font=("Arial", 15, 'bold'), command=logout)

if USERNAME=='Guest':
    register_Button.place(relx=0.76, rely=0.02)
    signIN_Button.place(relx=0.86, rely=0.02)
else:
    register_Button.destroy()
    signIN_Button.destroy()
    logout_Button.place(relx=0.86, rely=0.02)

#     --------------------------------------------------Register button ends --------------------------------------------------------


app.mainloop()



