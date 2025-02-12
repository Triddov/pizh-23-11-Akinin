class Person:
    def __init__(self, name, surname, skill=1):
        self.name = name
        self.surname = surname
        self.skill = skill

    def __del__(self):
        print(f"До свидания, мистер {self.name} {self.surname}")

    def info(self):
        return f"{self.name} {self.surname}, {self.skill}"

worker = Person("И", "Котов", 3)
helper = Person("Д", "Мышев", 1)
maker = Person("O", "Рисов", 2)

print(worker.info())
print(helper.info())
print(maker.info())

del helper
print("Конец программы")
input()
