def main():
    print("Добро пожаловать в простое приложение!")
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

if __name__ == "__main__":
    main()