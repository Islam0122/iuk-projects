"""Лабораторная работа 10. Функции и модули"""

# Задание 10.1 (По индив. номеру)
# 13. Создайте словарь, представляющий собой записную книжку с тратами
# по разным категориям, где ключи - названия категорий, а значения -
# деньги, которые были потрачены в этой категории (целые положительные
# числа). Напишите функцию, которая принимает два словаря
# (представляющих две записные книжки) и возвращает новый словарь, в
# котором значения трат сложены.

# notebook1 = {"еда": 2000, "транспорт": 500, "развлечения": 800}
# notebook2 = {"еда": 1500, "транспорт": 300, "спорт": 400}
# def combine_expenses(dict1, dict2):
#     result = dict1.copy()
#     for category, amount in dict2.items():
#         if category in result:
#             result[category] += amount
#         else:
#             result[category] = amount
#     return result
#
# combined_notebook = combine_expenses(notebook1, notebook2)
# print(combined_notebook)

# Задание 10.1 (По индив. номеру)
# 9. При помощи функций реализуйте игру &quot;Угадай число&quot;
# import random
# def main():
#     bot_number = random.randint(1, 10)
#     print("Я загадал число от 1 до 10. Попробуй угадать!")
#     user_number = int(input("Введи число: "))
#     if user_number == bot_number:
#         print("Ты угадал! ")
#     else:
#         print(f"Не угадал! Я загадал: {bot_number}")
# main()

# 8. Программа предлагает пользователю два случайных числа и случайную
# математическую операцию из двух: сложение или умножение. Далее
# пользователь вводит ответ, и если он правильный, программа выводит
# поздравление. Если ответ неправильный, тогда выводится правильный ответ
import random

def main():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    operation = random.choice(['+', '*'])

    if operation == '+':
        correct_answer = num1 + num2
    else:
        correct_answer = num1 * num2

    print(f"Вычислите: {num1} {operation} {num2}")
    user_answer = float(input("Ваш ответ: "))

    if user_answer == correct_answer:
        print("Поздравляем! Ответ правильный ")
    else:
        print(f"Неправильно Правильный ответ: {correct_answer}")

main()


