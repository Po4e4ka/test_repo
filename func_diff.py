"""
Сделать функцию diff, которая считает разницу чисел,
добавить проверки на правильный тип аргументов,
вернуть результат.
Если результат меньше 0 - вернуть 0
Дополнительно:
1. Сделайте ещё один именной аргумент типа bool. Если True - то показывает разницу меньше 0
2. Попробуйте посчитать разность 3.3*3 и 9.9, попробуйте сделать так, чтобы избежать эту ошибку
"""

# --------- Проверки -----------------------
print(diff(10, 5))     # Должно вернуться 5
print(diff(100, 120))  # Должно вернуться 0
print(diff(45, 13))    # Должно вернуться 32
print(diff(3.3*3, 9.9))



