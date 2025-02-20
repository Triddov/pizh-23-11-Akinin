from random import randint

class Soldier:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def make_kick(self, enemy):
        enemy.health -= 20
        print(f"{self.name} бьет {enemy.name}")
        print(f"{enemy.name} = {enemy.health}")

first = Soldier("AAA")
second = Soldier("BBB")

while first.health > 0 and second.health > 0:
    if randint(1, 2) == 1:
        first.make_kick(second)
    else:
        second.make_kick(first)

print("ПОБЕДИЛ", first.name if first.health > second.health else second.name)
