def main():
    print("ПРИЛОЖЕНИЕ")
    print("Доступные функции:")
    print("1. Функция 1")
    print("2. Функция 2")
    print("3. Функция 3")
    print("4. Функция 4")
    
    choice = input("Выберите функцию (1-4): ")
    
    if choice == "1":
        function1()
    elif choice == "2":
        function2()
    elif choice == "3":
        function3()
    elif choice == "4":
        function4()
    else:
        print("Неверный ввод")

def function1():
    print("Это функция 1 - Сложение")
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    print(f"Результат: {a + b}")

def function2():
    print("Это функция 2 - Вычитание")
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    print(f"Результат: {a - b}")        

def function3():
    print("Это функция 3 - Умножение")
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    print(f"Результат: {a * b}")

def function4():
    print("Это функция 4 - Деление")
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    if b != 0:
        print(f"Результат: {a / b}")
    else:
        print("Ошибка: деление на ноль!")

if __name__ == "__main__":
    main()