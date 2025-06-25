import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона!")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self):
        self.player = Hero(input("Введите имя вашего героя: "))
        self.computer = Hero("Компьютерный Герой")

    def start(self):
        print("\nНачинается битва героев!")
        print(f"{self.player.name} vs {self.computer.name}\n")

        current_attacker, current_defender = self.player, self.computer

        while self.player.is_alive() and self.computer.is_alive():
            # Показываем текущее состояние
            print(f"{self.player.name}: {self.player.health} HP")
            print(f"{self.computer.name}: {self.computer.health} HP\n")

            # Ход текущего атакующего
            current_attacker.attack(current_defender)

            # Меняем атакующего и защитника местами для следующего раунда
            current_attacker, current_defender = current_defender, current_attacker

            # Небольшая пауза для удобства чтения
            input("\nНажмите Enter для продолжения...\n")

        # Определяем победителя
        if self.player.is_alive():
            print(f"\n{self.player.name} побеждает! Поздравляем!")
        else:
            print(f"\n{self.computer.name} побеждает. Попробуйте еще раз!")

        print("\nИгра завершена.")


# Создаем и запускаем игру
if __name__ == "__main__":
    game = Game()
    game.start()