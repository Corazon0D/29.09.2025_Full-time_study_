"""
N = 10
for i in range(1, N + 1):
    if i % 2 == 0:
        print('Второй')
    else:
        print('Первый')
"""
# while True # вечный цикл

# string = input("Введите любую строку или exit для завершения:")
while True:
    string = input("Введите любую строку или exit для завершения:")
    if string == 'exit':
        break
        print('Вы ввели: ' + string)

