"""Лабораторная работа 4."""

# 13.
# А) Дан одномерный массив, состоящий из N вещественных элементов.
# Ввести массив с клавиатуры. Найти и вывести минимальный по модулю
# элемент.
# Б) Переставить в одномерном массиве минимальный элемент и
# максимальный.

# --- А ---
N = int(input("Введите количество элементов: "))
array = []
for i in range(N):
    x = float(input(f"Введите элемент #{i+1}: "))
    array.append(x)

print("Введённый массив:", array)
min_abs = min(array, key=lambda x: abs(x))
print("Минимальный по модулю элемент:", min_abs)

# --- Б ---
min_value = min(array)
max_value = max(array)

min_index = array.index(min_value)
max_index = array.index(max_value)
array[min_index], array[max_index] = array[max_index], array[min_index]

print("Массив после перестановки минимального и максимального:", array)
