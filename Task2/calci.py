class Calci() :

    def __init__(self) :
        self.history = []
        self.FRAC = 6
        self.VIEW = "────────────────────────────────"


    def reset(self) :
        self.num1 = self.num2 = self.symb = ""
        self.errorFlag = ''
        print(self.VIEW)


    def getOperand(self, msg) :
        while True :
            try :
                s = input(msg)
                if s.lower() in ['memo', 'exit', 'info'] :
                    return s.lower()

                return round(float(s), self.FRAC)

            except Exception :
                print("Plz enter a valid Number.")


    def displayHistory(self) :
        if not self.history :
            print("<NO HISTORY>")
        else :
            print("\n".join(self.history))

    def showInfo(self) :
        print(self.VIEW)
        print("type info: to display this msg")
        print("type memo: to display history")
        print("type exit: to terminate")

    def terminate(self) :
        print(self.VIEW)
        exit()

    def checkStatus(self, status) :
        if status == "exit" :
            self.terminate()

        if status == "info" :
            self.showInfo()
            self.errorFlag = True
            return True

        if status == "memo" :
            self.displayHistory()
            self.errorFlag = True
            return True

        return False


    def getInput(self) :

        self.num1 = str(self.getOperand("Enter first  operand: "))
        flag = self.checkStatus(self.num1)

        if not flag :
            self.num2 = str(self.getOperand("Enter second operand: "))
            flag = self.checkStatus(self.num2)

        if not flag :
            self.symb = input("Enter operator +-*/%: ")
            self.check_limits()


    def check_limits(self) :

        if self.symb.lower() == "memo" :
            self.displayHistory()
            self.errorFlag = True
            return

        try :
            self.errorFlag = '1'
            if self.symb not in {'+', '-', '*', '/', '%'} :
                raise Exception

            self.errorFlag = '2'
            if self.symb in {'/', '%'} and float(self.num2) == 0.0 :
                raise Exception

            self.errorFlag = ''

        except Exception :
            self.handleError()


    def handleError(self) :

        if self.errorFlag == '1' :
            print("Operator Error: Pls use +-*/%")
        elif self.errorFlag == '2' :
            print("Zero-Division Error")


    def getResult(self) :
        if not self.errorFlag :
            res = eval(self.num1 + self.symb + self.num2)
            self.history.append("%s %c %s -> %.2f" % (self.num1, self.symb, self.num2, res))
            print(self.history[-1])



if __name__ == "__main__":

    obj = Calci()
    obj.showInfo()
    while True :
        obj.reset()
        obj.getInput()
        obj.getResult()
