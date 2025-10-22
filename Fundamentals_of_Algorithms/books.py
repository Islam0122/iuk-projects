# # --- ОТКРЫТИЕ ФАЙЛА ---
# # open(имя_файла, режим, кодировка)
# # режим "r" — чтение, "w" — запись, "a" — добавление, "r+" — чтение и запись
# file = open("books.txt", "r", encoding="utf-8")
#
# print("📂 1. Объект файла:")
# print(file)  # просто показывает объект, не содержимое
#
# # --- ЧТЕНИЕ ФАЙЛА ---
# print("\n📖 2. Чтение первых 21 символа:")
# print(file.read(21))  # считывает 21 символ
#
# print("\n📖 3. Чтение следующей строки:")
# print(file.readline())  # читает одну строку после уже прочитанного
#
# print("\n📖 4. Чтение оставшихся строк как список:")
# print(file.readlines())  # возвращает список всех оставшихся строк
#
# # --- Положение курсора ---
# print("\n📍 5. Позиция курсора после чтения:", file.tell())
#
# # --- Перемещение курсора ---
# file.seek(0)  # возвращаем курсор в начало файла
# print("\n🔁 6. После seek(0):", file.tell())
# print("Снова читаем первые 10 символов:", file.read(10))
#
# # --- Закрытие файла ---
# file.close()
# print("\n❌ 7. Файл закрыт:", file.closed)
#
# # --- АВТОМАТИЧЕСКОЕ ОТКРЫТИЕ ЧЕРЕЗ 'with' ---
# print("\n✅ 8. Работа с файлом через 'with open()' (автоматически закрывает):")
# with open("books.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())
#
# # --- ЗАПИСЬ В ФАЙЛ ---
# print("\n✏️ 9. Запись в новый файл:")
# with open("new_books.txt", "w", encoding="utf-8") as f:
#     f.write("The Alchemist\n")
#     f.write("The Great Gatsby\n")
#     f.writelines(["War and Peace\n", "Pride and Prejudice\n"])
#
# print("✅ Данные успешно записаны в new_books.txt")
#
# # --- ДОБАВЛЕНИЕ В ФАЙЛ ---
# print("\n➕ 10. Добавление данных:")
# with open("new_books.txt", "a", encoding="utf-8") as f:
#     f.write("Added later: Dune\n")
#
# # Проверим результат
# print("\n📄 11. Содержимое new_books.txt:")
# with open("new_books.txt", "r", encoding="utf-8") as f:
#     print(f.read())


"""
open file

body

close file
"""
file = open('books.txt')
c = file.readlines()
print(c)
file.close()