"""Лабораторная работа 10. Функции и модули"""

# Задание 10.1 (По индив. номеру)
# 13. Создайте словарь, представляющий собой записную книжку с тратами
# по разным категориям, где ключи - названия категорий, а значения -
# деньги, которые были потрачены в этой категории (целые положительные
# числа). Напишите функцию, которая принимает два словаря
# (представляющих две записные книжки) и возвращает новый словарь, в
# котором значения трат сложены.

notebook1 = {"еда": 2000, "транспорт": 500, "развлечения": 800}
notebook2 = {"еда": 1500, "транспорт": 300, "спорт": 400}
def combine_expenses(dict1, dict2):
    result = dict1.copy()
    for category, amount in dict2.items():
        if category in result:
            result[category] += amount
        else:
            result[category] = amount
    return result

combined_notebook = combine_expenses(notebook1, notebook2)
print(combined_notebook)
