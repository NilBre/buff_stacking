import numpy as np
import matplotlib.pyplot as plt
import re
# import tkinter as tk
# import tkinter as ttk
from tkinter import *
#import mysql.connector
# what do i need in terms of tkinter features?
# 1. Frame Widget: for the window: (1200, 900) maybe?
# 2. Check Button: so the user can check which buffs and debuffs he wants
# 3. label: to label the check buttons
# 4. List Box: drop down menu for all weapons to display -> the user
    # can choose from the available drop down features
# 5. Canvas: maybe show a picture of the weapon when selecting it
# 6. Scale: slider for the user to pick from a range of values (swashbuckler 1 -> 5) ?
# 7. TopLevel: spawning a new tkinter window
# 8. OptionMenu

class Window():
    def __init__(self, master):
        self.master = master
        self.Main = Frame(self.master)  # ---> define main
        multiplier = [1]
        # --- section1
        self.section1 = Frame(self.Main)  # ---> define section1 inside Main Frame
        ## --- sub section1_1
        self.section1_1 = Frame(self.section1)
        self.L1 = Label(self.section1_1, text="Weapon Name")  # what is written on frame
        self.L1.pack(padx=4, pady=4)  # pack it up

        self.E1 = Entry(self.section1_1)  # what should be tehe stuff, here entry
        self.E1.pack(padx=4, pady=4)

        self.L2 = Label(self.section1_1, text = "Base Damage")
        self.L2.pack(padx=4, pady=4)

        self.E2 = Entry(self.section1_1)
        self.E2.pack(padx=4, pady=4)

        self.L3 = Label(self.section1_1, text = "Damage per Bullet")
        self.L3.pack(padx=4, pady=4)

        self.L4 = Label(self.section1_1, text = f"0")
        self.L4.pack(padx=4, pady=4)

        # self.E3 = Entry(self.section1_1)
        # self.E3.pack(padx=4, pady=4)

        # self.L4 = Label(self.section1_1, text = "Reserves")
        # self.L4.pack(padx=4, pady=4)
        #
        # self.E4 = Entry(self.section1_1)
        # self.E4.pack(padx=4, pady=4)

        self.L5 = Label(self.section1_1, text = f"Damage Multiplier: {round((np.prod(multiplier) - 1) * 100, 1)} in %")  # this needs to be updated
        self.L5.pack(padx=4, pady=4)

        self.section1_1.pack(padx=4, pady=4, side=LEFT)
        ## ---> sub section1_1

        ## ---> sub section1_2
        self.section1_2 = Frame(self.section1)

        self.L6 = Label(self.section1, text="Buffs and Debuffs")
        self.L6.pack(padx=4, pady=4)

        self.C1 = Checkbutton(self.section1_2, text = "Empowering Buff", variable = Cvar1, command = isChecked)
        self.C1.pack(padx=4, pady=4)
        self.C2 = Checkbutton(self.section1_2, text = "Debuff", variable = Cvar2, command = isChecked)
        self.C2.pack(padx=4, pady=4)
        self.C3 = Checkbutton(self.section1_2, text = "Font of Might", variable = Cvar3, command = isChecked)
        self.C3.pack(padx=4, pady=4)
        self.C4 = Checkbutton(self.section1_2, text = "Focused Fury", variable = Cvar4, command = isChecked)
        self.C4.pack(padx=4, pady=4)
        self.C5 = Checkbutton(self.section1_2, text = "Power of Rasputin", variable = Cvar5, command = isChecked)
        self.C5.pack(padx=4, pady=4)
        self.C6 = Checkbutton(self.section1_2, text = "Bait and Switch", variable = Cvar6, command = isChecked)
        self.C6.pack(padx=4, pady=4)

        self.section1_2.pack(padx=4, pady=4, side=RIGHT)
        ## ---> sub section1_2

        ## ---> subsection1_3
        self.section1_2 = Frame(self.section1)

        self.C7 = Checkbutton(self.section1_2, text = "Mask of Bakris", variable = Cvar7, command = isChecked)
        self.C7.pack(padx=4, pady=4)
        self.C8 = Checkbutton(self.section1_2, text = "Firing Line", variable = Cvar8, command = isChecked)
        self.C8.pack(padx=4, pady=4)
        self.C9 = Checkbutton(self.section1_2, text = "Frenzy", variable = Cvar9, command = isChecked)
        self.C9.pack(padx=4, pady=4)
        self.C10 = Checkbutton(self.section1_2, text = "Vorpal Weapon", variable = Cvar10, command = isChecked)
        self.C10.pack(padx=4, pady=4)
        self.C11 = Checkbutton(self.section1_2, text = "Multi Kill Clip", variable = Cvar11, command = isChecked)
        self.C11.pack(padx=4, pady=4)
        self.C12 = Checkbutton(self.section1_2, text = "Swashbuckler", variable = Cvar12, command = isChecked)
        self.C12.pack(padx=4, pady=4)

        self.section1_2.pack(padx=4, pady=4, side=RIGHT)
        ## ---> subsection1_3
        self.section1.pack(padx = 5, pady = 5, expand = True, fill=X)  # ---> pack section up, close it here
        # --- section1

        # --- section2
        self.section2 = Frame(self.Main)  # ---> define section2 Frame inside Main Frame

        # self.Button = Button(self.section2, text="Submit", command = retrieve)
        # self.Button.pack(padx=4, pady=4)

        self.section2.pack(padx=4, pady=4, expand=True, fill=X)
        # section2

        self.Main.pack(padx=4, pady=4)  # ---> pack main up (basically closes it)

