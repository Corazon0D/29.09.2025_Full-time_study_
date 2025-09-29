#        012345
sting = 'Привет'# Пие
lenth = len(sting) # число элементов итерируемого объекта

print('Строка "' + sting + '" имеет длину:', lenth)

for i in range(0, len(sting), 2):
    print(sting[i])

# print(sting[3])