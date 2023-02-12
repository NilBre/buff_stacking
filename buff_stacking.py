import numpy as np
import matplotlib.pyplot as plt
import re

class weapon(object):
    """docstring for weapons."""

    def __init__(self, name, magazine, total_mag, base_damage, charge_time, enemy_type_fighting):
        self.magazine = magazine # base mag
        self.total_mag = total_mag  # full ammo reserves
        self.base_damage = base_damage # taken from nessus lost sector boss
        self.charge_time = charge_time # taken from d2 stats, in milliseconds
        self.enemy_type_fighting = enemy_type_fighting
        self.name = name

    def multi_killclip(mkc):
        match mkc:
            case 1:
                return 1.17
            case 2:
                return 1.33
            case 3:
                return 1.5

    def swashbuckler(stacks):
        match stacks:
            case 1:
                return 1.067
            case 2:
                return 1.13
            case 3:
                return 1.2
            case 4:
                return 1.266
            case 5:
                return 1.333

    def multiplier(self, enemy_type, debuff_type=False, empower=False, FoM=False, \
                        FF=False, POR=False, Bait=False, bakris=False, f_line=False, \
                        frenzy=False, vorpal=False, mkc=0, swash=0):

        base_multiplier = np.array([1])
        # if not empower:
        #     print("no empowering buff enabled")
        #     base_multiplier = np.append(base_multiplier, 1)
        if empower == "radiant":
            print("enabled: empowering buff = radiant (+ 25 %)")
            base_multiplier = np.append(base_multiplier, 1.25)
        if empower == "lumina":
            print("enabled: empowering buff = lumina (+ 35 %)")
            base_multiplier = np.append(base_multiplier, 1.35)
        if empower == "HEF":
            print("enabled: empowering buff = High Energy Fire (+ 20 %)")
            base_multiplier = np.append(base_multiplier, 1.2)
        if FoM:
            print("enabled: Font of Might (+ 25 %)")
            base_multiplier = np.append(base_multiplier, 1.25)
        if FF:
            print("enabled: Focused Fury, maximum damage (+ 22 %)")
            base_multiplier = np.append(base_multiplier, 1.22)
        # if not debuff_type:
        #     print("enemy is NOT debuffed!")
        #     base_multiplier = np.append(base_multiplier, 1)
        if debuff_type == "weak":
            print("enabled: weakened enemy (+ 15 %)")
            base_multiplier = np.append(base_multiplier, 1.15)
        if debuff_type == "debuff":
            print("enabled: enemy is debuffed with 30 %")
            base_multiplier = np.append(base_multiplier, 1.3)
        if POR:
            print("enabled: Power of Rasputin (+ 10 %)")
            base_multiplier = np.append(base_multiplier, 1.1)
        if Bait:
            print("enabled: Bait and Switch (+ 35 %)")
            base_multiplier = np.append(base_multiplier, 1.35)
        if bakris:
            print("enabled: Mask of Bakris on Hunter (+ 20 %)")
            base_multiplier = np.append(base_multiplier, 1.2)
        if f_line:
            print("enabled: Firing Line (+ 20 %)")
            base_multiplier = np.append(base_multiplier, 1.2)
        if frenzy:
            print("enabled: Frenzy (+ 15 %)")
            base_multiplier = np.append(base_multiplier, 1.15)
        if vorpal == "p":  # primary
            print("enabled: Vorpal for primaries (+ 20 %)")
            base_multiplier = np.append(base_multiplier, 1.2)
        if vorpal == "s":  # special
            print("enabled: Vorpal for special weapons (+ 15 %)")
            base_multiplier = np.append(base_multiplier, 1.15)
        if vorpal == "h":  # heavy
            print("enabled: Vorpal for heavy weapons (+ 10 %)")
            base_multiplier = np.append(base_multiplier, 1.1)
        if mkc > 0:
            print("enabled: multi kill clip with", mkc, "stacks for x", weapon.multi_killclip(mkc), "% dmg")
            base_multiplier = np.append(base_multiplier, weapon.multi_killclip(mkc))
        if swash > 0:
            print("enabled: Swashbuckler with", swash, "stacks for x", weapon.swashbuckler(swash), "% dmg")
            base_multiplier = np.append(base_multiplier, weapon.swashbuckler(swash))
        # print(base_multiplier)
        full_multiplier = np.prod(base_multiplier)
        print("Full multiplier: ", round((full_multiplier - 1) * 100, 1), "%")
        return self.base_damage * full_multiplier

