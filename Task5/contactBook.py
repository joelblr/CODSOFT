'''
TODO : Add 'Undo' Feature in Modifying Contacts
TODO : Improve Settings Tab
TODO : Show Notifications
TODO : Data Validations
'''

from PIL import Image
import customtkinter as CTk

from heapq import heapify, heappop, heappush
class SlotManager :

    def __init__(self) :
        self.vacant = []
        heapify(self.vacant)
        self.unr = -1

    def reserve(self) :
        if not self.vacant :
            self.unr += 1
            return self.unr
        return heappop(self.vacant)
        
    def unreserve(self, slotNumber) :
        heappush(self.vacant, slotNumber)



class MainFrame(CTk.CTkFrame) :

    def __init__(self, root) :

        super().__init__(root)
        self.configure(width=app.W-100, height=app.H,)
        self.place(x=100, y=0)

        self.bgImg = CTk.CTkLabel(master=self, text='', image=ds.imgs['frame_wlp'])
        self.bgImg.pack()

        name = CTk.CTkLabel(master=self, text='', image=ds.imgs['name'],
            bg_color='#212124', fg_color='#212124',
        )
        name.place(relx=0.05, rely=0.03,)
        self.nameText = CTk.CTkEntry(master=self, width=250,
            placeholder_text='Enter Name',
        )
        self.nameText.place(relx=0.10, rely=0.03,)

        phno = CTk.CTkLabel(master=self, text='', image=ds.imgs['phno'],
            bg_color='#212124', fg_color='#212124',
        )
        phno.place(relx=0.55, rely=0.03,)
        self.phnoText = CTk.CTkEntry(master=self, width=220,
            placeholder_text='Enter Mobile Number',
        )
        self.phnoText.place(relx=0.60, rely=0.03,)

        mail = CTk.CTkLabel(master=self, text='', image=ds.imgs['mail'],
            bg_color='#212124', fg_color='#212124',
        )
        mail.place(relx=0.05, rely=0.10,)
        self.mailText = CTk.CTkEntry(master=self, width=250,
            placeholder_text='Enter Email Address',
        )
        self.mailText.place(relx=0.10, rely=0.10,)

        addr = CTk.CTkLabel(master=self, text='', image=ds.imgs['addr'],
            bg_color='#212124', fg_color='#212124',
        )
        addr.place(relx=0.55, rely=0.10,)
        self.addrText = CTk.CTkEntry(master=self, width=220,
            placeholder_text='Enter Address',
        )
        self.addrText.place(relx=0.60, rely=0.10,)


        self.add = CTk.CTkButton(master=self, text='Add Contact',
            command=app.add2List
        )
        self.add.place(relx=0.5, rely=0.22, anchor=CTk.CENTER)

        self.edit = CTk.CTkButton(master=self, text='Edit Contact',
            command=app.edit2List
        )
        self.edit.place(relx=0.5, rely=0.22, anchor=CTk.CENTER)
        self.edit.place_forget()


        self.search_bar = CTk.CTkEntry(master=self, width=470, height=35,
            font=('Times new roman', 20), justify=CTk.CENTER,
            placeholder_text='Search Bar',
        )
        self.search_bar.place(relx=0.07, rely=0.30)

        find_btn = CTk.CTkButton(master=self, text='', width=0, height=35,
            image=ds.imgs['search'], fg_color='#00FFFF', hover_color='#00FFFF',
            command=app.search_contacts,
        )
        find_btn.place(relx=0.87, rely=0.30)

        self.list_frame = CTk.CTkScrollableFrame(
            master=self, width=500, height=250,
        )
        self.list_frame.place(relx=0.5, rely=0.65, anchor=CTk.CENTER)

        self.F1 = CTk.CTkFrame(master=self.list_frame, width=500, height=1,)
        self.F1.grid(row=0, column=0)

        self.F2 = CTk.CTkFrame(master=self.list_frame, width=100, height=1,)
        self.F2.grid(row=0, column=1)

        self.list_frame.columnconfigure(0, weight=8)
        self.list_frame.columnconfigure(1, weight=2)

    def changeBgImage(self) :
        self.bgImg.configure(image=ds.imgs['frame_wlp'])



