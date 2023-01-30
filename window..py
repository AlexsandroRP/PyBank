from tkinter import *
from PIL import Image
from ttkthemes import ThemedTk
from tkinter import ttk
from tkinter import messagebox
import ast
import customtkinter
from bank import PyBank
import database
import sqlite3 as lite

con = lite.connect('users.db')

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')
class LoginWindow(customtkinter.CTk):
    
    # INICIALIZAÇÃO DA JANELA DE LOGIN
    #############################################
    def __init__(self):
        super().__init__()       
        self.title("PyBank")
        self.geometry('925x500+300+200')
        self.resizable(0, 0)
        #self.window.config(bg='#333333')
    #############################################
        

    # TELA
    #############################################

    # LOGO
        self.img_logo = PhotoImage(file='pybank.png')
        label = customtkinter.CTkLabel(self, image = self.img_logo, text=None)
        label.place(x=-20, y=-10)
    

        # Texto
        ###########################################
        self.frame_login_text = customtkinter.CTkFrame(self, width=400, height=380)
        self.frame_login_text.place(x=480, y=60)

        self.login_text = customtkinter.CTkLabel(self.frame_login_text, text='Sign in  ', font=('Microsoft YaHei UI',25, 'bold'))
        self.login_text.place(x=50, y=20)

        self.login_text_description = customtkinter.CTkLabel(self.frame_login_text, text='Enter your data correctly to acess your account', font=('Microsoft YaHei UI',12))
        self.login_text_description.place(x=50, y=60)
        ###########################################


        # LOGIN
        ###########################################
        
        # USERNAME 
        self.username = customtkinter.CTkEntry(self.frame_login_text, width=300, font=('Microsoft YaHei UI',12))
        self.username.place(x=50, y=125)
        #self.username.insert(0, 'Username')
        # self.username.bind('<FocusIn>', self.on_enter)
        # self.username.bind('<FocusOut>', self.on_leave)

        self.username_description = customtkinter.CTkLabel(self.frame_login_text, text='Username', font=('Microsoft YaHei UI',12))
        self.username_description.place(x=50,y=153)

        # PASSWORD    
        self.password = customtkinter.CTkEntry(self.frame_login_text, width=300, font=('Microsoft YaHei UI',12), show='*')
        self.password.place(x=50, y=200)
        #self.password.insert(0, 'Password')
        # self.password.bind('<FocusIn>', self.on_enter_pass)
        # self.password.bind('<FocusOut>', self.on_leave_pass)

        self.password_description = customtkinter.CTkLabel(self.frame_login_text, text='Password', font=('Microsoft YaHei UI',12))
        self.password_description.place(x=50,y=228)
        ###########################################

        # Buttons
        ###########################################
        self.button_frame = customtkinter.CTkButton(self.frame_login_text, width=100, text='Sign in', cursor='hand2', font=('Microsoft YaHei UI',12, 'bold'), command=self.signin)
        self.button_frame.place(x=50, y=270)

        self.label_dont_have_account = customtkinter.CTkLabel(self.frame_login_text, text="Don't have an account?", font=('Microsoft YaHei UI',12))
        self.label_dont_have_account.place(x=50, y=330)

        # Button signup
        self.signup_button = customtkinter.CTkButton(self.frame_login_text, width=100, text='Sign up', cursor='hand2', font=('Microsoft YaHei UI',12, 'bold'), command=self.signup_window)
        self.signup_button.place(x=195, y=330)


    ##############################################

    def signin(self):
        username = self.username.get()
        password = self.password.get()

        # file=open('datasheet.txt', 'r')
        # d=file.read()
        # r=ast.literal_eval(d)
        # file.close()

        
        # if username in r.keys() and password == r[username]:
        with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM Users where nameAccount=? AND password=?",(username, password))
                row=cur.fetchone()
                if row:
                    messagebox.showinfo('Validation Ok', 'Welcome to PyBank')
                    for widget in self.winfo_children():
                        widget.destroy()
                    self.call_main_system()     
                else:
                    messagebox.showwarning('Info', 'Login has been failed')    

                 

        # elif username == '' or password == '':
        #         messagebox.showerror('Invalid credentials', 'Fields must not be blank')
            
        # else:
        #     messagebox.showerror('Invalid credentials', 'Invalid Username or Password')


    def signup_button_clicked(self):
        name = self.username_signup.get()
        password = self.password_signup.get()
        confirm = self.confirm_pass_signup.get()
        account = 7777
        balance = 10000
       
        
        if name == '' or password == '' or confirm == '':
            messagebox.showerror('Invalid credentials', 'Fields must not be blank') 

        elif password == confirm:
            
            with con:
                cur = con.cursor()
                cur.execute("INSERT INTO Users (nameAccount, password, balance, account) VALUES (?, ?, ?, ?)",(name, password, balance, account))
                # file=open('datasheet.txt', 'r+')
                # d=file.read()
                # r=ast.literal_eval(d)

                # dic={name:password}
                # r.update(dic)
                # file.truncate(0)
                # file.close()

                # file=open('datasheet.txt', 'w')
                # w=file.write(str(r))-

                messagebox.showinfo('SignUp', 'Sucessful Sign up')
                self.call_signin_window()
                
                
            
                # file=open('datasheet.txt','w')
                # data = str({'Username':'Password'})
                # file.write(data)
                # file.close()
        else:
            messagebox.showerror('Invalid credentials','Password and password confirm do not match')



    ####################################################################        
    # WINDOWS FUNCTIONS    
    def signup_window(self):
        # LOGO
        for widget in self.winfo_children():
                widget.destroy()
        self.img_logo = PhotoImage(file='pybank.png')
        self.label_logo = customtkinter.CTkLabel(self, image=self.img_logo, text=None).place(x=-20, y=-20)
    
        # Texts and entries
        self.frame_signup = customtkinter.CTkFrame(self, width=400, height=400)
        self.frame_signup.place(x=480, y=60)

        self.signup_text = customtkinter.CTkLabel(self.frame_signup, text='Sign up', font=('Microsoft YaHei UI',25, 'bold'))
        self.signup_text.place(x=50, y=20)
        
        # TEXT USERNAME
        self.username_signup= customtkinter.CTkEntry(self.frame_signup, width=300, font=('Microsoft YaHei UI',12))
        self.username_signup.place(x=50,y=80)
        # self.username_signup.insert(0, 'Username')
        # self.username_signup.bind('<FocusIn>', self.on_enter_signup)
        # self.username_signup.bind('<FocusOut>', self.on_leave_signup)

        self.frame_username_signup = customtkinter.CTkFrame(self.frame_signup, width=295, height=2).place(x=50, y=107)
        self.username_signup_description = customtkinter.CTkLabel(self.frame_signup, text='Username', font=('Microsoft YaHei UI',12))
        self.username_signup_description.place(x=50,y=107)

        # TEXT PASSWORD
        self.password_signup = customtkinter.CTkEntry(self.frame_signup, width=300, font=('Microsoft YaHei UI',10), show='*')
        self.password_signup.place(x=50,y=150)
        # self.password_signup.insert(0, 'Password')
        # self.password_signup.bind('<FocusIn>', self.on_enter_pass_signup)
        # self.password_signup.bind('<FocusOut>', self.on_leave_pass_signup)

        self.frame_password_signup = customtkinter.CTkFrame(self.frame_signup, width=295, height=2).place(x=50, y=177)
        self.password_signup_description = customtkinter.CTkLabel(self.frame_signup, text='Password', font=('Microsoft YaHei UI',12))
        self.password_signup_description.place(x=50,y=178)

        # TEXT CONFIRM
        self.confirm_pass_signup = customtkinter.CTkEntry(self.frame_signup, width=300, font=('Microsoft YaHei UI',10), show='*')
        self.confirm_pass_signup.place(x=50,y=220)
        # self.confirm_pass_signup.insert(0, 'Confirm Password')
        # self.confirm_pass_signup.bind('<FocusIn>', self.on_enter_confirm_pass)
        # self.confirm_pass_signup.bind('<FocusOut>', self.on_leave_confirm_pass)

        self.frame_password_signup = customtkinter.CTkFrame(self.frame_signup, width=295, height=2).place(x=50, y=247)
        self.confirm_description = customtkinter.CTkLabel(self.frame_signup, text='Confirm password', font=('Microsoft YaHei UI',12))
        self.confirm_description.place(x=50,y=248)

        ############################################################

        # BUTTON SIGN UP
        self.button_signup = customtkinter.CTkButton(self.frame_signup, width=100, text='Sign Up',font=('Microsoft YaHei UI',12, 'bold'), command=self.signup_button_clicked).place(x=50, y=300)
        self.label_button_signup = customtkinter.CTkLabel(self.frame_signup, text='I have an account?', font=('Microsoft YaHei UI',12))
        self.label_button_signup.place(x=50, y=350)

        self.button_signin = customtkinter.CTkButton(self.frame_signup, width=100, text='Sign in', cursor='hand2', font=('Microsoft YaHei UI',12, 'bold'), command=self.call_signin_window)
        self.button_signin.place(x=170,y=348)  

    def call_signin_window(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.img_logo = PhotoImage(file='pybank.png')
        label = customtkinter.CTkLabel(self, image = self.img_logo, text=None)
        label.place(x=-20, y=-10)
    

        # Texto
        ###########################################
        self.frame_login_text = customtkinter.CTkFrame(self, width=400, height=380)
        self.frame_login_text.place(x=480, y=60)

        self.login_text = customtkinter.CTkLabel(self.frame_login_text, text='Sign in  ', font=('Microsoft YaHei UI',25, 'bold'))
        self.login_text.place(x=50, y=20)

        self.login_text_description = customtkinter.CTkLabel(self.frame_login_text, text='Enter your data correctly to acess your account', font=('Microsoft YaHei UI',12))
        self.login_text_description.place(x=50, y=60)
        ###########################################


        # LOGIN
        ###########################################
        
        # USERNAME 
        self.username = customtkinter.CTkEntry(self.frame_login_text, width=300, font=('Microsoft YaHei UI',12))
        self.username.place(x=50, y=125)

        self.username_description = customtkinter.CTkLabel(self.frame_login_text, text='Username', font=('Microsoft YaHei UI',13))
        self.username_description.place(x=50,y=160)

        # PASSWORD    
        self.password = customtkinter.CTkEntry(self.frame_login_text, width=300, font=('Microsoft YaHei UI',12), show='*')
        self.password.place(x=50, y=200)
        
        self.password_description = customtkinter.CTkLabel(self.frame_login_text, text='Password', font=('Microsoft YaHei UI',13))
        self.password_description.place(x=50,y=232)
        ###########################################

        # Buttons
        ###########################################
        self.button_frame = customtkinter.CTkButton(self.frame_login_text, width=100, text='Sign in', cursor='hand2', font=('Microsoft YaHei UI',12, 'bold'), command=self.signin)
        self.button_frame.place(x=50, y=270)

        self.label_dont_have_account = customtkinter.CTkLabel(self.frame_login_text, text="Don't have an account?", font=('Microsoft YaHei UI',12))
        self.label_dont_have_account.place(x=50, y=330)

        # Button signup
        self.signup_button = customtkinter.CTkButton(self.frame_login_text, width=100, text='Sign up', cursor='hand2', font=('Microsoft YaHei UI',12, 'bold'), command=self.signup_window)
        self.signup_button.place(x=195, y=330)

    def call_main_system(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.main_system_window()

    def create_account_window(self):
        for widget in self.winfo_children():
            widget.destroy()

        label_name = customtkinter.CTkLabel(self, text='Name', font=('Microsoft YaHei UI',15, 'bold'))
        label_name.place(x=20, y=40)  
        self.create_name_entry = customtkinter.CTkEntry(self, width=400, font=('Microsoft YaHei UI',12)) 
        self.create_name_entry.place(x=20, y=70)
        

        label_id = customtkinter.CTkLabel(self, text='ID', font=('Microsoft YaHei UI',15, 'bold'))
        label_id.place(x=20, y=140)  
        self.create_id_entry = customtkinter.CTkEntry(self, width=295, font=('Microsoft YaHei UI',12)) 
        self.create_id_entry.place(x=20, y=170)

        label_account = customtkinter.CTkLabel(self, text='Account Number', font=('Microsoft YaHei UI',15, 'bold'))
        label_account.place(x=20, y=240)
        self.create_account_entry = customtkinter.CTkEntry(self, width=295, font=('Microsoft YaHei UI',12))  
        self.create_account_entry.place(x=20, y=270)

        self.button_create_account = customtkinter.CTkButton(self, width=200, height=80, text='Create account', cursor='hand2', font=('Microsoft YaHei UI',12, 'bold'), command=self.create_account_button)
        self.button_create_account.place(x=20, y=350)

    def create_account_button(self):
        name = self.create_name_entry.get()
        id = self.create_id_entry.get()
        account_number = self.create_account_entry.get()
        balance = 0
        self.user_created = PyBank(name, id, account_number, balance) 
        with con:
            cur = con.cursor()
            cur.execute("INSERT INTO Users (id, name, account, balance) VALUES (?, ?, ?, ?)",(id, name, account_number, balance))
            
        messagebox.showinfo('Validation Ok', 'Account has been created')
        for widget in self.winfo_children():
            widget.destroy()
        self.main_system_window()
        return self.user_created


    def checking_account_window(self):
        for widget in self.winfo_children():
            widget.destroy()

        cur = con.cursor()
        balance_checking = cur.execute("SELECT balance FROM Users WHERE id=?", 1)
        cur.fetchall()
                            
        label_name = customtkinter.CTkLabel(self, text='Account Balance', font=('Microsoft YaHei UI',15, 'bold'))
        label_name.place(x=20, y=40)
        label_balance = customtkinter.CTkLabel(self, text=balance_checking, font=('Microsoft YaHei UI',15, 'bold'))
        label_balance.place(x=20, y=80)
        self.button_back_checking_account = customtkinter.CTkButton(self, width=380, border_spacing=1,border_width=1, height=100, text='Back', cursor='hand2', font=('Microsoft YaHei UI',20, 'bold'), command=self.call_main_system)
        self.button_back_checking_account.place(x=10, y=300)

    def transfer_window(self):
        for widget in self.winfo_children():
            widget.destroy()
        label_name_transfer = customtkinter.CTkLabel(self, text='Transfer:', font=('Microsoft YaHei UI',15, 'bold'))
        label_name_transfer.place(x=20, y=40)
        # self.entry_transfer = customtkinter.CTkEntry(self, width=295, font=('Microsoft YaHei UI',12))  
        # self.entry_transfer.place(x=20, y=70)

        label_name_destination = customtkinter.CTkLabel(self, text='Destination account:', font=('Microsoft YaHei UI',15, 'bold'))
        label_name_destination.place(x=20, y=120)
        self.entry_transfer_destination = customtkinter.CTkEntry(self, width=295, font=('Microsoft YaHei UI',12))  
        self.entry_transfer_destination.place(x=20, y=150)

        label_name_amount = customtkinter.CTkLabel(self, text='Amount:', font=('Microsoft YaHei UI',15, 'bold'))
        label_name_amount.place(x=20, y=200)
        self.entry_amount = customtkinter.CTkEntry(self, width=295, font=('Microsoft YaHei UI',12))  
        self.entry_amount.place(x=20, y=230)

        self.button_transfer_destination = customtkinter.CTkButton(self, width=380, border_spacing=1,border_width=1, height=100, text='Transfer', cursor='hand2', font=('Microsoft YaHei UI',20, 'bold'), command=PyBank.transfer(self.entry_amount.get(), self.entry_transfer_destination.get()))
        self.button_transfer_destination.place(x=20, y=280)

    # def transfer_functions(self, amount):
    #     amount = self.entry_transfer.get()
    #     if self.user_created.balance - amount >= 0:


        

        


    def main_system_window(self):
        label = customtkinter.CTkLabel(self, text='SELECT THE TRANSACTION', font=('Microsoft YaHei UI',20, 'bold'))
        label.place(x=340, y=40)
        self.frame_buttons_left = customtkinter.CTkFrame(self, width=400, height=380)
        self.frame_buttons_left.place(x=20, y=80)

        self.button_check_balance = customtkinter.CTkButton(self.frame_buttons_left, width=380, border_spacing=1, border_color='white',border_width=1, height=100, text='Check Balance', cursor='hand2', font=('Microsoft YaHei UI',20, 'bold'), command=self.checking_account_window)
        self.button_check_balance.grid(row=0, column=0, padx= 20, pady=15)

        self.button_check_transactions = customtkinter.CTkButton(self.frame_buttons_left, width=380, border_spacing=1, border_color='white',border_width=1, height=100, text='Check Transactions', cursor='hand2', font=('Microsoft YaHei UI',20, 'bold'), command=None)
        self.button_check_transactions.grid(row=2, column=0, padx= 20, pady=15)

        self.button_account_info = customtkinter.CTkButton(self.frame_buttons_left, width=380, border_spacing=1, border_color='white',border_width=1, height=100, text='Create Account', cursor='hand2', font=('Microsoft YaHei UI',20, 'bold'), command=self.create_account_window)
        self.button_account_info.grid(row=3, column=0, padx= 20, pady=15)


        self.frame_buttons_right = customtkinter.CTkFrame(self, width=400, height=380)
        self.frame_buttons_right.place(x=488, y=80)

        self.button_withdraw = customtkinter.CTkButton(self.frame_buttons_right, width=380, border_spacing=1, border_color='white',border_width=1, height=100, text='Withdraw', cursor='hand2', font=('Microsoft YaHei UI',20, 'bold'), command=None)
        self.button_withdraw.grid(row=1, column=1, padx= 20, pady=15)

        self.button_transfer = customtkinter.CTkButton(self.frame_buttons_right, width=380, border_spacing=1, border_color='white',border_width=1, height=100, text='Transfer', cursor='hand2', font=('Microsoft YaHei UI',20, 'bold'), command=self.transfer_window)
        self.button_transfer.grid(row=2, column=1, padx= 20, pady=15)

        self.button_deposit = customtkinter.CTkButton(self.frame_buttons_right, width=380, border_spacing=1, border_color='white',border_width=1, height=100, text='Deposit', cursor='hand2', font=('Microsoft YaHei UI',20, 'bold'), command=None)
        self.button_deposit.grid(row=3, column=1, padx= 20, pady=15)


            



  
         





if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()     