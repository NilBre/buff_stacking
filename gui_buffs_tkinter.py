import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
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

        # --- subsection 0_2
        # self.section0_2 = Frame(self.section0_1)
        # self.section0_2.pack(padx=4, pady=4)
        # --- subsecton 0_2

        # self.L5 = Label(self.section0_1, text = f"0")
        # self.L5.pack(padx=4, pady=4)

        self.L6 = Label(self.section0_1, text = "Amplified Damage")
        self.L6.pack(padx=4, pady=4)

        # --- subsection0_1_1
        self.section0_1_1 = Frame(self.section0_1)

        # L7 is for every weapon, L7_1 for 3 burst linear fusions
        self.L7 = Label(self.section0_1_1, text = f"0")
        self.L7.pack(padx=4, pady=4, side=LEFT)

        self.L7_1 = Label(self.section0_1_1, text = f"0")
        self.L7_1.pack(padx=4, pady=4, side=LEFT)

        self.section0_1_1.pack(padx=4, pady=4)
        # --- subsection0_1_1

        self.L8 = Label(self.section0_1, text = f"Damage Multiplier: {round((np.prod(multiplier) - 1) * 100, 1)} in %")  # this needs to be updated
        self.L8.pack(padx=4, pady=4)

        self.Button = Button(self.section0_1, text="Select Weapon", command=Select_Weapon)
        self.Button.pack(padx=4, pady=4)

        self.section0_1.pack(padx=4, pady=4)
        # --- subsection 0_1
        self.section0.pack(padx=4, pady=4, expand=True, fill=X, side=LEFT)
        # --- section 0

        # --- section 1
        self.section1 = Frame(self.Main)

        self.L11 = Label(self.section1, text="DPS VALUES")
        self.L11.pack(padx=4, pady=4)

        self.L12 = Label(self.section1, text="Linear Fusion DPS")
        self.L12.pack(padx=4, pady=4)

        self.S0 = Scale(self.section1, from_=0, to_=3, orient=HORIZONTAL)
        self.S0.pack(padx=4, pady=4)

        # --- subsection1_1
        self.section1_1 = Frame(self.section1)

        self.L13 = Label(self.section1_1, text="0")
        self.L13.pack(padx=4, pady=4)

        self.L13_1 = Label(self.section1_1, text="0")
        self.L13_1.pack(padx=4, pady=4)

        self.section1_1.pack(padx=4, pady=4)
        # --- subsection1_1

        self.L14 = Label(self.section1, text="Rocketlauncher DPS")
        self.L14.pack(padx=4, pady=4)

        self.S1 = Scale(self.section1, from_=0, to_=7, orient=HORIZONTAL)
        self.S1.pack(padx=4, pady=4)

        self.L15 = Label(self.section1, text="0")
        self.L15.pack(padx=4, pady=4)

        self.L16 = Label(self.section1, text="Grenadelauncher DPS")
        self.L16.pack(padx=4, pady=4)

        self.S2 = Scale(self.section1, from_=0, to_=3, orient=HORIZONTAL)
        self.S2.pack(padx=4, pady=4)

        self.L17 = Label(self.section1, text="0")
        self.L17.pack(padx=4, pady=4)

        self.section1.pack(padx=4, pady=4, expand=True, fill=X, side=LEFT)
        # --- section 1

        # --- section 2
        self.section2 = Frame(self.Main)

        self.L10 = Label(self.section2, text="WEAPON- AND MOD BUFFS")
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
        # -- subsection3_1
        self.section3_1 = Frame(self.section3)

        self.L9 = Label(self.section3_1, text="EMPOWERING BUFFS")
        self.L9.pack(padx=4, pady=4)

        self.R0 = Radiobutton(self.section3_1, text="No Empowering Buff", variable = Rvar0, value = 0, command = isChecked)
        self.R0.pack(padx=4, pady=4)
        self.R1 = Radiobutton(self.section3_1, text="Bannershield", variable = Rvar0, value = 1, command = isChecked)
        self.R1.pack(padx=4, pady=4)
        self.R2 = Radiobutton(self.section3_1, text="Lumina / Lucent Blade", variable = Rvar0, value = 2, command = isChecked)
        self.R2.pack(padx=4, pady=4)
        self.R3 = Radiobutton(self.section3_1, text="Well / Bubble", variable = Rvar0, value = 3, command = isChecked)
        self.R3.pack(padx=4, pady=4)
        self.R4 = Radiobutton(self.section3_1, text="Empowering Rift / Mantle of. B. H.", variable = Rvar0, value = 4, command = isChecked)
        self.R4.pack(padx=4, pady=4)

        self.section3_1.pack(padx=4, pady=4)
        # --- subsection3_1

        # --- subsection3_2
        self.section3_2 = Frame(self.section3)

        self.L50 = Label(self.section3_2, text="DEBUFFS")
        self.L50.pack(padx=4, pady=4)

        self.R10 = Radiobutton(self.section3_2, text="No Debuff", variable = Rvar1, value = 0, command = isChecked)
        self.R10.pack(padx=4, pady=4)
        self.R11 = Radiobutton(self.section3_2, text="Weaken", variable = Rvar1, value = 1, command = isChecked)
        self.R11.pack(padx=4, pady=4)
        self.R12 = Radiobutton(self.section3_2, text="Full Debuff", variable = Rvar1, value = 2, command = isChecked)
        self.R12.pack(padx=4, pady=4)

        self.section3_2.pack(padx=4, pady=4)
        # subsection3_2


        self.section3.pack(padx=4, pady=4, expand=True, fill=X, side=LEFT)
        # --- section 3

        # some plotting stuff
        self.canvas = FigureCanvasTkAgg(fig, master=self.Main)
        self.canvas.get_tk_widget().pack()

        self.B10 = Button(self.Main, text="plot graph", command=plot)
        self.B10.pack(pady=4)

        self.Main.pack(padx=4, pady=4)
        # --- section Main