class SettingsFrame(CTk.CTkFrame) :

    def __init__(self, root) :
        super().__init__(root)

        self.configure(width=app.W-100, height=app.H,)
        self.place(x=100, y=0)

        self.bgImg = CTk.CTkLabel(master=self, text='', image=ds.imgs['frame_wlp'])
        self.bgImg.grid(row=0, column=0, rowspan=100)

        self.theme = CTk.CTkOptionMenu(
            master=self, values=['light', 'dark', 'system'],
            command=ds.update_theme
        )
        self.theme.grid(row=1, column=0, )
        self.theme.set('system')

        self.wlp = CTk.CTkOptionMenu(
            master=self, values=['wlp 1', 'wlp 2', 'wlp 3', 'wlp 4', 'wlp 5'],
            command=ds.update_wlp
        )
        self.wlp.grid(row=2, column=0)
        self.wlp.set('wlp 1')


    def changeBgImage(self) :
        self.bgImg.configure(image=ds.imgs['frame_wlp'])



class YesNoMessageBox(CTk.CTkToplevel) :

    def __init__(self, root, title, message) :

        super().__init__(root)

        self.result = None
        self.title(title)
        self.geometry('250x100')

        CTk.CTkLabel(master=self, font = ('Times new roman', 16),
            text=message,
        ).place(relx=0.5, rely=0.2, anchor='center')

        CTk.CTkButton(master=self, text='Yes', width=50,
            command=lambda: self.getValue(True)).place(relx=0.3, rely=0.7, anchor='center')
        CTk.CTkButton(master=self, text='No', width=50,
            command=lambda: self.getValue(False)).place(relx=0.7, rely=0.7, anchor='center')

        self.lift()
        self.grab_set()
        self.bind('<Return>', lambda e : self.getValue(True))
        self.bind('<Escape>', lambda e : self.getValue(False))
        self.protocol("WM_DELETE_WINDOW", lambda: self.getValue(False))


    def getValue(self, value) :
        self.result = value
        self.destroy()



