# Законсервируем
# Демонстрирует консервацию данных и доступ к ним через интерфейс полки
import pickle
import shelve
print("Конскрвация списков.")
variety = ["огрцы", "помидоры", "капуста"]
shape = ["целые", "клубками", "соломкой"]
brand = ["Главпродукт", "Чумак", "Бондюэль"]
# Теперь открою на запись новый файл
f = open("pickles1.dat", "wb")
pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()
print("\nРасконсервация списков.")
f = open("pickles1.dat", "rb")

variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)
print(brand)
print(shape)
print(variety)
f.close()
# Полки для консервированных данных
print("\nПомещение списков на полку.")
s = shelve.open("pickles2.dat")
s["variety"] = ["огрцы", "помидоры", "капуста"]
s["shape"] = ["целые", "клубками", "соломкой"]
s["brand"] = ["Главпродукт", "Чумак", "Бондюэль"]
s.sync()
# Убедимся что данные записаны
print("\nИзвлечение спсков из файла полки:")
print("Торговые марки -", s["brand"])
print("Формы -", s["shape"])
print("Виды овощей -", s["variety"])
# Закроем файл
s.close()
input("\n\nНажмите Enter, чтобы выйти.")