def plot():
    # this ist just for an example
    # plqn: draw dps over several magazines/bullets/rockets/...
    # ax.clear() # removes previous data points
    if Svar0.get() in LFRs:
        if Svar0.get() != "Stormchaser" and Svar0.get() != "Fire and Forget":
            single_bullet = window.L13.cget("text")
            burst = 0
        if Svar0.get() == "Stormchaser" or Svar0.get() == "Fire and Forget":
            single_bullet = window.L13.cget("text")
            burst = window.L13_1.cget("text")
    if Svar0.get() in Rockets:
        dps = window.L15.cget("text")
    if Svar0.get() in GLs:
        dps = get_GL_dps_full()[1:]
    print(dps)
    x = np.linspace(0, len(dps), len(dps))
    y = dps
    ax.plot(x, y, label=f"{Svar0.get()}")
    plt.xlabel("magazine number")
    plt.ylabel("DPS")
    plt.legend()
    plt.grid()
    window.canvas.draw()

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
        window.L7.configure(text=f"{round(wp_attributes[Svar0.get()]['base_dmg'] * np.prod(multipliers), 1)}")
        window.L7_1.configure(text=f"{round(wp_attributes[Svar0.get()]['base_dmg'] * np.prod(multipliers) * 3, 1)}")
    if Svar0.get() != "Stormchaser" and Svar0.get() != "Fire and Forget":
        window.L7.configure(text=f"{round(wp_attributes[Svar0.get()]['base_dmg'] * np.prod(multipliers), 1)}")
        window.L7_1.configure(text=f"")
    window.L8.configure(text=f"Damage Multiplier: {round((np.prod(multipliers) - 1) * 100, 1)} in %")
    Calculate_DPS()