class App(CTk.CTk) :

    def __init__(self) :

        super().__init__()

        ds.loadFile()
        slot.unr = len(ds.contacts)-1

        CTk.set_appearance_mode('system')
        CTk.set_default_color_theme('green')

        self.title('Contact Book')

        self.W, self.H = 700, 500
        self.geometry(f'{self.W}x{self.H}')
        self.minsize(self.W, self.H)
        self.resizable(0, 0)

        sidebar = CTk.CTkFrame(
            master=self, width=100, height=self.H,
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
            command=ds.updateFile,
        )
        commit.place(relx=0.55, rely=0.3, anchor='n')

        self.bind('<Control-s>', ds.updateFile)
        self.bind('<Alt-Key-F4>', self.confirm_close)
        self.protocol('WM_DELETE_WINDOW', self.confirm_close)


    def show_yes_no_message_box(self, parent, title, message) :
        message_box = YesNoMessageBox(parent, title, message)
        parent.wait_window(message_box)
        return message_box.result


    def confirm_save(self, event=None) :

        isSave = self.show_yes_no_message_box(self, 'Confirmation', 'Save Changes ?')
        if isSave :
            ds.updateFile()
        ds.update_flag = False

    def confirm_close(self, event=None) :

        if ds.update_flag : self.confirm_save()
        isQuit = self.show_yes_no_message_box(self, 'Confirmation', 'Quit ?')
        if isQuit : self.destroy()


    def create_frames(self) :

        self.frames = {
            'main' : MainFrame(self),
            'settings' : SettingsFrame(self),
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
        self.frames['main'].place(x=100, y=0)

    def indicate_settings(self) :
        self.delete_indicators()
        self.forget_frames()

        if ds.update_flag :  self.confirm_save()

        self.lbl2.configure(fg_color='#B3B3B3')
        self.frames['settings'].place(x=100, y=0)


    def clear_main_fields(self) :
        self.frames['main'].nameText.delete(0, CTk.END)
        self.frames['main'].phnoText.delete(0, CTk.END)
        self.frames['main'].mailText.delete(0, CTk.END)
        self.frames['main'].addrText.delete(0, CTk.END)

    def insert_main_fields(self, idx) :
        self.frames['main'].nameText.insert(0, ds.contacts[idx]['details']['contact_name'])
        self.frames['main'].phnoText.insert(0, ds.contacts[idx]['details']['contact_phno'])
        self.frames['main'].mailText.insert(0, ds.contacts[idx]['details']['contact_mail'])
        self.frames['main'].addrText.insert(0, ds.contacts[idx]['details']['contact_addr'])


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
            text=f"{ds.contacts[idx]['details']['contact_name']}").pack()
        CTk.CTkLabel(master=f2, font = ('Times new roman', 18),
            text=f"{ds.contacts[idx]['details']['contact_phno']}").pack()
        CTk.CTkLabel(master=f2, font = ('Times new roman', 18),
            text=f"{ds.contacts[idx]['details']['contact_mail']}").pack()
        CTk.CTkLabel(master=f2, font = ('Times new roman', 18),
            text=f"{ds.contacts[idx]['details']['contact_addr']}").pack()

        CTk.CTkButton(master=top, text='OK', width=50,
            command=lambda: top.destroy()).grid(row=1, column=0, columnspan=2)

        top.columnconfigure(0, weight=1)
        top.columnconfigure(1, weight=9)

        top.lift();  top.grab_set()
        return top


    def delete_contact(self, idx) :

        contact_details = ds.getLineDetails(idx)

        isDelete = self.show_yes_no_message_box(
            self,
            'Confirmation',
            f'Delete Contact ?\n{contact_details}'
        )

        if isDelete :
            ds.update_flag = True
            for w in ds.contacts[idx]['widgets'] :
                w.destroy()

            slot.unreserve(idx)
            del ds.contacts[idx]


    def search_contacts(self) :
        search = self.frames['main'].search_bar.get()

        data = []
        try :
            int(search)
            for ContNo in ds.contacts :
                if search in ds.contacts[ContNo]['details']['contact_phno'] :
                    data.append(ContNo)
        except :
            for ContNo in ds.contacts :
                if search == '' :
                    data.append(ContNo)
                elif search.lower() in ds.contacts[ContNo]['details']['contact_name'].lower() :
                    data.append(ContNo)
        finally :
            for w in self.frames['main'].F1.winfo_children() :
                w.pack_forget()

            for w in self.frames['main'].F2.winfo_children() :
                w.grid_forget()

            for ContNo in data :
                ds.contacts[ContNo]['widgets'][0].pack(expand=True, fill=CTk.X, pady=2)
                ds.contacts[ContNo]['widgets'][1].grid(row=ContNo, column=0, pady=2)
                ds.contacts[ContNo]['widgets'][2].grid(row=ContNo, column=1, pady=2)


    def edit_contact(self, idx) :
        self.frames['main'].add.place_forget()
        self.frames['main'].edit.place(relx=0.5, rely=0.22, anchor=CTk.CENTER)

        self.contactIdx = idx

        self.clear_main_fields()
        self.insert_main_fields(idx)


    def edit2List(self) :
        ds.update_flag = True

        self.frames['main'].edit.place_forget()
        self.frames['main'].add.place(relx=0.5, rely=0.22, anchor=CTk.CENTER)

        contact_name = ' '.join(map(lambda x : x.title(),
            self.frames['main'].nameText.get().split()))
        contact_phno = self.frames['main'].phnoText.get()
        contact_mail = self.frames['main'].mailText.get().lower()
        contact_addr = ' '.join(map(lambda x : x.title(),
            self.frames['main'].addrText.get().split()))

        self.clear_main_fields()

        info_btn = ds.contacts[self.contactIdx]['widgets'][0]
        info_btn.configure(text=f'{contact_name}          {contact_phno}')

        ds.contacts[self.contactIdx]['details']['contact_name'] = contact_name
        ds.contacts[self.contactIdx]['details']['contact_phno'] = contact_phno
        ds.contacts[self.contactIdx]['details']['contact_mail'] = contact_mail
        ds.contacts[self.contactIdx]['details']['contact_addr'] = contact_addr


    def add2List(self) :
        ds.update_flag = True

        contact_name = ' '.join(map(lambda x : x.title(),
            self.frames['main'].nameText.get().split()))
        contact_phno = self.frames['main'].phnoText.get()
        contact_mail = self.frames['main'].mailText.get().lower()
        contact_addr = ' '.join(map(lambda x : x.title(),
            self.frames['main'].addrText.get().split()))

        c = slot.reserve()
        ds.contacts[c] = {  'details' : {
                                            'contact_name' : contact_name,
                                            'contact_phno' : contact_phno,
                                            'contact_mail' : contact_mail,
                                            'contact_addr' : contact_addr,
                                        }
                        }
        self.create_contact_btn(c)
        self.clear_main_fields()


    def create_contact_btn(self, c) :

        text = ds.getLineDetails(c)

        n = CTk.CTkButton(master=self.frames['main'].F1, text=f'{text}', corner_radius=30,
            font=('Times new roman', 20), command=lambda: self.show_contact(c),
            height=32, anchor='e',
        )
        n.pack(expand=True, fill=CTk.X, pady=2,)

        e = CTk.CTkButton(master=self.frames['main'].F2, image=ds.imgs['edit'], width=0, height=10,
            command=lambda: self.edit_contact(c),   fg_color='blue', text='',
        )
        e.grid(row=c, column=0, pady=2)

        d = CTk.CTkButton(master=self.frames['main'].F2, image=ds.imgs['delete'], width=0, height=10,
            command=lambda: self.delete_contact(c), fg_color='#880808', text='',
        )
        d.grid(row=c, column=1, pady=2)

        ds.contacts[c]['widgets'] = [n, e, d]

    def init_listFrame(self) :
        for ContNo in ds.contacts :
            self.create_contact_btn(ContNo)



