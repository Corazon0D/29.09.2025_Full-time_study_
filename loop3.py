# else и while
# else  выполняется, если цикл завершился естественно
from itertools import count

count = 0
while count < 3:
    print(count)
    count += 1
else:
    print('Цикл завершён') #  если цикл завершён естественно