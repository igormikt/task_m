from abc import ABC, abstractmethod


# Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


# Конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом.")


class Bow(Weapon):
    def attack(self):
        print("Боец стреляет из лука.")


# Класс бойца
class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def fight(self):
        self.weapon.attack()  # Теперь здесь просто вызываем метод attack()


# Класс монстра
class Monster:
    def __init__(self):
        self.alive = True

    def defeat(self):
        self.alive = False
        print("Монстр побежден!")


# Демонстрация
if __name__ == "__main__":
    # Создаем оружие
    sword = Sword()
    bow = Bow()

    # Создаем бойца и монстра
    fighter = Fighter(sword)
    monster = Monster()

    # Бой с мечом
    print("Боец выбирает меч.")
    fighter.fight()
    monster.defeat()

    # Меняем оружие на лук
    print("\nБоец выбирает лук.")
    fighter.change_weapon(bow)
    fighter.fight()
    monster.defeat()