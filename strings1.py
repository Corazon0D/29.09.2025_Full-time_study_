#        012345
sting = input('Введите любую строку: ')
length = len(sting) # число элементов итерируемого объекта

print('Строка "' + sting + '" имеет длину:', length)

symb = sting[-1]# sting[lenth -1]

for index in range(-1, -(length + 1), -1):
    print(sting[index])
# print(sting[3]).