def Calculate_DPS():
    # amp_damage = window.L7.cget("text")
    # amp_damage_3burst = window.L7_1.cget("text")
    print("momentary weapon:", Svar0.get())
    if Svar0.get() in LFRs:
        if Svar0.get() != "Stormchaser" and Svar0.get() != "Fire and Forget":
            window.L13.configure(text=f"{LFR_dps()[0]} DPS for {window.S0.get()} mag(s)")
            window.L13_1.configure(text=f"")
        if Svar0.get() == "Stormchaser" or Svar0.get() == "Fire and Forget":
            window.L13.configure(text=f"{LFR_dps()[0]} DPS for {window.S0.get()} mag(s)")
            window.L13_1.configure(text=f"{LFR_dps()[1]} DPS for {window.S0.get()} mag(s)")
    if Svar0.get() in Rockets:
        window.L15.configure(text=f"{rocket_dps()} DPS for {window.S1.get()} rockets")
    if Svar0.get() in GLs:
        window.L17.configure(text=f"{GL_dps()} DPS for {window.S2.get()} magazines")

def LFR_dps():
    base_LFR_dmg = window.L7.cget("text")
    base_LFR_dmg_3burst = window.L7_1.cget("text")
    if window.L7_1.cget("text") == "":
        base_LFR_dmg_3burst = 0
    else:
        base_LFR_dmg_3burst = window.L7_1.cget("text")
    if window.S0.get() == 0:
        return 0, 0
    else:
        return round(window.S0.get() * wp_attributes[Svar0.get()]['mag_size'] * float(base_LFR_dmg) / (window.S0.get() * wp_attributes[Svar0.get()]['mag_size'] * ((wp_attributes[Svar0.get()]['charge_time'] * 1e-3) + 0.44) + (window.S0.get() - 1) * wp_attributes[Svar0.get()]['reload_speed']), 1), round(window.S0.get() * wp_attributes[Svar0.get()]['mag_size'] * float(base_LFR_dmg_3burst) / (window.S0.get() * wp_attributes[Svar0.get()]['mag_size'] * ((wp_attributes[Svar0.get()]['charge_time'] * 1e-3) + 0.44) + (window.S0.get() - 1) * wp_attributes[Svar0.get()]['reload_speed']), 1)

def rocket_dps():
    base_rocket_dmg = window.L7.cget("text")
    if window.S1.get() == 0:
        return 0
    elif window.S1.get() == 1:
        return round(float(base_rocket_dmg), 1)
    else:
        return round((window.S1.get() * float(base_rocket_dmg)) / ((window.S1.get() - 1) * wp_attributes[Svar0.get()]['reload_speed']), 1)

def GL_dps():
    base_GL_dmg = window.L7.cget("text")
    time_for_mag = wp_attributes[Svar0.get()]['mag_size'] / (wp_attributes[Svar0.get()]['rpm'] / 60)
    if window.S2.get() == 0:
        return 0
    else:
        return round((window.S2.get() * float(base_GL_dmg) * wp_attributes[Svar0.get()]['mag_size']) / (window.S2.get() * time_for_mag + (window.S2.get() - 1) * wp_attributes[Svar0.get()]['reload_speed']), 1)

# -----------------------
# functions for each weapon type that returns array
# of dps numbers for number of rockets/magazines
def get_GL_dps_full():
    # shape = [n_mags] list of length round(reserves/magsize), n_mags = dps value for each mag
    dps_vals = []
    base_GL_dmg = window.L7.cget("text")
    time_for_mag = wp_attributes[Svar0.get()]['mag_size'] / (wp_attributes[Svar0.get()]['rpm'] / 60)
    total_mags = round(wp_attributes[Svar0.get()]['reserves'] / wp_attributes[Svar0.get()]['mag_size'])
    # print(f"selected GL: {Svar0.get()}")
    for i in range(total_mags):
        if i == 0:
            dps_vals.append(0)
        else:
            dps_vals.append(round((i * float(base_GL_dmg) * wp_attributes[Svar0.get()]['mag_size']) / (i * time_for_mag + (i - 1) * wp_attributes[Svar0.get()]['reload_speed']), 1))
    return dps_vals

