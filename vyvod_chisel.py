

from unicodedata import digit


x = int(input('Введите число: '))
base = int(input('Введите в какой системе исчесления его вывести: '))

while x > 0:
    digit = x % base
    print(digit, end='')
    x //= base
