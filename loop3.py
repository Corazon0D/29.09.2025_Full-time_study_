# else и while
# else  выполняется, если цикл завершился естественно
from itertools import count

count = 0
while count < 3:
    if count == 1:
        count += 1
        continue
    print(count)
    count += 1
else:
    print('Цикл завершён') #  если цикл завершён естественно