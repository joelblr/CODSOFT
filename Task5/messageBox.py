import customtkinter as CTk

class MessageBox(CTk.CTkToplevel) :

    def __init__(self, root, title, message) :

        super().__init__(root)

        self.result = None
        self.title(title)

        CTk.CTkLabel(master=self, font=('Times new roman', 16),
            text=message,
        ).grid(row=0, column=0, columnspan=3, padx=20, pady=15)

        self.a = CTk.CTkButton(master=self, text='Ok', width=50, command=lambda: self.getValue(1))
        self.a.grid(row=1, column=0, padx=20, pady=20)

        self.b = CTk.CTkButton(master=self, text='Cancel', width=50, command=lambda: self.getValue(2))
        self.b.grid(row=1, column=1, padx=5, pady=20)

        self.c = CTk.CTkButton(master=self, text='Close', width=50, command=lambda: self.getValue(3))
        self.c.grid(row=1, column=2, padx=20, pady=20)

        self.lift()
        self.grab_set()
        self.bind('<Return>', lambda e : self.getValue(1))
        self.bind('<Escape>', lambda e : self.getValue(2))
        self.protocol("WM_DELETE_WINDOW", lambda: self.getValue(3))


    def getValue(self, value) :
        self.result = value
        self.destroy()



class WarningMessageBox(MessageBox) :

    def __init__(self, root, title, message) :

        super().__init__(root, title, message)

        self.b.destroy()
        self.c.destroy()
        self.a.configure(text='ok', command=lambda: self.getValue(True))
        self.a.grid(row=1, column=1)



class YesNoMessageBox(MessageBox) :

    def __init__(self, root, title, message) :

        super().__init__(root, title, message)

        self.b.destroy()
        self.a.configure(text='Yes', command=lambda: self.getValue(True))
        self.c.configure(text='No', command=lambda: self.getValue(False))

        self.bind('<Return>', lambda e : self.getValue(True))
        self.bind('<Escape>', lambda e : self.getValue(False))
        self.protocol("WM_DELETE_WINDOW", lambda: self.getValue(False))



if __name__ == '__main__' :

    root = CTk.CTk()
    root.geometry('500x500')

    CTk.CTkButton(master=root, text='Hello', command=root.destroy).pack(pady=100)
    root.bind('<Return>', lambda e : root.destroy())
    root.mainloop()