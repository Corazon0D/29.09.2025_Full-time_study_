# Методы строк
# string = input().strip(). lower() - цепочка вызовов
string = 'язык Python'

print(string.lower()) # все буквы маленькие
print(string.upper()) # все буквы большие
print(string.title()) # Все слова в строке начинаются с большой буквы
print(string.capitalize()) # Только первая буква большая
print(string.strip('я')) # Убрать символы в начале и в конце
# rstrip, lstrip