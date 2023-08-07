hero_damage = 100


def double_damage():
    global hero_damage
    hero_damage *= 2
    pass


def disarmed():
    global hero_damage
    hero_damage *= 0.1
    pass


def power_potion():
    global hero_damage
    hero_damage += 100
    pass
disarmed()
print(hero_damage)
