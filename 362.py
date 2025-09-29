sting = input('Введите любую строку: ')
lenth = len(sting)

print('Строка "' + sting + '" имеет длину:', lenth)

for i in range(0, len(sting), 2):
    print(sting[i])

symb = sting[lenth -1]
print(symb)
# print(sting[3])