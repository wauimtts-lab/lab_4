# Ввод числа
number = int(input("Введите четырёхзначное положительное число: "))

# Проверка числа
if 1000 <= number <= 9999:  # проверяем, что число четырёхзначное
    print("Цифры числа:")

    # Создаем итератор по цифрам
    digits = []
    temp = number
    while temp > 0:
        digits.append(temp % 10)  
        temp = temp // 10          

    digits.reverse()  

    # Вывод цифр
    for digit in digits:
        print(digit)
else:
    print("Ошибка: нужно ввести положительное четырёхзначное число.")