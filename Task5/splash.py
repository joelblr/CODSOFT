from PIL import Image
import customtkinter as CTk
import time



class SplashScreen(CTk.CTkToplevel) :

    def __init__(self, app) :
        super().__init__(app)
        self.create_screen()

    def create_screen(self) :

        clr = '#5F9EA0'
        splash_img = CTk.CTkImage(Image.open('./images/intro.png'), size = (600, 400))

        self.overrideredirect(True)
        x = self.winfo_screenwidth()//2 - 700//2
        y = self.winfo_screenheight()//2 - 550//2

        self.geometry(f"700x550+{x}+{y}")

        self.configure(fg_color=clr)

        CTk.CTkLabel(master=self, text='Welcome to Link Book', font=(('Trebuchet Ms'), 36),
            text_color='#FFFFFF', 
        ).pack(pady=20)

        CTk.CTkLabel(master=self, text='', image=splash_img).pack()
        self.wait_visibility()


if __name__ == '__main__' :
    app = CTk.CTk()
    spl = SplashScreen(app)
    app.mainloop()