class DataStorage() :

    def __init__(self) :

        self.contacts = {}
        self.update_flag = False

        self.name = CTk.CTkImage(
            light_image = Image.open('./images/name_light.png'),
            dark_image  = Image.open('./images/name_dark.png'), size = (30, 30)
        )
        self.phno = CTk.CTkImage(
            light_image = Image.open('./images/phno_light.png'),
            dark_image  = Image.open('./images/phno_dark.png'), size = (30, 30)
        )
        self.mail = CTk.CTkImage(
            light_image = Image.open('./images/mail_light.png'),
            dark_image  = Image.open('./images/mail_dark.png'), size = (30, 30)
        )
        self.addr = CTk.CTkImage(
            light_image = Image.open('./images/addr_light.png'),
            dark_image  = Image.open('./images/addr_dark.png'), size = (30, 30)
        )

        self.edit_img = CTk.CTkImage(Image.open('./images/edit.png'), size = (26,26))
        self.delete_img = CTk.CTkImage(Image.open('./images/bin.png'), size = (26,26))
        self.search_img = CTk.CTkImage(Image.open('./images/find.png'), size = (26,26))

        self.wlps = {
            'wlp 1' : CTk.CTkImage(Image.open('./images/p1.jpeg'), size = (600, 500)),
            'wlp 2' : CTk.CTkImage(Image.open('./images/p2.jpg'), size = (600, 500)),
            'wlp 3' : CTk.CTkImage(Image.open('./images/p3.jpeg'), size = (600, 500)),
            'wlp 4' : CTk.CTkImage(Image.open('./images/p4.jpeg'), size = (600, 500)),
            'wlp 5' : CTk.CTkImage(Image.open('./images/p5.jpeg'), size = (600, 500)),
        }

        self.imgs = {
            'name' : self.name,
            'phno' : self.phno,
            'mail' : self.mail,
            'addr' : self.addr,

            'frame_wlp' : self.wlps['wlp 1'],
            'edit' : self.edit_img,
            'delete' : self.delete_img,
            'search' : self.search_img,
        }


    def update_theme(self, choice) :
        CTk.set_appearance_mode(choice)

    def update_wlp(self, choice) :
        self.imgs['frame_wlp'] = self.wlps[choice]
        app.frames['main'].changeBgImage()
        app.frames['settings'].changeBgImage()


    def getLineDetails(self, idx) :
        return  self.contacts[idx]['details']['contact_name'] + ' '*10 + \
                self.contacts[idx]['details']['contact_phno']

    def loadFile(self) :

        try :
            with open('ContactBook.txt', 'r') as F :
                for idx, line in enumerate(F) :
                    details = line[:-1].split('; ')
                    self.contacts[idx] = {}
                    self.contacts[idx]['details'] = {}
                    self.contacts[idx]['details']['contact_name'] = details[0]
                    self.contacts[idx]['details']['contact_phno'] = details[1]
                    self.contacts[idx]['details']['contact_mail'] = details[2]
                    self.contacts[idx]['details']['contact_addr'] = details[3]

        except Exception as e :
            with open('ContactBook.txt', 'w') as F :
                pass

        finally :
            slot.unr = idx

    def updateFile(self, event=None) :
        if ds.update_flag :
            book = []
            for ContNo in ds.contacts :
                book.append('; '.join(self.contacts[ContNo]['details'].values()) + '\n')
            book.sort()
            with open('ContactBook.txt', 'w+') as F :
                F.writelines(book)
        ds.update_flag = False



if __name__ == '__main__' :

    ds = DataStorage()
    slot = SlotManager()

    app = App()
    app.create_frames()
    app.mainloop()
