# Неизменяемость строки (immutable не мутирует, не изменяется)
# на хождение и подсчёт элементов

# Узнать, а есть ли такое вложение в строке
#if 'оло' in string:
#    print('оло есть в строке')

string = 'толокно'
counter = 0

count = string.count('о')
index = string.find('о')

print('В слове', string, 'число букв "о" -', count)

#  Способ 1

for i in range(len(string)):
  if string[i] == 'о':
      print('Позиция -', i + 1) # i + 1 приводим в человеческий вид

# print(index) # На позиции 1, 3, 6

# Способ 2
#i = False # Флаг, отвечающий за последубщие итерации
#for _ in range(count):
#     if i:
#        counter = string.find('о', counter + 1)
#     else:
#          counter = string.find('0')
#      i += True
#      print(counter + 1)