# -*- coding: utf-8 -*-


from tkinter import *


class ExternalIME:

    def __init__(self, root, CLICKED):
        self.CLICKED = CLICKED
        self.IME = Toplevel(root)

        self.T = Entry(self.IME, width = 30, state = "disabled")
        self.T.grid(row = 0, column = 0, columnspan = 3, sticky = "NS")

        self.backspace = Button(self.IME, width = 9, height = 1, text = "DELETE", command = self.backSpace)
        self.backspace.grid(row = 0, column = 3)

        self.menu = list()
        for i in range(4):
            self.menu += [Button(self.IME, width = 9, height = 1)]
            self.menu[i].grid(row = 1, column = i, pady = 5)

        self.menu[0].config(text = "문장부호", command = self.menu0)
        self.menu[1].config(text = "수학기호", command = self.menu1)
        self.menu[3].config(text = "EXPORT", command = self.export)

        self.buttons = [[],[],[]]
        for i in range(3):
            for j in range(4):
                self.buttons[i] += [Button(self.IME, width = 9, height = 4)]
                self.buttons[i][j].grid(row = i + 2, column = j)

    def menu0(self):
        pass

    def menu1(self):
        self.buttons[0][0].config(text = "÷", command = lambda: self.putChar('÷'))
        self.buttons[0][1].config(text = "×", command = lambda: self.putChar('×'))

    def putChar(self, char):
        self.T.config(state = 'normal')
        self.T.insert(END, char)
        self.T.config(state = 'disabled')

    def backSpace(self):
        self.T.config(state = 'normal')
        self.T.delete(first = 0, last = END) 
        self.T.config(state = 'disabled')

    def export(self):
        self.CLICKED[0] = True
        self.CLICKED[1] = self.T.get()
        self.IME.destroy()

    def isRunning(self):
        try:
            if self.IME.state() == 'normal':
                return True
            else:
                return False
        except:
            return False



def openExternalIME(root):
    EXPORTED = [False, ""]

    print (A.isRunning())
    #while A.isRunning() == True:
    #    pass

    if EXPORTED[0] == True:
        return EXPORTED[1]
    else:
        print("An error occured")
        return

def main():
    print(isRunning())
    print(openExternalIME())


if __name__ == '__main__':
    main()