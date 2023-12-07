'''
TODO : Add Phone number Country Code
TODO : Add 'Undo' Feature in Modifying Contacts
TODO : Improve Settings Tab
'''
import time
import authn
import splash
import frames
import server
import notify
import messageBox
import customtkinter as CTk


class App(CTk.CTk) :

    ds = server.DataStorage()

    def update_app(self) :  self.update()
    def hide_app(self) :  self.withdraw()
    def show_app(self) :  self.deiconify()

    def show_splash_screen(self) :
        return splash.SplashScreen(self)


    def close_splash_screen(self, s) :
        s.destroy()


    def __init__(self) :

        super().__init__()

        CTk.set_appearance_mode('system')
        CTk.set_default_color_theme('green')
        self.title('Link Book')

        #App dimensions
        self.W, self.H = 700, 500

        #frame dimensions
        self.sbW = 100
        self.mW = self.W - self.sbW


    def create_app(self) :

        CTk.set_appearance_mode('system')
        CTk.set_default_color_theme('green')

        self.geometry(f'{self.W}x{self.H}')
        self.minsize(self.W, self.H)
        self.resizable(0, 0)

        sidebar = CTk.CTkFrame(
            master=self, width=self.sbW, height=self.H,
            fg_color='#404040', corner_radius=0
        )
        sidebar.place(x=0, y=0)

        self.lbl1 = CTk.CTkLabel(master=sidebar, text='',
            width=4, height=30, fg_color='#B3B3B3', corner_radius=2,
        )
        self.lbl1.place(relx=0.1, rely=0.1,)

        self.lbl2 = CTk.CTkLabel(master=sidebar, text='',
            width=4, height=30, corner_radius=2,
        )
        self.lbl2.place(relx=0.1, rely=0.2,)

        btn1 = CTk.CTkButton(
            master=sidebar, text='Contacts', width=5, height=30,
            corner_radius=10, bg_color='#404040',
            command=self.indicate_main,
        )
        btn1.place(relx=0.55, rely=0.1, anchor='n')

        btn2 = CTk.CTkButton(
            master=sidebar, text='Settings', width=5, height=30,
            corner_radius=10, bg_color='#404040',
            command=self.indicate_settings,
        )
        btn2.place(relx=0.55, rely=0.2, anchor='n')


        commit = CTk.CTkButton(
            master=sidebar, text='Commit', width=5, height=30,
            corner_radius=10, bg_color='#404040',
            command=App.ds.updateFile,
        )
        commit.place(relx=0.55, rely=0.3, anchor='n')


        self.bind('<Control-s>', App.ds.updateFile)
        self.bind('<Alt-Key-F4>', self.confirm_close)
        self.protocol('WM_DELETE_WINDOW', self.confirm_close)



    def update_theme(self, choice) :
        CTk.set_appearance_mode(choice)

    def update_wlp(self, choice) :
        App.ds.imgs['frame_wlp'] = App.ds.wlps[choice]
        app.frames['main'].changeBgImage()
        app.frames['settings'].changeBgImage()


    def show_yes_no_message_box(self, parent, title, message) :
        message_box = messageBox.YesNoMessageBox(parent, title, message)
        parent.wait_window(message_box)
        return message_box.result


    def confirm_save(self, event=None) :

        isSave = self.show_yes_no_message_box(self, 'Confirmation', 'Save Changes ?')
        if isSave :
            App.ds.updateFile()
        App.ds.update_flag = False

    def confirm_close(self, event=None) :

        if App.ds.update_flag : self.confirm_save()
        isQuit = self.show_yes_no_message_box(self, 'Confirmation', 'Quit ?')
        if isQuit : 
            self.withdraw()
            self.destroy()


    def create_frames(self) :

        self.frames = {
            'main' : frames.MainFrame(self, App),
            'settings' : frames.SettingsFrame(self, App),
        }
        self.frames['settings'].place_forget()

        self.init_listFrame()


    def forget_frames(self) :
        self.frames['main'].place_forget()
        self.frames['settings'].place_forget()

    def delete_indicators(self) :
        self.lbl1.configure(fg_color='#404040')
        self.lbl2.configure(fg_color='#404040')

    def indicate_main(self) :
        self.delete_indicators()
        self.forget_frames()
        self.lbl1.configure(fg_color='#B3B3B3')
        self.frames['main'].place(x=self.sbW, y=0)

    def indicate_settings(self) :
        self.delete_indicators()
        self.forget_frames()

        if App.ds.update_flag :
            App.ds.updateFile()
            App.ds.update_flag = False

        self.lbl2.configure(fg_color='#B3B3B3')
        self.frames['settings'].place(x=self.sbW, y=0)


    def clear_main_fields(self) :
        self.frames['main'].nameText.delete(0, CTk.END)
        self.frames['main'].phnoText.delete(0, CTk.END)
        self.frames['main'].mailText.delete(0, CTk.END)
        self.frames['main'].addrMenu.set('Select your Address')

    def insert_main_fields(self, idx) :
        self.frames['main'].nameText.insert(0, App.ds.contacts[idx]['details']['contact_name'])
        self.frames['main'].phnoText.insert(0, App.ds.contacts[idx]['details']['contact_phno'])
        self.frames['main'].mailText.insert(0, App.ds.contacts[idx]['details']['contact_mail'])
        self.frames['main'].addrMenu.set(App.ds.contacts[idx]['details']['contact_addr'])


    def show_contact(self, idx) :

        top = CTk.CTkToplevel(self)
        top.title('Contact Info')
        top.geometry('400x150')

        f1 = CTk.CTkFrame(master=top, width=20, height=200)
        f2 = CTk.CTkFrame(master=top, width=100, height=200)
        f1.grid(row=0, column=0, sticky='NEWS');  f2.grid(row=0, column=1, sticky='NEWS')

        CTk.CTkLabel(master=f1, font = ('Times new roman', 16), text=f'NAME').pack()
        CTk.CTkLabel(master=f1, font = ('Times new roman', 16), text=f'MOBILE NO.').pack()
        CTk.CTkLabel(master=f1, font = ('Times new roman', 16), text=f'EMAIL').pack()
        CTk.CTkLabel(master=f1, font = ('Times new roman', 16), text=f'ADDRESS').pack()

        CTk.CTkLabel(master=f2, font = ('Times new roman', 18),
            text=f"{App.ds.contacts[idx]['details']['contact_name']}").pack()
        CTk.CTkLabel(master=f2, font = ('Times new roman', 18),
            text=f"{App.ds.contacts[idx]['details']['contact_phno']}").pack()
        CTk.CTkLabel(master=f2, font = ('Times new roman', 18),
            text=f"{App.ds.contacts[idx]['details']['contact_mail']}").pack()
        CTk.CTkLabel(master=f2, font = ('Times new roman', 18),
            text=f"{App.ds.contacts[idx]['details']['contact_addr']}").pack()

        CTk.CTkButton(master=top, text='OK', width=50,
            command=lambda: top.destroy()).grid(row=1, column=0, columnspan=2)

        top.columnconfigure(0, weight=1)
        top.columnconfigure(1, weight=9)

        top.lift();  top.grab_set()
        return top


    def delete_contact(self, idx) :

        contact_details = App.ds.getLineDetails(idx)

        isDelete = self.show_yes_no_message_box(
            self,
            'Confirmation',
            f'Delete Contact ?\n{contact_details}'
        )

        if isDelete :
            notify.Notify(self, 'Contact Deleted')

            App.ds.update_flag = True
            for w in App.ds.contacts[idx]['widgets'] :
                w.destroy()
            slot.unreserve(idx)
            del App.ds.contacts[idx]


    def search_contacts(self) :
        search = self.frames['main'].search_bar.get()

        data = []
        try :
            int(search)
            for ContNo in App.ds.contacts :
                if search in App.ds.contacts[ContNo]['details']['contact_phno'] :
                    data.append(ContNo)
        except :
            for ContNo in App.ds.contacts :
                if search == '' :
                    data.append(ContNo)
                elif search.lower() in App.ds.contacts[ContNo]['details']['contact_name'].lower() :
                    data.append(ContNo)
        finally :
            for w in self.frames['main'].F1.winfo_children() :
                w.grid_forget()

            for w in self.frames['main'].F2.winfo_children() :
                w.grid_forget()
            
            for ContNo in data :
                App.ds.contacts[ContNo]['widgets'][0].grid(row=ContNo, column=0, pady=2)
                App.ds.contacts[ContNo]['widgets'][1].grid(row=ContNo, column=0, pady=2)
                App.ds.contacts[ContNo]['widgets'][2].grid(row=ContNo, column=1, pady=2)


    def isContactFound(self, idx) :
        return idx in App.ds.contacts

    def get_entry_values(self) :
        contact_name = self.frames['main'].nameText.get()
        contact_phno = self.frames['main'].phnoText.get()
        contact_mail = self.frames['main'].mailText.get()
        contact_addr = self.frames['main'].addrMenu.get()

        return (contact_name, contact_phno, contact_mail, contact_addr)


    def edit_contact(self, idx) :
        self.frames['main'].add.place_forget()
        self.frames['main'].edit.place(relx=0.5, rely=0.22, anchor=CTk.CENTER)

        self.contactIdx = idx

        self.clear_main_fields()
        self.insert_main_fields(idx)


    def edit2List(self) :

        c_name, c_phno, c_mail, c_addr = self.get_entry_values()

        action = self.authenticate_details((c_name, c_phno, c_mail, c_addr))
        if action == True :
            return

        if action == False :
            self.clear_main_fields()

        self.frames['main'].edit.place_forget()
        self.frames['main'].add.place(relx=0.5, rely=0.22, anchor=CTk.CENTER)

        if action == None :

            App.ds.update_flag = True
            if self.isContactFound(self.contactIdx) :

                notify.Notify(self, 'Contact Edited')
                info_btn = App.ds.contacts[self.contactIdx]['widgets'][0]
                info_btn.configure(text=f'{c_name}          {c_phno}')

                App.ds.contacts[self.contactIdx]['details']['contact_name'] = c_name
                App.ds.contacts[self.contactIdx]['details']['contact_phno'] = c_phno
                App.ds.contacts[self.contactIdx]['details']['contact_mail'] = c_mail
                App.ds.contacts[self.contactIdx]['details']['contact_addr'] = c_addr
                self.clear_main_fields()

            else :
                contact = c_name + ' '*10 + c_phno
                result = self.show_yes_no_message_box(self, 'Not Found', f'Add as New Contact ?\n{contact}')
                if result :
                    self.add2List()


    def authenticate_details(self, details) :

        try :
            details = list(map(lambda x : x.strip(), details))
            details[1] = details[1].lstrip('0')

            scan.checkName(details[0])
            scan.checkPhno(details[1])
            scan.checkMail(details[2])
            scan.checkAddr(details[3])
        except Exception as e :
            mb = messageBox.YesNoMessageBox(
                self, e.args[0], e.args[1]+'\n\nTry Again ?'
            )
            self.wait_window(mb)

            return mb.result


    def add2List(self) :

        c_name, c_phno, c_mail, c_addr = self.get_entry_values()

        action = self.authenticate_details((c_name, c_phno, c_mail, c_addr))

        if action == True :
            return

        self.clear_main_fields()

        self.frames['main'].edit.place_forget()
        self.frames['main'].add.place(relx=0.5, rely=0.22, anchor=CTk.CENTER)

        if action == None :

            App.ds.update_flag = True
            notify.Notify(self, 'Contact Added')

            c = slot.reserve()
            App.ds.contacts[c] = {  'details' : {
                                                'contact_name' : c_name,
                                                'contact_phno' : c_phno,
                                                'contact_mail' : c_mail,
                                                'contact_addr' : c_addr,
                                            }
                            }
            self.create_contact_btn(c)


    def create_contact_btn(self, c) :

        text = App.ds.getLineDetails(c)

        n = CTk.CTkButton(master=self.frames['main'].F1, text=f'{text}', corner_radius=30,
            font=('Times new roman', 20), command=lambda: self.show_contact(c),
            height=32, anchor='e', width=420,
        )
        n.grid(row=c, column=0, pady=2)

        e = CTk.CTkButton(master=self.frames['main'].F2, image=App.ds.imgs['edit'], width=0, height=10,
            command=lambda: self.edit_contact(c),   fg_color='blue', text='',
        )
        e.grid(row=c, column=0, pady=2)

        d = CTk.CTkButton(master=self.frames['main'].F2, image=App.ds.imgs['delete'], width=0, height=10,
            command=lambda: self.delete_contact(c), fg_color='#880808', text='',
        )
        d.grid(row=c, column=1, pady=2)

        App.ds.contacts[c]['widgets'] = [n, e, d]

    def init_listFrame(self) :
        for ContNo in App.ds.contacts :
            self.create_contact_btn(ContNo)


    def launch(self) :
        time.sleep(0.5)
        spl = splash.SplashScreen(self)

        self.create_app()
        self.wait_visibility()
        self.hide_app()
        self.update_app()
        self.create_frames()
        self.update_app()
        self.show_app()
        spl.destroy()




if __name__ == '__main__' :

    scan = authn.Validator()
    formator = authn.FormatData()

    app = App()
    app.launch()

    slot = server.SlotManager()
    slot.setStartNumber(len(App.ds.contacts)-1)

    notify.Notify(app, 'Welcome to Link Book', 850)

    app.mainloop()

# ------------------------------------------------------------------------------------------------------------