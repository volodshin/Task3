def season():
    number = int(input("Введіть номер місяця: "))
    if number <= 2 or number == 12:
        print("Зима")
    elif number >= 3 and number <= 5:
        print("Весна")
    elif number >= 6 and number <= 8:
        print("Літо")
    elif number >= 9 and number <= 11:
        print("Осінь")
    else:
        print("Неправильно введений номер місяця")
    
print(season())