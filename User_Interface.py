import customtkinter
from Top50Companies import  topCompany, currentValue,currentProgess, topCompanyMargin
from  sensex_data import current_Sensex_value, current_date, current_percent_value

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
username="Albin"

username_label=customtkinter.CTkLabel(user_frame,width=450, height=40, font=("Arial", 23, 'bold'), text_color='black', text=f'Welcome {username} !', fg_color='white', anchor='w')
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











app.mainloop()
