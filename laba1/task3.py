from random import randint

class Person:
    count = 0

    def __init__(self, c):
        self.id = Person.count
        Person.count += 1
        self.command = c

class Hero(Person):
    def __init__(self, c):
        super().__init__(c)
        self.level = 1

    def up_level(self):
        self.level += 1

class Soldier(Person):
    def __init__(self, c):
        super().__init__(c)
        self.my_hero = None

    def follow(self, hero):
        self.my_hero = hero.id

h1 = Hero(1)
h2 = Hero(2)
army1, army2 = [], []

for _ in range(20):
    (army1 if randint(1, 2) == 1 else army2).append(Soldier(randint(1, 2)))

print(len(army1), len(army2))
(h1 if len(army1) > len(army2) else h2).up_level()
army1[0].follow(h1)
print(army1[0].id, h1.id)
