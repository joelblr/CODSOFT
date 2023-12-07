import customtkinter as CTk


class Notify(CTk.CTkToplevel) :

    def __init__(self, app, txt='', time=1500) :
        super().__init__(app)
        self.app = app
        self.SHORT = 1500
        self.LONG = 2500

        self.wm_attributes("-alpha", 0.0)
        self.overrideredirect(True)

        CTk.CTkLabel(master=self, text=txt, font=('times new roman', 20, 'bold'),
            corner_radius=500, fg_color='blue',
        ).pack()

        x = y = 0
        self.geometry(f"+{x}+{y}")
        self.wait_visibility()

        x = self.app.winfo_x() + self.app.sbW + self.app.mW//2 - self.winfo_width()//2
        y = self.app.winfo_y() + self.app.H - 40

        self.geometry(f"+{x}+{y}")
        self.wm_attributes("-alpha", 1.0)

        self.after(time, self.destroy)