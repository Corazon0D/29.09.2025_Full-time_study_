"""
N = 10
for i in range(1, N + 1):
    if i % 2 == 0:
        print('Второй')
    else:
        print('Первый')
"""

for i in range(101):
    if i % 10 != 4:
        continue
    print(i)