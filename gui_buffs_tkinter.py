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

        # --- section 0
        self.section0 = Frame(self.Main)

        self.L0 = Label(self.section0, text="WEAPON SPECS")
        self.L0.pack(padx=4, pady=4)

        # --- subsection 0_1
        self.section0_1 = Frame(self.section0)

        self.L1 = Label(self.section0_1, text="Name")
        self.L1.pack(padx=4, pady=4)

        self.M0 = OptionMenu(self.section0_1, Svar0, *wp)
        self.M0.pack(padx=4, pady=4)

        self.L2 = Label(self.section0_1, text = "Base Damage (Single Bullet)")
        self.L2.pack(padx=4, pady=4)

        self.L3 = Label(self.section0_1, text = f"0")
        self.L3.pack(padx=4, pady=4)

        self.L4 = Label(self.section0_1, text = "Amplified Damage")
        self.L4.pack(padx=4, pady=4)

        self.L5 = Label(self.section0_1, text = f"0")
        self.L5.pack(padx=4, pady=4)

        self.Button = Button(self.section0_1, text="Select Weapon", command=Select_Weapon)
        self.Button.pack(padx=4, pady=4)

        self.L6 = Label(self.section0_1, text = f"Damage Multiplier: {round((np.prod(multiplier) - 1) * 100, 1)} in %")  # this needs to be updated
        self.L6.pack(padx=4, pady=4)

        self.section0_1.pack(padx=4, pady=4)
        # --- subsection 0_1

        self.section0.pack(padx=4, pady=4, expand=True, fill=X, side=LEFT)
        # --- section 0

        # --- section 1
        self.section1 = Frame(self.Main)

        self.L7 = Label(self.section1, text="EMPOWERING BUFFS")
        self.L7.pack(padx=4, pady=4)

        self.R0 = Radiobutton(self.section1, text="No Empowering Buff", variable = Rvar0, value = 0, command = isChecked)
        self.R0.pack(padx=4, pady=4)
        self.R1 = Radiobutton(self.section1, text="Lumina buff", variable = Rvar0, value = 1, command = isChecked)
        self.R1.pack(padx=4, pady=4)
        self.R2 = Radiobutton(self.section1, text="Well of Radiance", variable = Rvar0, value = 2, command = isChecked)
        self.R2.pack(padx=4, pady=4)
        self.R3 = Radiobutton(self.section1, text="Empowering Rift", variable = Rvar0, value = 3, command = isChecked)
        self.R3.pack(padx=4, pady=4)

        self.section1.pack(padx=4, pady=4, expand=True, fill=X, side=LEFT)
        # --- section 1

        # --- section 2
        self.section2 = Frame(self.Main)

        self.C0 = Checkbutton(self.section2, text = "Font of Might", variable = Cvar2, command = isChecked)
        self.C0.pack(padx=4, pady=4)
        self.C1 = Checkbutton(self.section2, text = "Focused Fury", variable = Cvar3, command = isChecked)
        self.C1.pack(padx=4, pady=4)
        self.C2 = Checkbutton(self.section2, text = "Power of Rasputin", variable = Cvar4, command = isChecked)
        self.C2.pack(padx=4, pady=4)
        self.C3 = Checkbutton(self.section2, text = "Bait and Switch", variable = Cvar5, command = isChecked)
        self.C3.pack(padx=4, pady=4)
        self.C4 = Checkbutton(self.section2, text = "Mask of Bakris", variable = Cvar6, command = isChecked)
        self.C4.pack(padx=4, pady=4)
        self.C5 = Checkbutton(self.section2, text = "Firing Line", variable = Cvar7, command = isChecked)
        self.C5.pack(padx=4, pady=4)
        self.C6 = Checkbutton(self.section2, text = "Frenzy", variable = Cvar8, command = isChecked)
        self.C6.pack(padx=4, pady=4)
        self.C7 = Checkbutton(self.section2, text = "Vorpal Weapon", variable = Cvar9, command = isChecked)
        self.C7.pack(padx=4, pady=4)
        self.C8 = Checkbutton(self.section2, text = "Multi Kill Clip", variable = Cvar10, command = isChecked)
        self.C8.pack(padx=4, pady=4)
        self.C9 = Checkbutton(self.section2, text = "Swashbuckler", variable = Cvar11, command = isChecked)
        self.C9.pack(padx=4, pady=4)

        self.section2.pack(padx=4, pady=4, expand=True, fill=X, side=LEFT)
        # --- section 2

        # --- section 3
        self.section3 = Frame(self.Main)

        self.L50 = Label(self.section3, text="DEBUFFS")
        self.L50.pack(padx=4, pady=4)

        self.R10 = Radiobutton(self.section3, text="No Debuff", variable = Rvar1, value = 0, command = isChecked)
        self.R10.pack(padx=4, pady=4)
        self.R11 = Radiobutton(self.section3, text="Weaken", variable = Rvar1, value = 1, command = isChecked)
        self.R11.pack(padx=4, pady=4)
        self.R12 = Radiobutton(self.section3, text="Full Debuff", variable = Rvar1, value = 2, command = isChecked)
        self.R12.pack(padx=4, pady=4)

        self.section3.pack(padx=4, pady=4, expand=True, fill=X, side=LEFT)
        # --- section 3

        self.Main.pack(padx=4, pady=4)
        # --- section Main

