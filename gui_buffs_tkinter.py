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

        self.M0 = OptionMenu(self.section0_1, Svar0, *list(wp_attributes.keys()))
        self.M0.pack(padx=4, pady=4)

        self.L2 = Label(self.section0_1, text = "Base Damage (Single Bullet)")
        self.L2.pack(padx=4, pady=4)

        self.L3 = Label(self.section0_1, text = f"0")
        self.L3.pack(padx=4, pady=4)

        self.L4 = Label(self.section0_1, text = "DPS")
        self.L4.pack(padx=4, pady=4)

        self.L5 = Label(self.section0_1, text = f"0")
        self.L5.pack(padx=4, pady=4)

        self.L6 = Label(self.section0_1, text = "Amplified Damage")
        self.L6.pack(padx=4, pady=4)

        self.L7 = Label(self.section0_1, text = f"0")
        self.L7.pack(padx=4, pady=4)

        self.Button = Button(self.section0_1, text="Select Weapon", command=Select_Weapon)
        self.Button.pack(padx=4, pady=4)

        self.L8 = Label(self.section0_1, text = f"Damage Multiplier: {round((np.prod(multiplier) - 1) * 100, 1)} in %")  # this needs to be updated
        self.L8.pack(padx=4, pady=4)

        self.section0_1.pack(padx=4, pady=4)
        # --- subsection 0_1

        self.section0.pack(padx=4, pady=4, expand=True, fill=X, side=LEFT)
        # --- section 0

        # --- section 1
        self.section1 = Frame(self.Main)

        self.L9 = Label(self.section1, text="EMPOWERING BUFFS")
        self.L9.pack(padx=4, pady=4)

        self.R0 = Radiobutton(self.section1, text="No Empowering Buff", variable = Rvar0, value = 0, command = isChecked)
        self.R0.pack(padx=4, pady=4)
        self.R1 = Radiobutton(self.section1, text="Bannershield", variable = Rvar0, value = 1, command = isChecked)
        self.R1.pack(padx=4, pady=4)
        self.R2 = Radiobutton(self.section1, text="Lumina / Lucent Blade", variable = Rvar0, value = 2, command = isChecked)
        self.R2.pack(padx=4, pady=4)
        self.R3 = Radiobutton(self.section1, text="Well / Bubble", variable = Rvar0, value = 3, command = isChecked)
        self.R3.pack(padx=4, pady=4)
        self.R4 = Radiobutton(self.section1, text="Empowering Rift / Mantle of. B. H.", variable = Rvar0, value = 4, command = isChecked)
        self.R4.pack(padx=4, pady=4)

        self.section1.pack(padx=4, pady=4, expand=True, fill=X, side=LEFT)
        # --- section 1

        # --- section 2
        self.section2 = Frame(self.Main)

        self.L10 = Label(self.section1, text="WEAPON- AND MOD BUFFS")
        self.L10.pack(padx=4, pady=4)

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
        self.C10 = Checkbutton(self.section2, text = "High Impact Reserves", variable = Cvar12, command = isChecked)
        self.C10.pack(padx=4, pady=4)
        self.C11 = Checkbutton(self.section2, text = "Golden Tricorn x1", variable = Cvar13, command = isChecked)
        self.C11.pack(padx=4, pady=4)
        self.C12 = Checkbutton(self.section2, text = "Golden Tricorn x2", variable = Cvar14, command = isChecked)
        self.C12.pack(padx=4, pady=4)
        self.C13 = Checkbutton(self.section2, text = "Cluster Bombs", variable = Cvar15, command = isChecked)
        self.C13.pack(padx=4, pady=4)
        self.C14 = Checkbutton(self.section2, text = "Explosive Light (GL)", variable = Cvar16, command = isChecked)
        self.C14.pack(padx=4, pady=4)
        self.C15 = Checkbutton(self.section2, text = "Explosive Light (Rocket)", variable = Cvar17, command = isChecked)
        self.C15.pack(padx=4, pady=4)
        self.C16 = Checkbutton(self.section2, text = "Full Court", variable = Cvar18, command = isChecked)
        self.C16.pack(padx=4, pady=4)
        self.C17 = Checkbutton(self.section2, text = "Adagio", variable = Cvar19, command = isChecked)
        self.C17.pack(padx=4, pady=4)
        self.C18 = Checkbutton(self.section2, text = "Lasting Impression", variable = Cvar20, command = isChecked)
        self.C18.pack(padx=4, pady=4)

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
    value0  = Rvar0.get()
    value1  = Rvar1.get()
    value2  = Cvar2.get()
    value3  = Cvar3.get()
    value4  = Cvar4.get()
    value5  = Cvar5.get()
    value6  = Cvar6.get()
    value7  = Cvar7.get()
    value8  = Cvar8.get()
    value9  = Cvar9.get()
    value10 = Cvar10.get()
    value11 = Cvar11.get()
    value12 = Cvar12.get()
    value13 = Cvar13.get()
    value14 = Cvar14.get()
    value15 = Cvar15.get()
    value16 = Cvar16.get()
    value17 = Cvar17.get()
    value18 = Cvar18.get()
    value19 = Cvar19.get()
    value20 = Cvar20.get()

    if value0 == 0:
        multipliers = np.append(multipliers, 1)    # no empowering buff
    if value0 == 1:
        multipliers = np.append(multipliers, 1.40) # bannershield
    if value0 == 2:
        multipliers = np.append(multipliers, 1.35) # Lumina, lucent blade
    if value0 == 3:
        multipliers = np.append(multipliers, 1.25) # well of radiance, bubble
    if value0 == 4:
        multipliers = np.append(multipliers, 1.2)  # empowering buff
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
    if value12 == 1:
        multipliers = np.append(multipliers, 1.24) # High impact resevrs (take max for now at 24 %)
    if value13 == 1:
        multipliers = np.append(multipliers, 1.15) # Golden Tricorn x1
    if value14 == 1:
        multipliers = np.append(multipliers, 1.5) # Golden Tricorn x2
    if value15 == 1:
        multipliers = np.append(multipliers, 1.24) # Cluster bombs
    if value16 == 1:
        multipliers = np.append(multipliers, 1.44) # Explosive Light for GLs
    if value17 == 1:
        multipliers = np.append(multipliers, 1.25) # Explosive Lightfor Rockets
    if value18 == 1:
        multipliers = np.append(multipliers, 1.25) # Full Court (max = 25 %)
    if value19 == 1:
        multipliers = np.append(multipliers, 1.3) # Adagio: +30 % dmg, -20 % fire rate
    if value20 == 1:
        multipliers = np.append(multipliers, 1.19) # lasting impression: + 30 % explosion dmg -> 19% overall
    if Svar0.get() == "Stormchaser" or Svar0.get() == "Fire and Forget":
        window.L7.configure(text=f"{round(float(base_damage) * np.prod(multipliers), 1)} ({round(float(base_damage) * np.prod(multipliers)  * 3, 1)})")
    if Svar0.get() != "Stormchaser" and Svar0.get() != "Fire and Forget":
        window.L7.configure(text=f"{round(float(base_damage) * np.prod(multipliers), 1)}")
    window.L8.configure(text=f"Damage Multiplier: {round((np.prod(multipliers) - 1) * 100, 1)} in %")

    Calculate_DPS()

