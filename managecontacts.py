from tkinter import *
from tkinter.ttk import *
from sqlite3 import *
from tkinter import messagebox

class ManageContactsFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.pack(fill = BOTH, expand = TRUE)

        s = Style()
        s.configure('TFrame', background = 'white')
        s.configure('TLabel', background = 'white', font = ('Arial', 12))
        s.configure('TButton', font = ('Arial', 12))
        s.configure('Treeview.Heading', font = ('Arial', 12))
        s.configure('Treeview', font = ('Arial', 11), rowheight = 25)

        self.con = connect('contacts.db')
        self.cur = self.con.cursor()
        
        self.create_view_all_contacts_frame()

    def create_view_all_contacts_frame(self):
        self.view_all_contacts_frame = Frame(self)
        self.view_all_contacts_frame.place(relx = .5, rely = .5, anchor = CENTER)

        add_new_contact_button = Button(self.view_all_contacts_frame,
        text = "Add New Contact", width = 20, command = self.add_new_contact_button_click)
        add_new_contact_button.grid(row = 0, column = 1, pady = 25, sticky = E)
        
        name_label = Label(self.view_all_contacts_frame, text = "Name:")
        name_label.grid(row = 1, column = 0, sticky = W)

        self.name_entry = Entry(self.view_all_contacts_frame, font = ('Arial', 12), width = 60)
        self.name_entry.grid(row = 1, column = 1, pady = 10)

        self.contacts_treeview = Treeview(self.view_all_contacts_frame,
        columns = ('name', 'phone_no', 'email_id', 'city'), show = 'headings')
        self.contacts_treeview.heading('name', text = "Name", anchor = W)
        self.contacts_treeview.heading('phone_no', text = "Phone Number", anchor = W)
        self.contacts_treeview.heading('email_id', text = "Email Id", anchor = W)
        self.contacts_treeview.heading('city', text = "City", anchor = W)
        self.contacts_treeview.column('name', width = 175)
        self.contacts_treeview.column('phone_no', width = 125)
        self.contacts_treeview.column('email_id', width = 175)
        self.contacts_treeview.column('city', width = 125)
        self.contacts_treeview.grid(row = 3, column = 0, pady = 10, columnspan = 2)

        self.cur.execute("select * from Contact")
        contacts = self.cur.fetchall()
        for contact in contacts:
            self.contacts_treeview.insert("", END, values = contact)

    def add_new_contact_button_click(self):
        self.view_all_contacts_frame.destroy()

        self.add_new_contacts_frame = Frame(self)
        self.add_new_contacts_frame.place(relx = .5, rely = .5, anchor = CENTER)

        name_label = Label(self.add_new_contacts_frame, text = "Name:")
        name_label.grid(row = 0, column = 0, sticky = W)

        self.name_entry = Entry(self.add_new_contacts_frame, font = ('Arial', 12), width = 25)
        self.name_entry.grid(row = 0, column = 1, pady = 5)

        phone_number_label = Label(self.add_new_contacts_frame, text = "Phone Number:")
        phone_number_label.grid(row = 1, column = 0, sticky = W)

        self.phone_number_entry = Entry(self.add_new_contacts_frame, font = ('Arial', 12), width = 25)
        self.phone_number_entry.grid(row = 1, column = 1, pady = 5)

        email_id_label = Label(self.add_new_contacts_frame, text = "Email Id:")
        email_id_label.grid(row = 2, column = 0, sticky = W)

        self.email_id_entry = Entry(self.add_new_contacts_frame, font = ('Arial', 12), width = 25)
        self.email_id_entry.grid(row = 2, column = 1, pady = 5)

        city_label = Label(self.add_new_contacts_frame, text = "City:")
        city_label.grid(row = 3, column = 0, sticky = W)

        self.city_combobox = Combobox(self.add_new_contacts_frame, font = ('Arial', 12),
        width = 23, values = ('Noida', 'Greater Noida', 'Delhi', 'Mumbai', 'Banglore'))
        self.city_combobox.grid(row = 3, column = 1, pady = 5)
        self.city_combobox.set("Please select your city")

        add_button = Button(self.add_new_contacts_frame, text = "Add", width = 25, command = self.add_button_click)
        add_button.grid(row = 4, column = 1, pady = 5)

    def add_button_click(self):
        self.cur.execute("select * from Contact where EmailId = ?", (self.email_id_entry.get(),))
        contact = self.cur.fetchone()
        if contact is None:
            self.cur.execute("insert into Contact values (?, ?, ?, ?)", (self.name_entry.get(),
            self.phone_number_entry.get(), self.email_id_entry.get(), self.city_combobox.get()))
            self.con.commit()
            messagebox.showinfo("Success Message", "Contact details are saved successfully")
            self.add_new_contacts_frame.destroy()
            self.create_view_all_contacts_frame()
        else:
            messagebox.showerror("Error Message", "Contact details are already added")

        
        




        

    
