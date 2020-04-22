# Запишем
# Демонстрирует запись в текстовый файл
print("Создаю текстовый файл методом write().")
text_file = open("write_it.txt", "w", encoding='utf-8')
text_file.write("Это 1 строка.\n")
text_file.write("2 строка.\n")
text_file.write("А это 3 строка\n")
text_file.close()
print("\nЧитаю весь сосданный файл.")
text_file = open("write_it.txt", "r", encoding='utf-8')
print(text_file.read())
text_file.close()

print("Создаю текстовый файл методом write().")
text_file = open("write_it.txt", "w", encoding='utf-8')
lines = ["Строка 1\n",
         "Строка 2\n",
         "Это 3 строка\n"]
text_file.writelines(lines)
text_file.close()
print("\nЧитаю весь сосданный файл.")
text_file = open("write_it.txt", "r", encoding='utf-8')
print(text_file.read())
text_file.close()
input("\n\nНажмите Enter, чтобы выйти.")
