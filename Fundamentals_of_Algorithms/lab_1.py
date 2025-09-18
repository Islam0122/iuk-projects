""" Лабораторная работа №1"""
# Программирование алгоритмов линейной структуры

# print("=== Примеры ===")
# print("Информатика")
#
# sms = input("Введите сообщение: ")
# print(sms)
#
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# print("Сумма:", a + b)
#
# som = float(input("Количество денег (в сомах): "))
# dollar = float(input("Курс доллара: "))
# print("Можно купить долларов:", round(som / dollar, 2))
#
# from math import *
# x = float(input("Введите x: "))
# a = float(input("Введите a: "))
# y = sin(x) + pow(a, 3)
# print("y =", y)
from math import *
# print("\n=== ЗАДАНИЕ 1 ===")
# 1. ФИО
# f = input("Фамилия: ")
# i = input("Имя: ")
# o = input("Отчество: ")
# print(f, i, o)
#
# # # 2. Фамилия ж.р.12
#
# # 3. Дата рождения
# d = input("День: ")
# m = input("Месяц: ")
# y = input("Год: ")
# print(d + "." + m + "." + y)
# print(d + "/" + m + "/" + y)
# print(d + " " + m + " " + y)
# print(d + "-" + m + "-" + y)
#
# # # 4. Стоимость фото
# price = float(input("Цена за фото: "))
# count = int(input("Количество: "))
# print("Стоимость печати:", price * count)
#
# # 5. Периметр, площадь, диагональ
# a = float(input("a: "))
# b = float(input("b: "))
# P = 2 * (a + b)
# S = a * b
# d = sqrt(a**2 + b**2)
# print("P =", P, "S =", S, "d =", d)
#
#
# print("\n=== ЗАДАНИЕ 1.2 ===")
#
# # 1. Расстояние между точками
# x1, y1 = map(float, input("x1 y1: ").split())
# x2, y2 = map(float, input("x2 y2: ").split())
# dist = sqrt((x2 - x1)**2 + (y2 - y1)**2)
# print("Расстояние =", dist)
# #
# # 2. Скорость спортсмена
# s = float(input("Дистанция (м): "))
# t = float(input("Время (с): "))
# print("Скорость:", s / t)
#
# # 3. Доход по вкладу
# summ = float(input("Сумма вклада: "))
# p = float(input("Процент годовых: "))
# m = int(input("Срок (мес): "))
# income = summ * (p / 100) * (m / 12)
# print("Доход:", income)
#
# # 4. Денежный формат
# num = float(input("Введите дробное число: "))
# som = int(num)
# tyiyn = round((num - som) * 100)
# print(f"{som} сом {tyiyn} тыйын")
#
# # 5. Оптимальный вес
# height = int(input("Рост: "))
# weight = int(input("Вес: "))
# optimal = height - 100
# print("Оптимальный вес:", optimal)

# print("\n=== ЗАДАНИЕ 1.2 --> 13 ===")
# # Найти площадь треугольника по формуле Герона.
# a = int(input("a= "))
# b = int(input("b= "))
# c = int(input("c= "))
# p = (a + b + c) / 2
# s = (p*(p - a)*(p - b)*(p - c)) ** 0.5
#
# print("res: ",s)