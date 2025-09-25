# print("Задание 1.1 ")
"""
13. Составить программу проверки умения умножать числа.
"""
# import random
#
# a = random.randint(1, 10)
# b = random.randint(1, 10)
#
# print(f"Сколько будет {a} × {b}?")
# user_answer = int(input("Ваш ответ: "))
# if user_answer == a * b:
#     print("Правильно! Молодец!")
# else:
#     print(f"Неправильно. Правильный ответ: {a * b}")


# print("Задание 1.2")
"""
13. Напишите программу, вычисляющую значение функции 
(на вход подается вещественное число).
"""
# from math import sin
# x = float(input("Введите число x: "))
# if 0.2 <= x <= 0.9:
#     f = sin(x)
# else:
#     f = 1
#
# print(f"f(x) = {f}")



# print("Задание 1.3")
"""
13. Написать программу, которая запрашивает номер дня недели и 
выводит одно из сообщений: «Рабочий день», «Суббота» или «Воскресенье».
"""
# day = int(input("Введите номер дня недели (1-7): "))
# if 1 <= day <= 5:
#     print("Рабочий день")
# elif day == 6:
#     print("Суббота")
# elif day == 7:
#     print("Воскресенье")
# else:
#     print("Ошибка: в неделе только 7 дней!")


# print("Задание 1.4")
"""
13. Даны 10 чисел. Определить максимальное число и его порядковый номер.
"""
# numbers = []
# for i in range(10):
#     num = int(input(f"Введите число {i+1}: "))
#     numbers.append(num)
# max_number = max(numbers)
# max_index = numbers.index(max_number)
# print(f"Максимальное число: {max_number}")
# print(f"Его порядковый номер: {max_index}")


# print("Задание 1.5")
"""
13. Найти сумму всех положительных чисел от a до b включительно 
(значения a и b вводятся с клавиатуры).
"""
# a = int(input("Введите число a: "))
# b = int(input("Введите число b: "))
#
# if a > b:
#     a, b = b, a
# total = sum(i for i in range(a, b + 1) if i > 0)
# print(f"Сумма всех положительных чисел от {a} до {b} = {total}")


# print("Задание 1.6")
"""
13. Вводя в цикле три оценки, определить число студентов,
не имеющих оценок 2 и 3. В группе учится К студентов.
"""
# K = int(input("Введите количество студентов в группе: "))
# count = 0
# for i in range(1, K + 1):
#     print(f"\nСтудент {i}:")
#     grades = []
#     for j in range(1, 4):
#         grade = int(input(f"Введите оценку {j}: "))
#         grades.append(grade)
#     if 2 not in grades and 3 not in grades:
#         count += 1
# print(f"\nКоличество студентов без оценок 2 и 3: {count}")
