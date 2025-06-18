class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} ест")

    def make_sound(self):
        pass


class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} поет: Чирик-чирик!")


class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} рычит: Рррр!")


class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} шипит: Шшссс!")


class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк")

    def add_staff(self, person):
        self.staff.append(person)
        print(f"Сотрудник {person.name} добавлен в зоопарк")


class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}")


class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}")


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


# Создаем животных
bird = Bird("Соловей", 1)
mammal = Mammal("Лев", 3)
reptile = Reptile("Змея", 2)

# Создаем сотрудников
keeper = ZooKeeper("Иван")
vet = Veterinarian("Мария")

# Создаем зоопарк и добавляем животных и сотрудников
zoo = Zoo()
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)
zoo.add_staff(keeper)
zoo.add_staff(vet)

# Демонстрируем работу
print("\nЗвуки животных:")
animal_sound(zoo.animals)

print("\nРабота сотрудников:")
keeper.feed_animal(bird)
vet.heal_animal(mammal)