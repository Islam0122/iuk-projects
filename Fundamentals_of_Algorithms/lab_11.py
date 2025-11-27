"""Лабораторная работа 11"""
# Работа с двумерными массивами
# 13.
# В) Дана матрица 4*5. Заменить все элементы с нечетными индексами на
# число 15, а числа с четными индексами заменить на нули.
rows, cols = 4, 5
matrix = [[0 for _ in range(cols)] for _ in range(rows)]
for i in range(rows):
    for j in range(cols):
        if i % 2 != 0 or j % 2 != 0:
            matrix[i][j] = 15
        else:
            matrix[i][j] = 0
for row in matrix:
    print(row)
