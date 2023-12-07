
import heapq
class SlotManager :

    def __init__(self) :
        self.vacant = []
        heapq.heapify(self.vacant)
        self.unr = -1

    # -> int
    def reserve(self) :
        if not self.vacant :
            self.unr += 1
            return self.unr
        return heapq.heappop(self.vacant)
        
    # slotNumber: int -> None
    def unreserve(self, slotNumber) :
        heapq.heappush(self.vacant, slotNumber)

    # value: int -> None
    def setStartNumber(self, value) :
        self.unr = value


from PIL import Image
import customtkinter as CTk


class DataStorage() :

    def __init__(self) :

        self.contacts = {}
        self.update_flag = False

        #Loading Contacts' info
        self.loadFile()

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


    def updateFile(self, event=None) :
        if self.update_flag :
            book = []
            for ContNo in self.contacts :
                book.append('; '.join(self.contacts[ContNo]['details'].values()) + '\n')
            book.sort()
            with open('ContactBook.txt', 'w+') as F :
                F.writelines(book)
        self.update_flag = False