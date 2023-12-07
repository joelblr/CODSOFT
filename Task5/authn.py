import re

#FIXME TODO : Add Phone number Country Code
class Validator :

    def __init__(self) :
        self.regex = '^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$'

    def checkName(self, name: str) :
        if len(name) == 0 :
            raise ValueError('Invalid Contact Name', 'Name cannot be Null !')
        if len(name) > 20 :
            raise ValueError('Invalid Contact Name', 'Name not longer than 20!')

    def checkPhno(self, phno: str) :
        if len(phno) != 10 :
            raise ValueError('Invalid Mobile Number', 'Phno should contain 10 digits!\nNo Leading 0s')
        try :
            int(phno)
        except :
            raise ValueError('Invalid Mobile Number', 'Should contain only digits!')

    def checkMail(self, mail: str) :
        if not re.search(self.regex, mail) :
            raise ValueError('Invalid Email Address', 'Format: email.address@domain.com !')

    def checkAddr(self, addr: str) :
        if len(addr) == 0 or addr == 'Select your Address' :
            raise ValueError('Invalid Address', 'Address cannot be Null !')


class FormatData :

    def __init__(self) :

        self.nameFormatList = {
            'C' : str.capitalize,
            'L' : str.lower,
            'T' : str.title,
            'U' : str.upper,
        }
        self.phnoFormatList = {
            0 : '2-4-4',
            1 : '3-3-4',
            2 : '3-4-3',
            3 : '4-3-3',
            4 : '4-4-2',
            5 : '5-5',
        }
        self.nameFormat = 'T'
        self.phnoFormat = 2

    def formatName(self, name) :
        return ' '.join(map(lambda x : self.nameFormat(x), name.split()))

    def formatPhno(self, phno) :
        idx = 0
        new_phno = ''
        for n in self.phnoFormat.split('-') :
            new_phno += phno[idx : idx + int(n)]
            idx += int(n)
        return new_phno[:-1]

    def formatMail(self, mail) :
        return mail.lower()

    def formatMail(self, addr) :
        return self.formatName(addr)


    def changeNameFormat(self, key) :
        self.nameFormat = self.nameFormatList[key]

    def changePhnoFormat(self, key) :
        self.phnoFormat = self.phnoFormatList[key]
