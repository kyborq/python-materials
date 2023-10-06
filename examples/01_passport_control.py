# константы для переиспользования переменных
# всегда с заглавных и в начале файла
CURRENT_YEAR = 2023
AGE_MINIMUM_LIMIT = 18

# после вызова input программа будет ждать
# ввода с клавиатуры, после чего нужно
# нажать клавишу Enter и программа продолжится
my_name = input("Как тебя зовут: ")

# int превращает строку в число
my_birth_year = int(input("Введи год рождения: "))

actual_age = CURRENT_YEAR - my_birth_year

if (actual_age > AGE_MINIMUM_LIMIT):
    print(f"Привет, {my_age}!")
else:
    print("Ты слишком молод для этого!")