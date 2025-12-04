"""Лабораторная работа 11"""
# Работа с двумерными массивами
# 13.
# В) Дана матрица 4*5. Заменить все элементы с нечетными индексами на
# число 15, а числа с четными индексами заменить на нули.
# rows, cols = 4, 5
# matrix = [[0 for _ in range(cols)] for _ in range(rows)]
# for i in range(rows):
#     for j in range(cols):
#         if i % 2 != 0 or j % 2 != 0:
#             matrix[i][j] = 15
#         else:
#             matrix[i][j] = 0
# for row in matrix:
#     print(row)

# 9.В) Даны матрицы А и В одинаковой размерности, составленные из
# случайных чисел. Вывести матрицы С, D на основе матриц А и В, таким
# образом, чтобы матрица С состояла из элементов суммы соответствующих
# элементов матриц А и В. D из элементов матрицы А, если элементы
# матрицы А четные умножить на два, нечетные возвести в квадрат.

# import random
#
# rows = 3
# cols = 3
#
# A = [[random.randint(1, 9) for _ in range(cols)] for _ in range(rows)]
# B = [[random.randint(1, 9) for _ in range(cols)] for _ in range(rows)]
# C = [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]
# D = [[(A[i][j] * 2) if A[i][j] % 2 == 0 else (A[i][j] ** 2)
#       for j in range(cols)] for i in range(rows)]
#
# print("A:")
# for row in A:
#     print(row)
#
# print("\nB:")
# for row in B:
#     print(row)
#
# print("\nC = A + B:")
# for row in C:
#     print(row)
#
# print("\nD (чётные * 2, нечётные ** 2):")
# for row in D:
#     print(row)
