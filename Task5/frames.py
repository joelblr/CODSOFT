import customtkinter as CTk


class MainFrame(CTk.CTkFrame) :

    def __init__(self, app, App) :

        super().__init__(app)
        MainFrame.App = App

        self.configure(width=app.mW, height=app.H,)
        self.place(x=app.sbW, y=0)

        self.bgImg = CTk.CTkLabel(master=self, text='', image=App.ds.imgs['frame_wlp'])
        self.bgImg.pack()

        name = CTk.CTkLabel(master=self, text='', image=App.ds.imgs['name'],
            bg_color='#212124', fg_color='#212124',
        )
        name.place(relx=0.05, rely=0.03,)
        self.nameText = CTk.CTkEntry(master=self, width=250,
            placeholder_text='Enter Name',
        )
        self.nameText.place(relx=0.10, rely=0.03,)

        phno = CTk.CTkLabel(master=self, text='', image=App.ds.imgs['phno'],
            bg_color='#212124', fg_color='#212124',
        )
        phno.place(relx=0.55, rely=0.03,)
        self.phnoText = CTk.CTkEntry(master=self, width=220,
            placeholder_text='Enter Mobile Number',
        )
        self.phnoText.place(relx=0.60, rely=0.03,)

        mail = CTk.CTkLabel(master=self, text='', image=App.ds.imgs['mail'],
            bg_color='#212124', fg_color='#212124',
        )
        mail.place(relx=0.05, rely=0.10,)
        self.mailText = CTk.CTkEntry(master=self, width=250,
            placeholder_text='Enter Email Address',
        )
        self.mailText.place(relx=0.10, rely=0.10,)

        addr = CTk.CTkLabel(master=self, text='', image=App.ds.imgs['addr'],
            bg_color='#212124', fg_color='#212124',
        )
        addr.place(relx=0.55, rely=0.10,)

        self.addrMenu = CTk.CTkOptionMenu(
            master=self, width=100,
            values=[
                'Amaravati, Andhra Pradesh, India',
                'Itanagar, Arunachal Pradesh, India',
                'Dispur, Assam, India',
                'Patna, Bihar, India',
                'Raipur, Chhattisgarh, India',
                'Panaji, Goa, India',
                'Gandhinagar, Gujarat, India',
                'Chandigarh, Haryana, India',
                'Shimla, Himachal Pradesh, India',
                'Ranchi, Jharkhand, India',
                'Bengaluru, Karnataka, India',
                'Thiruvananthapuram, Kerala, India',
                'Bhopal, Madhya Pradesh, India',
                'Mumbai, Maharashtra, India',
                'Imphal, Manipur, India',
                'Shillong, Meghalaya, India',
                'Aizawl, Mizoram, India',
                'Kohima, Nagaland, India',
                'Bhubaneswar, Odisha, India',
                'Chandigarh, Punjab, India',
                'Jaipur, Rajasthan, India',
                'Gangtok, Sikkim, India',
                'Chennai, Tamil Nadu, India',
                'Hyderabad, Telangana, India',
                'Agartala, Tripura, India',
                'Lucknow, Uttar Pradesh, India',
                'Dehradun, Uttarakhand, India',
                'Kolkata, West Bengal, India',
            ],
        )
        self.addrMenu.place(relx=0.60, rely=0.10,)
        self.addrMenu.set('Select your Address')
        self.addrMenu.configure(width=100)

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
            image=App.ds.imgs['search'], fg_color='#00FFFF', hover_color='#00FFFF',
            command=app.search_contacts,
        )
        find_btn.place(relx=0.87, rely=0.30)

        self.list_frame = CTk.CTkScrollableFrame(master=self, width=500, height=250)
        self.list_frame.place(relx=0.5, rely=0.65, anchor=CTk.CENTER)

        self.F1 = CTk.CTkFrame(master=self.list_frame, width=500, height=1,)
        self.F1.grid(row=0, column=0)

        self.F2 = CTk.CTkFrame(master=self.list_frame, width=100, height=1,)
        self.F2.grid(row=0, column=1)

        self.list_frame.columnconfigure(0, weight=8)
        self.list_frame.columnconfigure(1, weight=2)

    def changeBgImage(self) :
        self.bgImg.configure(image=MainFrame.App.ds.imgs['frame_wlp'])


#XXX TODO : add a frame 'Settings'
class SettingsFrame(CTk.CTkFrame) :

    def __init__(self, app, App) :
        super().__init__(app)

        SettingsFrame.App = App

        self.configure(width=app.mW, height=app.H,)
        self.place(x=app.sbW, y=0)

        self.bgImg = CTk.CTkLabel(master=self, text='', image=App.ds.imgs['frame_wlp'])
        self.bgImg.grid(row=0, column=0, rowspan=100)

        self.theme = CTk.CTkOptionMenu(
            master=self, values=['light', 'dark', 'system'],
            command=app.update_theme
        )
        self.theme.grid(row=1, column=0, )
        self.theme.set('system')

        self.wlp = CTk.CTkOptionMenu(
            master=self, values=['wlp 1', 'wlp 2', 'wlp 3', 'wlp 4', 'wlp 5'],
            command=app.update_wlp
        )
        self.wlp.grid(row=2, column=0)
        self.wlp.set('wlp 1')


    def changeBgImage(self) :
        self.bgImg.configure(image=SettingsFrame.App.ds.imgs['frame_wlp'])