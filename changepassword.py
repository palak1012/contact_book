from tkinter import *
from tkinter.ttk import *
from sqlite3 import *
from tkinter import messagebox

class ChangePasswordFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.place(relx=.5, rely=.5,anchor=CENTER)

        s = Style()
        s.configure('TFrame', background = 'white')
        s.configure('TLabel', background = 'white', font = ('Arial', 12))
        s.configure('TButton', font = ('Arial', 12))

        old_password_label = Label(self, text = "Old Password:")
        old_password_label.grid(row = 0, column = 0, sticky = E)

        self.old_password_entry = Entry(self, font = ('Arial', 12), width = 15, show = '*')
        self.old_password_entry.grid(row = 0, column = 1, pady = 5)

        new_password_label = Label(self, text = "New Password:")
        new_password_label.grid(row = 1, column = 0, sticky = E)

        self.new_password_entry = Entry(self, font = ('Arial', 12), width = 15, show = '*')
        self.new_password_entry.grid(row = 1, column = 1, pady = 5)

        confirm_password_label = Label(self, text = "Confirm Password:")
        confirm_password_label.grid(row = 2, column = 0, sticky = E)

        self.confirm_password_entry = Entry(self, font = ('Arial', 12), width = 15, show = '*')
        self.confirm_password_entry.grid(row = 2, column = 1, pady = 5)

        change_button = Button(self, text = "Change", width = 15, command = self.change_button_click)
        change_button.grid(row = 3, column = 1, pady = 5)

    def change_button_click(self):
        con = connect('contacts.db')
        cur = con.cursor()
        cur.execute("select * from Login where Password = ?", (self.old_password_entry.get(),))
        row = cur.fetchone()
        if row is not None:
            if self.new_password_entry.get() == self.confirm_password_entry.get():
                cur.execute("update Login set Password = ? where Password = ?",
                (self.confirm_password_entry.get(), self.old_password_entry.get()))
                con.commit()
                messagebox.showinfo('Success Message', "Password is changed successfully")
            else:
                messagebox.showerror('Error Message', "New and Confirm passwords didn't match")
        else:
            messagebox.showerror('Error Message', 'Incorrect old password')



        

        
