"""
Поиск элемента: линейный и бинарный
"""

# def linear_search(arr, n):
#     c = 0
#     for i in range(len(arr)):
#         c += 1
#         if arr[i] == n:
#             return f"{i} index, {c} comparisons"
#     return -1, c
#
# # print(linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 9))
# db = ['islam','b','d','a']
# search = 'a'
# print(linear_search(db, search))


# def linear_search(arr, n):
#     c = 0
#     for i in arr:
#         c += 1
#         if i == n:
#             return f"{i} , {c} comparisons"
#     return -1, c


#
# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#     c = 0
#     while left <= right:
#         mid = (left + right) // 2
#         c += 1
#         if arr[mid] == target:
#             return f"{mid} index, {c} comparisons"
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1, c
#
# print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 9))


# students = ["Alice", "Bob", "Charlie", "David", "Eve"]
#
# def linear_search_student(students, name):
#     print(f"Students: {students}")
#     print(f"Searching for: {name}\n")
#
#     for i, student in enumerate(students):
#         print(f"Step {i + 1}: checking {student}")
#         if student == name:
#             print(f"✅ Found {name} at index {i} after {i + 1} comparisons!")
#             return i
#     print(f"❌ {name} not found in the list.")
#     return -1
#
#
# linear_search_student(students, "David")


"""
Алгоритм сортировки
"""
# Пузырьковая сортировка (Bubble Sort)
# def bubble_sort(arr):
#     n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print(arr)
    return arr
#
# # Пример
# numbers = [5, 2, 9, 1, 5]
# sorted_numbers = bubble_sort(numbers)
# print("Sorted:", sorted_numbers)

# ⃣ Сортировка вставками (Insertion Sort)
#
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        print(arr)
    return arr
#
# numbers = [5, 2, 9, 1, 5]
# sorted_numbers = insertion_sort(numbers)
# print("Sorted:", sorted_numbers)


# Сортировка выбором (Selection Sort)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(arr)
    return arr
#
# numbers = [5, 2, 9, 1, 5]
# sorted_numbers = selection_sort(numbers)
# print("Sorted:", sorted_numbers)

"""
Алгоритм хеширование
"""
"""
| Область                      | Пример использования                              |
| ---------------------------- | ------------------------------------------------- |
| 🧭 **Хеш-таблицы / словари** | Быстрый поиск данных по ключу                     |
| 🔐 **Пароли**                | Хранение паролей в виде хеша (не в открытом виде) |
| 🧾 **Контроль целостности**  | Проверка, изменился ли файл                       |
| 🧠 **Базы данных / кэш**     | Быстрый доступ и идентификация записей            |
"""
"""
"Hello"  →  8b1a9953c4611296a827abf8c47804d7
"""
# def simple_hash(text):
#     hash_value = 0
#     for char in text:
#         hash_value += ord(char)  # превращаем символ в число (код)
#     return hash_value % 100  # остаток для ограничения длины
#
# print(simple_hash("Islam"))
# print(simple_hash("IslAm"))

# import hashlib
#
# # Строку нужно сначала закодировать в байты
# text = "IslamDuishobaev".encode()
#
# # Пример с алгоритмом MD5
# hash_md5 = hashlib.md5(text).hexdigest()
#
# # Пример с алгоритмом SHA256 (надёжнее)
# hash_sha256 = hashlib.sha256(text).hexdigest()
#
# print("MD5:", hash_md5)
# print("SHA256:", hash_sha256)

"""
🧰 Применение в реальных проектах

Веб-приложения: хеширование паролей пользователей (например, Django, Flask)

Системы контроля версий: Git использует SHA1 для идентификаторов коммитов

Базы данных: ключи в Redis, MongoDB и других системах — это хеши
"""


"""
Рекурсия
"""
# def countdown(n):
#     if n == 0:  # базовый случай
#         print("Старт!")
#     else:
#         print(n)
#         countdown(n - 1)  # рекурсивный вызов
#
# countdown(5)
#
# def list_sum(numbers):
#     if not numbers:  # если список пуст
#         return 0
#     return numbers[0] + list_sum(numbers[1:])
#
# print(list_sum([1, 2, 3, 4, 5]))
#
#
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# #
# print(factorial(5))