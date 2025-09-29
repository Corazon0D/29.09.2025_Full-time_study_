# Неизменяемость строки (immutable не мутирует   не изменяется)

string = 'Теливидение'

ya = 'я'
#res = ya + string[1:]
res = string.replace('и', 'е', 1)

print(res)