def Calculate_DPS():
    amp_damage = window.L7.cget("text")
    print("momentary weapon:", Svar0.get())
    print("current charge time:", wp_attributes[Svar0.get()] * 1e-3, "second(s)")
    print("time to release shot roughly", 0.1, "second(s)")
    print("rate of fire =", wp_attributes[Svar0.get()] * 1e-3 + 0.1, "Shots/second")
    window.L5.configure(text=f"{round(float(amp_damage) / (wp_attributes[Svar0.get()] * 1e-3 + 0.1), 1)} DPS")


def Select_Weapon():
    undo()
    # print("selected weapon: " + Svar0.get())
    ### --- python version older than 3.10 (don't know switch cases)
    # if Svar0.get() == "Cataclysmic":
    #     window.L3.configure(text="56586")
    # if Svar0.get() == "Stormchaser":
    #     window.L3.configure(text="27704")
    # if Svar0.get() == "Fire and Forget":
    #     window.L3.configure(text="28258")
    # if Svar0.get() == "Reed's Regret":
    #     window.L3.configure(text="123")

    # damage numbers are for minibosses
    match Svar0.get():
        case "Cataclysmic":
            window.L3.configure(text="56586")
            # print("which case of svar0: ", Svar0.get(), wp_attributes[Svar0.get()], float(base_damage))
            cataclysmic_perks()
        case "Stormchaser":
            window.L3.configure(text="27704") # times 3
            stormchaser_perks()
        case "Fire and Forget":
            window.L3.configure(text="28258") # times 3
            fire_and_forget_perks()
        case "Reed's Regret":
            window.L3.configure(text="57822")
            reeds_regret_perks()
        case "Sailspy Pitchglass":
            window.L3.configure(text="58356")
            saispy_pitchglass_perks()
        case "Taipan 4FR":
            window.L3.configure(text="58356")
            taipan_perks()
        case "Threaded Needle":
            window.L3.configure(text="58356")
            threaded_needle_perks()
        case "The Hothead":
            window.L3.configure(text="98208")
            hothead_perks()
        case "Blowout":
            window.L3.configure(text="98209")
            blowout_perks()
        case "Roar Of The Bear":
            window.L3.configure(text="84309")
            roar_of_the_bear_perks()
        case "Hezen Vengeance":
            window.L3.configure(text="98209")
            hezen_vengeance_perks()
        case "Code Duello":
            window.L3.configure(text="84309")
            code_duello_perks()
        case "RedHerring":
            window.L3.configure(text="1")
            red_herring_perks()
        case "Royal Entry":
            window.L3.configure(text="80352")
            royal_entry_perks()
        case "Bump In The Night":
            window.L3.configure(text="98209")
            bump_in_the_night_perks()
        case "Palmyra-B":
            window.L3.configure(text="80352")
            palmyra_perks()
        case "Wendigo GL3":
            window.L3.configure(text="1")
            wendigo_perks()
        case "Interference VI":
            window.L3.configure(text="39382") # min = 39382, max = 46157
            interference_perks()
        case "Tarnation":
            window.L3.configure(text="31880")
            tarnation_impact()
        case "Cry Mutiny":
            window.L3.configure(text="35411")
            cry_mutiny_perks()
        case "Typhon GL5":
            window.L3.configure(text="39155")
            typhon_perks()
    isChecked()
    # test_color()