# ------------------------


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
            window.L3.configure(text=f"{wp_attributes[Svar0.get()]['base_dmg']}")
            cataclysmic_perks()
        case "Stormchaser":
            window.L3.configure(text=f"{wp_attributes[Svar0.get()]['base_dmg']}") # times 3
            stormchaser_perks()
        case "Fire and Forget":
            window.L3.configure(text=f"{wp_attributes[Svar0.get()]['base_dmg']}") # times 3
            fire_and_forget_perks()
        case "Reed's Regret":
            window.L3.configure(text=f"{wp_attributes[Svar0.get()]['base_dmg']}")
            reeds_regret_perks()
        case "Sailspy Pitchglass":
            window.L3.configure(text=f"{wp_attributes[Svar0.get()]['base_dmg']}")
            saispy_pitchglass_perks()
        case "Taipan 4FR":
            window.L3.configure(text=f"{wp_attributes[Svar0.get()]['base_dmg']}")
            taipan_perks()
        case "Threaded Needle":
            window.L3.configure(text=f"{wp_attributes[Svar0.get()]['base_dmg']}")
            threaded_needle_perks()
        case "The Hothead":
            window.L3.configure(text=f"{wp_attributes[Svar0.get()]['base_dmg']}")
            hothead_perks()
        case "Blowout":
            window.L3.configure(text=f"{wp_attributes[Svar0.get()]['base_dmg']}")
            blowout_perks()
        case "Roar Of The Bear":
            window.L3.configure(text=f"{wp_attributes[Svar0.get()]['base_dmg']}")
            roar_of_the_bear_perks()
        case "Hezen Vengeance":
            window.L3.configure(text=f"{wp_attributes[Svar0.get()]['base_dmg']}")
            hezen_vengeance_perks()
        case "Code Duello":
            window.L3.configure(text=f"{wp_attributes[Svar0.get()]['base_dmg']}")
            code_duello_perks()
        case "RedHerring":
            window.L3.configure(text=f"{wp_attributes[Svar0.get()]['base_dmg']}")
            red_herring_perks()
        case "Royal Entry":
            window.L3.configure(text=f"{wp_attributes[Svar0.get()]['base_dmg']}")
            royal_entry_perks()
        case "Bump In The Night":
            window.L3.configure(text=f"{wp_attributes[Svar0.get()]['base_dmg']}")
            bump_in_the_night_perks()
        case "Palmyra-B":
            window.L3.configure(text=f"{wp_attributes[Svar0.get()]['base_dmg']}")
            palmyra_perks()
        case "Wendigo GL3":
            window.L3.configure(text=f"{wp_attributes[Svar0.get()]['base_dmg']}")
            wendigo_perks()
        case "Interference VI":
            window.L3.configure(text=f"{wp_attributes[Svar0.get()]['base_dmg']}") # min = 39382, max = 46157
            interference_perks()
        case "Tarnation":
            window.L3.configure(text=f"{wp_attributes[Svar0.get()]['base_dmg']}")
            # tarnation_impact()
        case "Cry Mutiny":
            window.L3.configure(text=f"{wp_attributes[Svar0.get()]['base_dmg']}")
            cry_mutiny_perks()
        case "Typhon GL5":
            window.L3.configure(text=f"{wp_attributes[Svar0.get()]['base_dmg']}")
            typhon_perks()
    isChecked()
    # test_color()

def undo():
    # uncheck all checkboxes for the user
    # Cvar2.set(0)
    # Cvar3.set(0)
    # Cvar4.set(0)
    # Cvar5.set(0)
    # Cvar6.set(0)
    # Cvar7.set(0)
    # Cvar8.set(0)
    # Cvar9.set(0)
    # Cvar10.set(0)
    # Cvar11.set(0)
    # Cvar12.set(0)
    # Cvar13.set(0)
    # Cvar14.set(0)
    # Cvar15.set(0)
    # Cvar16.set(0)
    # Cvar17.set(0)
    # Cvar18.set(0)
    # Cvar19.set(0)
    # Cvar20.set(0)
    # change all window colors
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

# Begin main part
root = Tk()

