# Моржовый оператор (walrus operator - :=)


while (string := input("Введите любую строку или exit для завершения:")) != '':
    string = input("Введите любую строку или exit для завершения:")
    if string == 'exit':
        break
        print('Вы ввели: ' + string)

print('Вы ввели: exit. Программа завершена')