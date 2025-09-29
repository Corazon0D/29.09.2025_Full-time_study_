from itertools import count
# for count in range(s, s, s)
# s - start ( 0 -  по умолчанию )
# s - stop (не включая)
# s - step ( 1 -  по умолчанию )
# for i in range(10) ->... i in range(0, 10, 1)

import turtle

count = 8 # Число фигур
sides = 4

"""
for i in range(count): # (просто крутануть sides раз) 8
    for i in range(sides): # 4
        turtle.forward(100) # идёт вперёд на 100
        turtle.right(360 / sides) # 360 градусов / количество сторон
    turtle.right(360 / count)
# count += 1 # Инкремент счётчика

turtle.mainloop()
"""
# или таким способом
count = 0 # Число фигур
sides = 0
N = 8 # Большая Буква ОЗНАЧАЕТ константа (не изменяемая)
M = 5
turtle.speed(0) # мгновенная скорость

# переносим "черепаху" на 50 вверих и на 30 влево
turtle.penup()
turtle.goto(-30, 50)
turtle.pendown()

while count < N: #
    while sides < M: # 4
        turtle.forward(100) # идёт вперёд на 100
        turtle.right(360 / M) # 360 градусов / количество сторон
        sides += 1
    turtle.right(360 / N )
    count += 1
    sides = 0

turtle.mainloop()