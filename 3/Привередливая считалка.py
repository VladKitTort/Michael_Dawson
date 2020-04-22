# Привередливая считалка
# Демонстрирует работу команды break и ontinue
count = 0
while True:
    count += 1
    # Завершить цикл, если count принимает значение больше 10
    if count > 10:
        break
    # ропустить 5
    if count == 5:
        continue
    print(count)
input("\n\nНажмите Enter, чтобы выйти.")