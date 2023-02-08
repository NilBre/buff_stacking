import numpy as np
import matplotlib.pyplot as plt

def triple_tap(n_bullets):
    counter = 0
    bullet_depletion = []
    while n_bullets != 0:
        bullet_depletion.append(n_bullets)
        n_bullets -= 1
        counter += 1
        if counter % 3 == 0:
            n_bullets += 1
    bullet_depletion.append(0)
    return bullet_depletion, counter

def FourTimesTheCharm(n_bullets):
    counter = 0
    bullet_depletion = []
    while n_bullets != 0:
        bullet_depletion.append(n_bullets)
        n_bullets -= 1
        counter += 1
        if counter % 4 == 0:
            n_bullets += 2
    bullet_depletion.append(0)
    return bullet_depletion, counter

def TripleTapFourTimes(n_bullets):
    counter = 0
    bullet_depletion = []
    while n_bullets != 0:
        bullet_depletion.append(n_bullets)
        n_bullets -= 1
        counter += 1
        if counter % 4 == 0:
            n_bullets += 2
        if counter % 3 == 0:
            n_bullets += 1
    bullet_depletion.append(0)
    # print(counter)
    return bullet_depletion, counter

if __name__=="__main__":

    bullets = 7
    y_triple = triple_tap(bullets)[0]
    y_four = FourTimesTheCharm(bullets)[0]
    y_both = TripleTapFourTimes(bullets)[0]

    x1 = np.linspace(0, len(y_triple)-1, len(y_triple))
    x2 = np.linspace(0, len(y_four)-1, len(y_four))
    x3 = np.linspace(0, len(y_both)-1, len(y_both))

    plt.plot(x1, y_triple, "r-", label='triple tap: {} bullets'.format(triple_tap(bullets)[1]))
    plt.plot(x2, y_four, 'b-', label='four times: {} bullets'.format(FourTimesTheCharm(bullets)[1]))
    plt.plot(x3, y_both, 'g-', label='four times and triple tap: {} bullets'.format(TripleTapFourTimes(bullets)[1]))
    plt.grid()
    plt.xlabel('# Bullets')
    plt.ylabel('Bullet Depletion')
    plt.legend()
    plt.show()
    plt.clf()

    # weapons with 4 times the charm and their maximum mag size
    weapons = {"duty_bound":57, "pointed_inquiry":19, "braytech_werewolf":45, "cataclysmic":7, "tears_of_contrition":20}

    vals = weapons.values()
    keys = weapons.keys()

    for weapon in keys:
        if weapon=="duty_bound" or weapon=="tears_of_contrition":
            print(f"Weapon : {weapon}: # bullets 4 times the charm and triple tap: ", TripleTapFourTimes(weapons[weapon])[1])
        print(f"Weapon : {weapon}: # bullets 4 times the charm: ", FourTimesTheCharm(weapons[weapon])[1])

    for weapon,n_bullets in zip(list(keys),list(vals)):
        y = FourTimesTheCharm(n_bullets)[0]
        total_bullets_used = FourTimesTheCharm(n_bullets)[1]
        x = np.linspace(0, len(y)-1, len(y))
        plt.plot(x, y, label=weapon+" : (mag|bullets shot) : ({}|{})".format(n_bullets, total_bullets_used))
        plt.grid()
        plt.legend()
        plt.xlabel("# bullets")
        plt.ylabel("Bullet Depletion")
    plt.show()
