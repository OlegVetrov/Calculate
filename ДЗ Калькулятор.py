while True:
    a = float(input("Пожалуйста, введите первое число"))
    operation = input("""Пожалуйста, выберите действие
    + для сложения
    - для вычитания
    / для деления
    * для умножения
    0 для завершения программы
    """)
    if operation == "0":
        print("Операция отменена!")
        break
    else:
        b = float(input("Пожалуйста, введите второе число"))
        if operation == "+":
            print(a + b)
        elif operation == "-":
            print(a - b)
        elif operation == "/":
            print(a / b)
        elif operation == "*":
            print(a * b)
        else:
            print("Вы ввели некорректные данные. Пожалуйста, попробуйте еще раз.")
