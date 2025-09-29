# else и while
# else  выполняется, если цикл завершился естественно
from itertools import count
num = 6 # 0 ... 10
attemts = 0

while attemts < 3:
    guess = int(input('Введите чиcло: '))
    attemts += 1
    if guess == num:
        print('Ура, угадали!')
        break
    elif guess > num:
        print('Ваше число больше загаданного')
    else:
        print('Ваше чило меньше загаданного')
else:
    print('Попытки закончились! А число было:', num) #  если цикл завершён естественно