from datetime import datetime
import mysql.connector
import tkinter as tk

# Global variable for USERNAME
USERNAME = 'Guest'

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="albin@democracy@1234",
    database="sensex_db"
)
mycursor = mydb.cursor()

# Placeholder data
topCompany = ["Company 1", "Company 2", "Company 3"]
currentValue = ["Value 1", "Value 2", "Value 3"]
currentProgress = ["Progress 1", "Progress 2", "Progress 3"]
topCompanyMargin = ["Margin 1", "Margin 2", "Margin 3"]
current_Sensex_value = 50000
current_percent_value = 5
current_date = datetime.now().strftime("%Y-%m-%d")
current_time = datetime.now().strftime("%H:%M:%S")
avg_List = ["Average 1", "Average 2", "Average 3"]

# Function to handle registration
def register(en1, en3, en4, en6, en7, error_label):
    # Your registration logic here
    pass

# Function to create registration form
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

# Function to handle user sign-in
def submit(user_name_entry, password_entry, app):
    # Your sign-in logic here
    pass

# Function to create sign-in page
def sign_in_page():
    # Your sign-in page creation logic here
    pass

# Function to handle logout
def logout():
    global USERNAME
    USERNAME = "Guest"

# Creating Tkinter app
app = tk.Tk()
app.title("Sensex Management")
app.geometry("1100x700")

# Rest of your GUI code goes here...

# Placeholder interface components
# Replace with actual interface code

# Placeholder company frame
Company_frame = tk.Frame(app, width=750, height=454, bg="grey")
Company_frame.place(relx=0.01, rely=0.35)

# Placeholder company labels and listbox
# Replace with actual data and labels
for i, j , k, l in zip(topCompany, currentValue, currentProgress, topCompanyMargin):
    pass

# Placeholder user frame
user_frame = tk.Frame(app, width=750, height=180, bg="grey")
user_frame.place(relx=0.01, rely=0.01)

# Placeholder username label, BSE Sensex label, date label, etc.
# Replace with actual data and labels

# Placeholder average frame
average_frame = tk.Frame(app, width=300, height=300, bg="grey")
average_frame.place(relx=0.71, rely=0.563)

# Placeholder average listbox and label
# Replace with actual data and labels
for i in avg_List:
    pass

# Placeholder buttons for register, sign in, and logout
# Replace with actual buttons
register_Button = tk.Button(app, text="Register", command=register_form)
register_Button.place(relx=0.76, rely=0.02)

signIN_Button = tk.Button(app, text="Sign in", command=sign_in_page)
signIN_Button.place(relx=0.86, rely=0.02)

logout_Button = tk.Button(app, text="Logout", command=logout)
logout_Button.place(relx=0.96, rely=0.02)

app.mainloop()
