# -*- coding: utf-8 -*-


from tkinter import *
from braille import *
import SpecialCharacterIME
import serial as ser


class UI:
    def __init__(self):
        root1 = Tk()
        statebar = stateBar(root1)
        connectdevice = connectDevice(root1)
        Button(root1, text="출력", width = 10).grid(row = 1, column = 2)
        Label(root1, text = "입력", width = 10).grid(row = 1)
        braillebox = brailleBox(root1)
        textline = textLine(root1, braillebox, statebar)
        SpecialCharacter(root1, textline)
        root1.mainloop()


class connectDevice:
    def __init__(self, root):
        Label(root, text = "장치 포트", width = 10).grid(row = 0)
        self.textbox = Entry(root, width = 35)
        self.textbox.grid(row = 0, column = 1, sticky = "WE")
        self.connectButton = Button(root, text="연결", width = 10, command = self.connect)
        self.connectButton.grid(row = 0, column = 2, sticky = "W")
        self.connectedDevicesButton = Button(root, text="장치", width = 10, command = self.getSerial)
        self.connectedDevicesButton.grid(row = 0, column = 3)
        
    def connect(self):
        try:
            self.device = ser.Serial(port='COM3', baudrate=9600)
        except:
            return
        
        self.button.config(state = 'disabled')
        self.device.write("C".encode())
        self.connected = True

    def getSerial(self):
        return self.device
 

class textLine:
    def __init__(self, root, braillebox, statebar):
        self.E = Entry(root, width = 35)
        self.E.grid(row = 1, column = 1, columnspan = 1)
        self.E.bind('<KeyRelease>', self.onchanged)
        self.braillebox = braillebox
        self.statebar = statebar

    def onchanged(self, args):
        a = makeBrailleBlock(self.E.get(), self.statebar)
        b = getBrailleStr(a)
        self.braillebox.modify(b)


class brailleBox:
    def __init__(self, root):
        self.sBar = Scrollbar(root, orient = HORIZONTAL)
        self.sBar.grid(row = 3, column = 0, columnspan = 4, sticky = (E,W))
        self.T = Text(root, width = 70, height = 4, wrap = 'none', xscrollcommand = self.sBar.set, state = 'disabled')
        self.T.grid(row = 2, column = 0, columnspan = 4)
        self.sBar.config(command = self.T.xview)
        
    def modify(self, contents):
        self.T.config(state = 'normal')
        self.T.delete('1.0', END) 
        self.T.insert(END, contents)
        self.T.config(state = 'disabled')


class stateBar:
    def __init__(self, root):
        Label(root, text = "상태").grid(row = 4, column = 0)
        self.state = Label(root, text = "연결되지 않음")
        self.state.grid(row= 4, column = 1, columnspan = 3)


class SpecialCharacter:
    def __init__(self, root, text):
        self.root = root
        Button(root, text="외부 입력기", width = 10, command = self.openSCIME).grid(row = 1, column = 3)

    def openSCIME(self):
        print(SpecialCharacterIME.openExternalIME(self.root))