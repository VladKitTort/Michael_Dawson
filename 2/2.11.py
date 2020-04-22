# Создание нового блюда.
# Создание производим через запрос от пользователя.

favorite_dish_1 = input("\nВедите свое самое любимое блюдо: ")
favorite_dish_2 = input("\nВедите свое самое любимое блюдо номер 2: ")
favorite_dish = favorite_dish_1 + favorite_dish_2
print("\nНовейшее прекрасное блюдо:", favorite_dish.title())