# Begin main part
root = Tk()

def isChecked():
    base_damage = window.L3.cget("text")
    multipliers = np.array([1])
    value0  = Rvar0.get()   # empowering buffs as Radiobutton (35% / 25% / 20%)
    value1  = Rvar1.get()   # debuff: 15% weaken or 30% debuff
    value2  = Cvar2.get()   # Font of Might: 25 %
    value3  = Cvar3.get()   # Focused Fury: 22 %
    value4  = Cvar4.get()   # Power of Rasputin: 10 %
    value5  = Cvar5.get()   # Bait and Switch: 35 %
    value6  = Cvar6.get()   # Mask of Bakris: 20 %
    value7  = Cvar7.get()   # Firing Line: 20 %
    value8  = Cvar8.get()   # Frenzy: 15 %
    value9  = Cvar9.get()   # Vorpal Weapon: for now 10 % (heavy weapons)
    value10 = Cvar10.get()  # Multi Kill Clip: for now max stacks = 50 %
    value11 = Cvar11.get()  # Swashbuckler: for now max stacks = 33.3 %
    if value0 == 0:
        multipliers = np.append(multipliers, 1)    # no empowering buff
    if value0 == 1:
        multipliers = np.append(multipliers, 1.35) # lumina
    if value0 == 2:
        multipliers = np.append(multipliers, 1.25) # well of radiance, bubble
    if value0 == 3:
        multipliers = np.append(multipliers, 1.2)  # empowering rift
    if value1 == 0:
        multipliers = np.append(multipliers, 1)    # no debuff
    if value1 == 1:
        multipliers = np.append(multipliers, 1.15) # weaken
    if value1 == 2:
        multipliers = np.append(multipliers, 1.3)  # debuff
    if value2 == 1:
        multipliers = np.append(multipliers, 1.25) # font of might
    if value3 == 1:
        multipliers = np.append(multipliers, 1.22) # focused fury
    if value4 == 1:
        multipliers = np.append(multipliers, 1.10) # power of rasputin
    if value5 == 1:
        multipliers = np.append(multipliers, 1.35) # bait and switch
    if value6 == 1:
        multipliers = np.append(multipliers, 1.20) # mask of bakris
    if value7 == 1:
        multipliers = np.append(multipliers, 1.20) # firing line
    if value8 == 1:
        multipliers = np.append(multipliers, 1.15) # frenzy
    if value9 == 1:
        multipliers = np.append(multipliers, 1.10) # vorpal heavy
    if value10 == 1:
        multipliers = np.append(multipliers, 1.5) # multi kill clip max
    if value11 == 1:
        multipliers = np.append(multipliers, 1.333) # swash max
    if Svar0.get() == "Stormchaser" or Svar0.get() == "Fire and Forget":
        window.L5.configure(text=f"{round(float(base_damage) * np.prod(multipliers), 1)} ({round(float(base_damage) * np.prod(multipliers)  * 3, 1)})")
    if Svar0.get() != "Stormchaser" and Svar0.get() != "Fire and Forget":
        window.L5.configure(text=f"{round(float(base_damage) * np.prod(multipliers), 1)}")
    window.L6.configure(text=f"Damage Multiplier: {round((np.prod(multipliers) - 1) * 100, 1)} in %")
    # print(base_damage)

def Select_Weapon():
    print("selected weapon: " + Svar0.get())

    if Svar0.get() == "Cataclysmic":
        window.L3.configure(text="56586")
    if Svar0.get() == "Stormchaser":
        window.L3.configure(text="27704")
    if Svar0.get() == "Fire and Forget":
        window.L3.configure(text="28258")
    if Svar0.get() == "Reed's Regret":
        window.L3.configure(text="123")
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
Cvar2 = IntVar()  # Font of Might
Cvar3 = IntVar()  # Focused Fury
Cvar4 = IntVar()  # Power of Rasputin
Cvar5 = IntVar()  # Bait and Switch
Cvar6 = IntVar()  # Mask of Bakris
Cvar7 = IntVar()  # Firing Line
Cvar8 = IntVar()  # Frenzy
Cvar9 = IntVar()  # Vorpal Weapon
Cvar10 = IntVar() # multi kill clip
Cvar11 = IntVar() # swashbuckler

# here: add ALL weapons for the dropdown menu
wp = ["Cataclysmic","Stormchaser","Fire and Forget","Reed's Regret"]
Svar0 = StringVar(root)
Svar0.set(wp[0])

# make Radiobutton for empowering buff and debuff options
Rvar0 = IntVar()
Rvar1 = IntVar()

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