fig, ax = plt.subplots()

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
wp_attributes = {"Cataclysmic":
        {"charge_time": 533, "base_dmg": 56586, "mag_size": 6, "reserves": 22, "reload_speed": 3.69},
    "Stormchaser":
        {"charge_time": 533, "base_dmg": 27704, "mag_size": 5, "reserves": 22, "reload_speed": 3.69},
    "Fire and Forget":
        {"charge_time": 533, "base_dmg": 28258, "mag_size": 5, "reserves": 22, "reload_speed": 3.74},
    "Reed's Regret":
        {"charge_time": 533, "base_dmg": 57822, "mag_size": 5, "reserves": 22, "reload_speed": 3.59},
    "Sailspy Pitchglass":
        {"charge_time": 533, "base_dmg": 58356, "mag_size": 5, "reserves": 22, "reload_speed": 3.73},
    "Taipan 4FR":
        {"charge_time": 533, "base_dmg": 58356, "mag_size": 5, "reserves": 22, "reload_speed": 3.63},
    "Threaded Needle":
        {"charge_time": 533, "base_dmg": 58356, "mag_size": 5, "reserves": 22, "reload_speed": 3.78},
    "The Hothead":
        {"rpm": 20, "base_dmg": 98208, "mag_size": 1, "reserves": 7, "reload_speed": 3.12},
    "Blowout":
        {"rpm": 20, "base_dmg": 98208, "mag_size": 1, "reserves": 7, "reload_speed": 3.12},
    "Roar Of The Bear":
        {"rpm": 15, "base_dmg": 84309, "mag_size": 1, "reserves": 7, "reload_speed": 3.35},
    "Hezen Vengeance":
        {"rpm": 25, "base_dmg": 98209, "mag_size": 1, "reserves": 7, "reload_speed": 2.92},
    "Code Duello":
        {"rpm": 15, "base_dmg": 84309, "mag_size": 1, "reserves": 7, "reload_speed": 3.34},
    "RedHerring":
        {"rpm": 20, "base_dmg": 98208, "mag_size": 1, "reserves": 7, "reload_speed": 3.22},
    "Royal Entry":
        {"rpm": 15, "base_dmg": 80352, "mag_size": 1, "reserves": 7, "reload_speed": 3.45},
    "Bump In The Night":
        {"rpm": 25, "base_dmg": 98209, "mag_size": 1, "reserves": 7, "reload_speed": 2.98},
    "Palmyra-B":
        {"rpm": 15, "base_dmg": 80352, "mag_size": 1, "reserves": 7, "reload_speed": 3.59},
    "Wendigo GL3":
        {"rpm": 120, "base_dmg": 39531, "mag_size": 6, "reserves": 24, "reload_speed": 3.14},
    "Interference VI":
        {"rpm": 120, "base_dmg": 39382, "mag_size": 6, "reserves": 24, "reload_speed": 3.25},
    "Tarnation":
        {"rpm": 150, "base_dmg": 31880, "mag_size": 5, "reserves": 24, "reload_speed": 3.57},
    "Cry Mutiny":
        {"rpm": 120, "base_dmg": 35411, "mag_size": 4, "reserves": 24, "reload_speed": 3.16},
    "Typhon GL5":
        {"rpm": 120, "base_dmg": 39155, "mag_size": 6, "reserves": 24, "reload_speed": 3.16},
}

weapon_list = list(wp_attributes.keys())
LFRs = weapon_list[:7]
Rockets = weapon_list[7:16]
GLs = weapon_list[16:21]

Svar0 = StringVar(root)
Svar0.set(list(wp_attributes.keys())[0])

Rvar0 = IntVar()
Rvar1 = IntVar()

# load class window
window = Window(root) # unit for reload speed is seconds

root.mainloop()

################ TODO ###############################################
# Golden Tricorn and Explosive light can be done as dropdown, or Radiobutton with 3 options (x0, x1, x2)
#
# whenever i add a new perk, do the following steps
# 1. add new Cvar<new_value> = IntVar()
# 2. add it to the undo() method to be colored black
# 3. add a Radiobutton or Checkbutton for the perk
# 4. add it to isChecked() method as Cvar(...).get()
# 5. append it to multipliers if value == 1
#
# whenever i add a new weapon do the following steps:
# 1. add it to "wp" list
# 2. make a function which colors its perks
# 3. add it to Select_Weapon() method
#
# fix slider with isChecked method
# add reload speed for each weapon to attributes
# put wp_attributes in seperate file for overview purposes
#
######################################################################