def undo():
    # ich habe kein bock mehr jetzt, brute force
    # set every checkbutton to black
    # what is the elegant way???
    window.C0.config(fg="black")
    window.C1.config(fg="black")
    window.C2.config(fg="black")
    window.C3.config(fg="black")
    window.C4.config(fg="black")
    window.C5.config(fg="black")
    window.C6.config(fg="black")
    window.C7.config(fg="black")
    window.C8.config(fg="black")
    window.C9.config(fg="black")
    window.C10.config(fg="black")
    window.C11.config(fg="black")
    window.C12.config(fg="black")
    window.C13.config(fg="black")
    window.C14.config(fg="black")
    window.C15.config(fg="black")
    window.C16.config(fg="black")
    window.C17.config(fg="black")
    window.C18.config(fg="black")

def cataclysmic_perks():
    window.C1.config(fg="green")
    window.C3.config(fg="green")
    window.C10.config(fg="green")

def stormchaser_perks():
    window.C5.config(fg="green")
    window.C6.config(fg="green")
    window.C7.config(fg="green")

def fire_and_forget_perks():
    window.C1.config(fg="green")
    window.C6.config(fg="green")
    window.C7.config(fg="green")
    window.C10.config(fg="green")

def reeds_regret_perks():
    window.C1.config(fg="green")
    window.C5.config(fg="green")
    window.C7.config(fg="green")

def saispy_pitchglass_perks():
    window.C1.config(fg="green")
    window.C6.config(fg="green")
    window.C7.config(fg="green")
    window.C8.config(fg="green")
    window.C9.config(fg="green")

def taipan_perks():
    window.C1.config(fg="green")
    window.C5.config(fg="green")
    window.C6.config(fg="green")

def threaded_needle_perks():
    window.C6.config(fg="green")
    window.C7.config(fg="green")
    window.C8.config(fg="green")

def hothead_perks():
    window.C7.config(fg="green")
    window.C15.config(fg="green")
    window.C18.config(fg="green")

