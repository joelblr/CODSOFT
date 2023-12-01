from random import choices, shuffle
from datetime import datetime

class Password() :

    def __init__(self) :
        self.dict = {
            0 : 'qwertyuioplkjhgfdsazxcvbnm',
            1 : 'QWERTYUIOPLKJHGFDSAZXCVBNM',
            2 : '1234567890',
            3 : '~`!@#$%^&*()_+-=[{|\}]:;<,.?/"\'>'
        }
        self.VIEW = "──────────────────────────────────────────────────"


    def getNumber(self, msg, a, b) :
        while True :
            try :
                s = input(msg)
                if s.lower() in ['exit', 'info'] :
                    return s.lower()

                s = int(s)
                if a <= s <= b :
                    return s
                raise Exception

            except Exception :
                print(f"Plz enter a valid Number[{a}-{b}].")


    def showInfo(self) :
        print(self.VIEW)
        print("type info: to display this msg")
        print("type exit: to terminate")

    def terminate(self) :
        print(self.VIEW)
        exit()

    def checkStatus(self, status) :
        if status == "exit" :
            self.terminate()

        if status == "info" :
            self.showInfo()
            self.skipFlag = True
            return True

        return False

    def getLength(self) :
        print(self.VIEW)
        self.skipFlag = False
        self.passLen = str(self.getNumber("Enter Password Length[8-20]: ", 8, 20))
        flag = self.checkStatus(self.passLen)

        if not flag :
            self.lvl = str(self.getNumber("Enter Strength Level [1-4]: ", 1, 4))
            flag = self.checkStatus(self.lvl)

        if not flag :
            self.count = str(self.getNumber("How many PassCodes[1-20]: ", 1, 20))
            flag = self.checkStatus(self.count)


    def genPass(self) :

        if not self.skipFlag :

            self.lvl = int(self.lvl)
            self.count = int(self.count)
            self.passLen = int(self.passLen)

            self.passcode = []
            for _ in range(self.count) :
                tmp, c = [], 0
                for _ in range(self.passLen) :
                    tmp.append(choices(self.dict[c])[0])
                    c = (c + 1) % self.lvl
                shuffle(tmp)
                self.passcode.append("".join(tmp))

            if len(self.passcode) % 2 :
                self.passcode.append("")

            print()
            for i in range(0, len(self.passcode), 2) :
                print(self.passcode[i]," "*7, self.passcode[i+1])


    def save_codes(self) :

        flag = input("\nSave the Passwords[y/n]?: ")

        if flag.lower() == 'y' :
            T = datetime.now()
            a = ('0' if len(str(T.hour)) == 1 else '') + str(T.hour)
            b = ('0' if len(str(T.minute)) == 1 else '') + str(T.minute)
            c = ('0' if len(str(T.second)) == 1 else '') + str(T.second)
            idx = a + b + c

            with open(f'Codes{idx}.txt', 'w') as f :
                for line in self.passcode :
                    if line :
                        f.write(line + "\n")

            print(f"Passwords save in 'Codes{idx}.txt'")


if __name__ == "__main__":

    obj = Password()
    obj.showInfo()
    while True :
        obj.getLength()
        obj.genPass()
        obj.save_codes()
