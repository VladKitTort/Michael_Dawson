# Цена авто
# Расчитываем полную стоимость автомобиля

price = float(input("Напишите цену автомобиля: "))

tax = price / 100 * 25
registration_fee = price / 100 * 15
agency_fee = 100
delivery = 150
full_price = price + tax + registration_fee + agency_fee + delivery

print("\nПолная стоимость вашего автомобиля:", full_price)
