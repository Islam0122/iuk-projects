from colorama import Fore, Style
import random


class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.randint(1, self.attack_power)
        other.health -= damage
        return f"{Fore.RED}{self.name} атакует {other.name} и наносит {damage} урона {Style.RESET_ALL}"

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{Fore.YELLOW}{self.name}: {self.health} HP ❤️ {Style.RESET_ALL}"


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=30)

    def special_attack(self, other):
        damage = random.randint(30, 50)
        other.health -= damage
        return f"{Fore.BLUE}{self.name} использует *Мощный удар мечом* и наносит {damage} урона!{Style.RESET_ALL}"


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=15)

    def heal(self):
        heal_amount = random.randint(15, 30)
        self.health += heal_amount
        return f"{Fore.GREEN}{self.name} восстанавливает {heal_amount} здоровья ❤️‍🩹!{Style.RESET_ALL}"


class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=25)

    def special_attack(self, other):
        damage = random.randint(20, 40)
        other.health -= damage
        return f"{Fore.CYAN}{self.name} выпускает *Точный выстрел* и наносит {damage} урона!{Style.RESET_ALL}"


def battle(hero1, hero2):
    print(f"\n{Fore.MAGENTA}Бой начинается: {hero1.name} vs {hero2.name}{Style.RESET_ALL}\n")

    while hero1.is_alive() and hero2.is_alive():
        if random.random() < 0.3 and hasattr(hero1, 'special_attack'):
            print(hero1.special_attack(hero2))
        else:
            print(hero1.attack(hero2))

        if not hero2.is_alive():
            print(f"{Fore.GREEN}{hero2.name} повержен! {hero1.name} победил!{Style.RESET_ALL}")
            break

        if random.random() < 0.3 and hasattr(hero2, 'special_attack'):
            print(hero2.special_attack(hero1))
        elif hasattr(hero2, 'heal') and random.random() < 0.2:
            print(hero2.heal())
        else:
            print(hero2.attack(hero1))
        print(hero1)
        print(hero2)
        print("-" * 40)


if __name__ == "__main__":
    thor = Warrior("Thor")
    legolas = Archer("Legolas")
    gandalf = Mage("Gandalf")

    battle(thor, legolas)
    battle(gandalf, thor)

# 8. Ввести два целых числа A и B (A < B).
# Вывести в порядке возрастания все целые числа,
# расположенные между A и B (включая сами числа A и B),
# а также количество N этих чисел.

# A = int(input("Введите A: "))
# B = int(input("Введите B: "))
#
# print("Числа от A до B:")
#
# for i in range(A, B + 1):
#     print(i, end=" ")
#
# N = B - A + 1
# print("\nКоличество чисел:", N)


#
# Задание 5.2
#
# Общее задание
# Вводится целое число N (1<=N<=9), а выводится несколько строк с числами, которые образуют определенный «узор». «Узор» задается вариантом. «Узор» создается использованием вложенных циклов.
# В варианте показан узор при введенном N=5.
# Например:
# Нужно написать программу, формирующую и выводящую в консоль узор из чисел по заданной схеме.
# Ввод:
# N = 5
# Вывод:
# 5
# 4 5
# 3 4 5
# 2 3 4 5
# 1 2 3 4 5
# // Формируем узор  (Нужно написать на языке Python )
# for (int i = n; i >= 1; i--) {
#    for (int j = i; j <= n; j++) {
#      System.out.print(j + " ");
#    }
#    System.out.println();
#    }
#   }
# }
