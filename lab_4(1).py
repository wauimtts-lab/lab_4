number = input("Введите номер телефона в формате +7(ххх)ххх-хх-хх: ")
if (len(number) == 16 and number[0:2] == "+7" and number[2] == "(" and number[6] == ")" and
     number[10] == "-" and number [13] == "-" and number[3:6].isdigit() and number[7:10].isdigit() and number[11:13].isdigit() and number[14:16].isdigit()):
    print("Да")
else:
    print("Нет")