def blowout_perks():
    window.C6.config(fg="green")
    window.C7.config(fg="green")
    window.C8.config(fg="green")
    window.C9.config(fg="green")
    window.C11.config(fg="green")
    window.C12.config(fg="green")
    window.C13.config(fg="green")
    window.C15.config(fg="green")
    window.C18.config(fg="green")

def roar_of_the_bear_perks():
    window.C7.config(fg="green")
    window.C13.config(fg="green")
    window.C18.config(fg="green")

def hezen_vengeance_perks():
    window.C7.config(fg="green")
    window.C13.config(fg="green")
    window.C18.config(fg="green")

def red_herring_perks():
    window.C6.config(fg="green")
    window.C11.config(fg="green")
    window.C12.config(fg="green")
    window.C18.config(fg="green")

def royal_entry_perks():
    window.C13.config(fg="green")
    window.C18.config(fg="green")

def bump_in_the_night_perks():
    window.C6.config(fg="green")
    window.C7.config(fg="green")

def palmyra_perks():
    window.C6.config(fg="green")
    window.C15.config(fg="green")
    window.C18.config(fg="green")

def wendigo_perks():
    window.C6.config(fg="green")
    window.C11.config(fg="green")
    window.C12.config(fg="green")
    window.C14.config(fg="green")
    window.C16.config(fg="green")

def interference_perks():
    window.C9.config(fg="green")
    window.C16.config(fg="green")

def cry_mutiny_perks():
    window.C7.config(fg="green")
    window.C9.config(fg="green")

def typhon_perks():
    window.C15.config(fg="green")
    window.C6.config(fg="green")

def code_duello_perks():
    window.C6.config(fg="green")
    window.C13.config(fg="green")
    window.C18.config(fg="green")

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
Cvar12 = IntVar() # High Impact Reserves
Cvar13 = IntVar() # Golden Tricorn x1
Cvar14 = IntVar() # Golden Tricorn x2
Cvar15 = IntVar() # Cluster bombs
Cvar16 = IntVar() # Explosive Light (GL)
Cvar17 = IntVar() # Explosive Light (Rockets)
Cvar18 = IntVar() # Full Court
Cvar19 = IntVar() # Adagio
Cvar20 = IntVar() # lasting impression
# here: add ALL weapons for the dropdown menu
wp_attributes = {"Cataclysmic": 533,
    "Stormchaser": 533,
    "Fire and Forget": 533,
    "Reed's Regret": 533,
    "Sailspy Pitchglass": 533,
    "Taipan 4FR": 533,
    "Threaded Needle": 533,
    "The Hothead": 533,
    "Blowout": 533,
    "Roar Of The Bear": 533,
    "Hezen Vengeance": 533,
    "Code Duello": 533,
    "RedHerring": 533,
    "Royal Entry": 533,
    "Bump In The Night": 533,
    "Palmyra-B": 533,
    "Wendigo GL3": 533,
    "Interference VI": 533,
    "Tarnation": 533,
    "Cry Mutiny": 533,
    "Typhon GL5": 533,
    }

Svar0 = StringVar(root)
Svar0.set(list(wp_attributes.keys())[0])

# make Radiobutton for empowering buff and debuff options
Rvar0 = IntVar()
Rvar1 = IntVar()

window = Window(root)

root.mainloop()

################ TODO ###############################################
# for empowering buffs: group them by buff% for each layer, like:
# 40 %: banner shield
# 35 %: lumina, lucent blade
# 25 %: well of radiance, weapons of light, radiant
# 20 %: empowering rift, High Energy Fire, mantle of battle harmony
#
# Add more weapons buffs:
# Golden Tricorn and Explosive light can be done as dropdown, or Radiobutton with 3 options (x0, x1, x2)
# scale sections to be 25% of page
#
# whenever i add a new perK, do the followinf steps
# 1. add new Cvar<new_value> = IntVar()
# 2. add it to the undo() method to be colored black
# 3. add a Radiobutton or Checkbutton for the perk
# 4. add it to isChecked() method as Cvar(...).get()
# 5. append it to multipliers if value == 1
#
#
# whener i add a new weapon do the following steps:
# 1. add it to "wp" list
# 2. make a function which colors its perks
# 3. add it to Select_Weapon() method
######################################################################
