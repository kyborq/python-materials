print("--- Калькулятор 2000")
print("1) Сложить")
print("2) Вычесть")
print("3) Умножить")
print("4) Поделить")

choice = input("Ваш выбор: ")
left_op = int(input("Первое число: "))
right_op = int(input("Второе число: "))

if (choice == "1"):
    result = left_op + right_op
    print(f"Результат сложения: {result}")
elif (choice == "2")
    result = left_op - right_op
    print(f"Результат вычитания: {result}")
elif (choice == "3")
    result = left_op * right_op
    print(f"Результат умножения: {result}")
elif (choice == "4")
    result = left_op / right_op
    print(f"Результат деления: {result}")