if __name__=="__main__":
    # define your weapon here
    print("=================== buff/debuff options ====================")
    print("enemy_type        : \t (red_bar|miniboss)")  # higher tier enemies take less dmg
    print("empower           : \t (raidant|lumina|HEF)")  # empowering buff such as well, lumina,  etc
    print("Font of Might     : \t (True|False)")  # Font of Might Mod (stacks with everything)
    print("Focused Fury      : \t (True|False)")  # Focused Fury if the weapons can get it at maximum buff
    print("debuff_type       : \t (weak|debuff)") # self explanatory
    print("Power of Rasputin : \t (True|False)")  # Power of Rasputin Mod (stacks with everything)
    print("Bait and switch   : \t (True|False)")  # Bait and Switch for weapons which can get it
    print("Mask of Bakris    : \t (True|False)")  # mask of bakis damag when used by stasis hunters with arc weapons
    print("Firing Line       : \t (True|False)")  # firing line for weapons which can get it
    print("frenzy            : \t (True|False)")  # firing line for weapons which can get it
    print("vorpal            : \t (p|s|h)")  # firing line for weapons which can get it
    print("multi killclip    : \t (1|2|3)")  # firing line for weapons which can get it
    print("swashbuckler      : \t (1|2|3|4|5)")  # firing line for weapons which can get it
    # print("=================== define weapons here ====================")
    fire_and_forget = weapon("Fire_And_Forget", 6, 25, 28258, 533, "miniboss")  # have not tested max bullets for this gun
    cataclysmic = weapon("Cataclysmic", 6, 34, 56586, 533, "miniboss")  # 34 total mag bc of 4 times the charm
    stormchaser = weapon("Stormchaser", 5, 24, 27704, 533, "miniboss")
    print("=================== Fire and Forget ========================")
    f_and_f_all = fire_and_forget.multiplier("miniboss",
                               empower="lumina",
                               FoM=True,
                               FF=True,
                               debuff_type="debuff",
                               POR=True)
    print("Fire and Forget base damage:", fire_and_forget.base_damage, "per bullet")
    print("Fire and Forget Damage:", int(f_and_f_all), "per Bullet. Per Burst the damage is:", int(f_and_f_all) * 3)
    total_dmg_fandf = f_and_f_all * fire_and_forget.total_mag
    print("Total Damage when all buffs/debuffs active 100% of the time: ", int(total_dmg_fandf)*3, " damage")
    print("")
    print("=================== cataclysmic ========================")
    cata_per_shot = cataclysmic.multiplier("miniboss",
                               empower="lumina",
                               FoM=True,
                               debuff_type="debuff",
                               POR=True,
                               Bait=True)
    print("Cataclysmic base damage:", cataclysmic.base_damage, "per bullet")
    print("Cataclysmic Damage:", int(cata_per_shot), "per Bullet")
    total_dmg_cata = cata_per_shot * cataclysmic.total_mag
    print("Total Damage when all buffs/debuffs active 100% of the time: ", int(total_dmg_cata), " damage")
    print("")
    print("=================== stormchaser ========================")
    print("Stormchase base vs miniboss:", 27704, "but sometimes when frozen:", 34906, "and sometimes roughly 29000")
    storm_bullet_dmg = stormchaser.multiplier("miniboss",
                               empower="lumina",
                               FoM=True,
                               debuff_type="debuff",
                               POR=True,
                               bakris=False,
                               f_line=True)
    print("Stormchaser base damage:", stormchaser.base_damage, "per bullet")
    print("Stormchaser Damage:", int(storm_bullet_dmg), "per Bullet. Per Burst the damage is:", int(storm_bullet_dmg) * 3)
    total_dmg_storm = storm_bullet_dmg * stormchaser.total_mag
    print("Total Damage when all buffs/debuffs active 100% of the time: ", int(total_dmg_storm)*3, " damage")
    print("=================== template ========================")

    # wp = weapon("name", magazine, total_mag, base_damage, charge_time, enemy_type)
    # amp = wp.multiplier(enemy_type,
    #
    #
    #
    # )
