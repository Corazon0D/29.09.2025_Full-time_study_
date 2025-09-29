"""
N = 10
for i in range(1, N + 1):
    if i % 2 == 0:
        print('Второй')
    else:
        print('Первый')
"""
from xml.dom.expatbuilder import FILTER_SKIP

"""
string = input("Введите любую строку: ")

while string != '':
    string = input("Введите любую строку: ")

print("Вы ничего не ввели. Программа завершена")
"""
loop = True
while loop:
    string = input("Введите любую строку: ")
    if not string:
        loop = False

print("Вы ничего не ввели. Программа завершена")