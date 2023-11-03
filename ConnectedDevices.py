# -*- coding: utf-8 -*-


from tkinter import *
import serial.tools.list_ports as aa


for i in aa.comports():
    print("basic : {}".format(i))
    print("device : {}".format(i.device))
    print("name : {}".format(i.name))
    print("description : {}".format(i.description))
    print("hwid : {}".format(i.hwid))
    print("vid : {}".format(i.vid))
    print("pid : {}".format(i.pid))
    print("serialnumber : {}".format(i.serial_number))
    print("location : {}".format(i.location))
    print("manufacturer : {}".format(i.manufacturer))
    print("product : {}".format(i.product))
    print("interface : {}".format(i.interface))
    print()