# Begin main part
root = Tk()

# define some functions
def retrieve():
    print("==========")
    print(Cvar1.get())
    print(Cvar2.get())
    print(Cvar3.get())
    print(Cvar4.get())
    print(Cvar5.get())
    print(Cvar6.get())
    print(Cvar7.get())
    print(Cvar8.get())
    print(Cvar9.get())
    print(Cvar10.get())
    print(Cvar11.get())
    print(Cvar12.get())
    print("==========")

def isChecked():
    base_damage = window.E2.get()
    multipliers = np.array([1])
    value1  = Cvar1.get()   # empowering buff: for now 35 % (lumina buff)
    value2  = Cvar2.get()   # debuff: for now full debuffed 30 %
    value3  = Cvar3.get()   # Font of Might: 25 %
    value4  = Cvar4.get()   # Focused Fury: 22 %
    value5  = Cvar5.get()   # Power of Rasputin: 10 %
    value6  = Cvar6.get()   # Bait and Switch: 35 %
    value7  = Cvar7.get()   # Mask of Bakris: 20 %
    value8  = Cvar8.get()   # Firing Line: 20 %
    value9  = Cvar9.get()   # Frenzy: 15 %
    value10 = Cvar10.get()  # Vorpal Weapon: for now 10 % (heavy weapons)
    value11 = Cvar11.get()  # Multi Kill Clip: for now max stacks = 50 %
    value12 = Cvar12.get()  # Swashbuckler: for now max stacks = 33.3 %
    if value1 == 1:
        multipliers = np.append(multipliers, 1.35)
    if value2 == 1:
        multipliers = np.append(multipliers, 1.3)
    if value3 == 1:
        multipliers = np.append(multipliers, 1.25)
    if value4 == 1:
        multipliers = np.append(multipliers, 1.22)
    if value5 == 1:
        multipliers = np.append(multipliers, 1.10)
    if value6 == 1:
        multipliers = np.append(multipliers, 1.35)
    if value7 == 1:
        multipliers = np.append(multipliers, 1.20)
    if value8 == 1:
        multipliers = np.append(multipliers, 1.20)
    if value9 == 1:
        multipliers = np.append(multipliers, 1.15)
    if value10 == 1:
        multipliers = np.append(multipliers, 1.10)
    if value11 == 1:
        multipliers = np.append(multipliers, 1.5)
    if value12 == 1:
        multipliers = np.append(multipliers, 1.333)
    window.L5.configure(text=f"Damage Multiplier: {round((np.prod(multipliers) - 1) * 100, 1)} in %")
    # print(base_damage)
    window.L4.configure(text=f"{round(float(base_damage) * np.prod(multipliers), 1)}")

# def isWritten():
#     char = ""

# end defining functions

# define Checkbox variables
Cvar1 = IntVar()  # empowering buff
Cvar2 = IntVar()  # debuff
Cvar3 = IntVar()  # Font of Might
Cvar4 = IntVar()  # Focused Fury
Cvar5 = IntVar()  # Power of Rasputin
Cvar6 = IntVar()  # Bait and Switch
Cvar7 = IntVar()  # Mask of Bakris
Cvar8 = IntVar()  # Firing Line
Cvar9 = IntVar()  # Frenzy
Cvar10 = IntVar()  # Vorpal Weapon
Cvar11 = IntVar()  # multi kill clip
Cvar12 = IntVar()  # swashbuckler

# root.resizable(False, False)
window = Window(root)

root.mainloop()

################ TODO ###############################################
# 1. get the base dmg from a database when i enter name
# 2. or make a dropdown menu for name and have the dmg mapped to it
# 3. make different empowering buffs
# 4. make different debuffs
# 5. align the checkboxes to be in line with one another
# 6. remember: make branch for each development aspect!
######################################################################
