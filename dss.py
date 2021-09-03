from tkinter import *
from time import *
from tkinter import ttk, messagebox
import sqlite3

class win(Tk):
    def __init__(self):
        super().__init__()
        self.title("Digital Surveillance System")
        self.state("zoomed")
        self.configure(bg = "gray40")
        self.resizable(False,False)
        self.add_credential_gui()

    def add_credential_gui(self):
        global username_entry, password_entry, key_entry, repassword_entry
        frame = Frame(self, bg = "white", width = 200, height = 200)
        frame.pack(pady = 120)
        ttk.Label(frame, text = "Username").grid(row = 0, column = 0, padx = 2, pady = 2, sticky = W)
        username_entry = ttk.Entry(frame)
        username_entry.grid(row = 0, column = 1, padx = 2, pady = 2, sticky = W)

        ttk.Label(frame, text = "Type Password").grid(row = 1, column = 0, padx = 2, pady = 2, sticky = W)
        password_entry = ttk.Entry(frame)
        password_entry.grid(row = 1, column = 1, padx = 2, pady = 2, sticky = W)

        ttk.Label(frame, text = "Re-type Password").grid(row = 2, column = 0, padx = 2, pady = 2, sticky = W)
        repassword_entry = ttk.Entry(frame)
        repassword_entry.grid(row = 2, column = 1, padx = 2, pady = 2, sticky = W)

        ttk.Label(frame, text = "keyword").grid(row = 3, column = 0, padx = 2, pady = 2, sticky = W)
        key_entry = ttk.Entry(frame)
        key_entry.grid(row = 3, column = 1, padx = 2, pady = 2, sticky = W)

        set_credential = ttk.Button(frame, text = "Save data", command = lambda : win.check_match())
        set_credential.grid(row = 4, column = 1, padx = 2, pady = 2, sticky = W)

        show_credential = ttk.Button(frame, text = "Show data", command = lambda : create_database.db1.show_saved(self))
        show_credential.grid(row = 4, column = 0, padx = 2, pady = 2, sticky = W)

    def check_match():
        first_pass = password_entry.get()
        sec_pass = repassword_entry.get()

        if first_pass == sec_pass:
            add_toDb = lambda : create_database.db1.add_credentials(900,username_entry.get(), password_entry.get(), key_entry.get())
            add_toDb()
            messagebox.showinfo("saving data", "saving credentials have been saved successfully!!!")
        else:
            messagebox.showerror("check matching", "typed passwords not matching")

class create_database:
    def __init__(self):
        pass

    class db1:
        def __init__(self, *args):
            pass

        def create_conn(self):
            global conn, curs
            conn = sqlite3.connect("database1.db")
            curs = conn.cursor()
            self.create_table1()

        def create_table1(self):
            curs.execute("""CREATE TABLE IF NOT EXISTS confidentials(username text,
                                password text,
                                Keyword text)
                                """)
            conn.commit()

        def add_credentials(self, *data):
            print(data)
            curs.execute("INSERT INTO confidentials VALUES(?,?,?)", data)
            conn.commit()
            

        def show_saved(self):
            curs.execute("SELECT * FROM confidentials")
            all_data = curs.fetchall()
            for line in all_data:
                print(line)
        
        
# full_window
call_db1 = create_database().db1()
call_db1.create_conn()
full_window = win()
full_window.mainloop()
