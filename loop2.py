# Моржовый оператор (walrus operator - :=)
string = input("Введите любую строку или exit для завершения:")

while string != '':
    string = input("Введите любую строку или exit для завершения:")
    if string == 'exit':
        break
        print('Вы ввели: ' + string)

print('Вы ввели: exit. Программа завершена')