import numpy as np
import matplotlib.pyplot as plt
import re
# import tkinter as tk
# import tkinter as ttk
from tkinter import *
#import mysql.connector

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

        self.M1 = OptionMenu(self.section1_1, Svar1, *wp)
        self.M1.pack(padx=4, pady=4)

        self.L2 = Label(self.section1_1, text = "Base Damage (single bullet)")
        self.L2.pack(padx=4, pady=4)

        self.L7 = Label(self.section1_1, text = f"0")
        self.L7.pack(padx=4, pady=4)

        self.L3 = Label(self.section1_1, text = "Amplified Damage")
        self.L3.pack(padx=4, pady=4)

        self.L4 = Label(self.section1_1, text = f"0")
        self.L4.pack(padx=4, pady=4)

        self.Button = Button(self.section1_1, text="select weapon", command=Select_Weapon)
        self.Button.pack(padx=4, pady=4)

        self.L5 = Label(self.section1_1, text = f"Damage Multiplier: {round((np.prod(multiplier) - 1) * 100, 1)} in %")  # this needs to be updated
        self.L5.pack(padx=4, pady=4)

        self.section1_1.pack(padx=4, pady=4, side=LEFT)
        ## ---> sub section1_1

        ## ---> sub section1_2
        self.section1_2 = Frame(self.section1)

        self.L6 = Label(self.section1, text="Buffs and Debuffs")
        self.L6.pack(padx=4, pady=4)

        ## ---> sub section1_2_1
        self.section1_2_1 = Frame(self.section1_2)
        self.R1 = Radiobutton(self.section1_2_1, text="Lumina buff", variable = Rvar1, value = 0, command = isChecked)
        self.R1.pack(padx=4, pady=4, side=LEFT)
        self.R1 = Radiobutton(self.section1_2_1, text="Well of Radiance", variable = Rvar1, value = 1, command = isChecked)
        self.R1.pack(padx=4, pady=4, side=LEFT)
        self.R1 = Radiobutton(self.section1_2_1, text="Empowering Rift", variable = Rvar1, value = 2, command = isChecked)
        self.R1.pack(padx=4, pady=4, side=LEFT)
        self.section1_2_1.pack(padx=4, pady=4)
        ## ---> sub section1_2_1

        ## ---> sub section1_2_2
        self.section1_2_2 = Frame(self.section1_2)
        self.R1 = Radiobutton(self.section1_2_2, text="Weaken", variable = Rvar2, value = 0, command = isChecked)
        self.R1.pack(padx=4, pady=4, side=LEFT)
        self.R1 = Radiobutton(self.section1_2_2, text="Full Debuff", variable = Rvar2, value = 1, command = isChecked)
        self.R1.pack(padx=4, pady=4, side=LEFT)
        self.section1_2_2.pack(padx=4, pady=4)
        ## ---> sub section1_2_2

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
        self.section1.pack(padx = 5, pady = 5, expand = True, fill=X)
        # --- section1

        # --- section2
        self.section2 = Frame(self.Main)


        self.section2.pack(padx=4, pady=4, expand=True, fill=X)
        # section2

        self.Main.pack(padx=4, pady=4)  # ---> pack main up (basically closes it)

# Begin main part
root = Tk()

def isChecked():
    base_damage = window.L7.cget("text")
    multipliers = np.array([1])
    value0  = Rvar1.get()   # empowering buffs as Radiobutton (35% / 25% / 20%)
    value2  = Rvar2.get()   # debuff: 15% weaken or 30% debuff
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
    if value0 == 0:
        multipliers = np.append(multipliers, 1.35) # lumina
    if value0 == 1:
        multipliers = np.append(multipliers, 1.25) # well of radiance, bubble
    if value0 == 2:
        multipliers = np.append(multipliers, 1.2)  # empowering rift
    if value2 == 0:
        multipliers = np.append(multipliers, 1.15) # weaken
    if value2 == 1:
        multipliers = np.append(multipliers, 1.3)  # debuff
    if value3 == 1:
        multipliers = np.append(multipliers, 1.25) # font of might
    if value4 == 1:
        multipliers = np.append(multipliers, 1.22) # focused fury
    if value5 == 1:
        multipliers = np.append(multipliers, 1.10) # power of rasputin
    if value6 == 1:
        multipliers = np.append(multipliers, 1.35) # bait and switch
    if value7 == 1:
        multipliers = np.append(multipliers, 1.20) # mask of bakris
    if value8 == 1:
        multipliers = np.append(multipliers, 1.20) # firing line
    if value9 == 1:
        multipliers = np.append(multipliers, 1.15) # frenzy
    if value10 == 1:
        multipliers = np.append(multipliers, 1.10) # vorpal heavy
    if value11 == 1:
        multipliers = np.append(multipliers, 1.5) # multi kill clip max
    if value12 == 1:
        multipliers = np.append(multipliers, 1.333) # swash max
    if Svar1.get() == "Stormchaser" or Svar1.get() == "Fire and Forget":
        window.L4.configure(text=f"{round(float(base_damage) * np.prod(multipliers), 1)} ({round(float(base_damage) * np.prod(multipliers)  * 3, 1)})")
    if Svar1.get() != "Stormchaser" and Svar1.get() != "Fire and Forget":
        window.L4.configure(text=f"{round(float(base_damage) * np.prod(multipliers), 1)}")
    window.L5.configure(text=f"Damage Multiplier: {round((np.prod(multipliers) - 1) * 100, 1)} in %")
    # print(base_damage)

def Select_Weapon():
    print("selected weapon: " + Svar1.get())

    if Svar1.get() == "Cataclysmic":
        window.L7.configure(text="56586")
    if Svar1.get() == "Stormchaser":
        window.L7.configure(text="27704")
    if Svar1.get() == "Fire and Forget":
        window.L7.configure(text="28258")
    if Svar1.get() == "Reed's Regret":
        window.L7.configure(text="123")
#    match Svar1.get():
#        case "Cataclysmic":
#            window.L7.configure(text="56586")
#        case "Stormchaser":
#            window.L7.configure(text="27704") # times 3
#        case "Fire and Forget":
#            window.L7.configure(text="28258") # times 3
#        case "Reed's Regret":
#            window.L7.configure(text="123")
    isChecked()

# define Checkbox variables
Cvar3 = IntVar()  # Font of Might
Cvar4 = IntVar()  # Focused Fury
Cvar5 = IntVar()  # Power of Rasputin
Cvar6 = IntVar()  # Bait and Switch
Cvar7 = IntVar()  # Mask of Bakris
Cvar8 = IntVar()  # Firing Line
Cvar9 = IntVar()  # Frenzy
Cvar10 = IntVar() # Vorpal Weapon
Cvar11 = IntVar() # multi kill clip
Cvar12 = IntVar() # swashbuckler

# here: add ALL weapons for the dropdown menu
wp = ["Cataclysmic","Stormchaser","Fire and Forget","Reed's Regret"]
Svar1 = StringVar(root)
Svar1.set(wp[0])

# make Radiobutton for empowering buff and debuff options
Rvar1 = IntVar()
Rvar2 = IntVar()

window = Window(root)

root.mainloop()

################ TODO ###############################################
# 1. get the base dmg from a database when i enter name
# 2. or make a dropdown menu for name and have the dmg mapped to it (done)
# 3. make different empowering buffs (done)
# 4. make different debuffs
# 5. align the checkboxes to be in line with one another
# 6. remember: make branch for each development aspect! (jep remembered)
######################################################################
