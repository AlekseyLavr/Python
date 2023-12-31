'''
Задача 10
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть.
Пример:
5 -> 1 0 1 1 0
2
'''
from random import randint
n = int(input('Введите число монеток: '))
heads, tails = 0, 0
for i in range(n):
    send = randint(0, 1)
    print(send, end=' ')
    if send > 0:
        heads += 1
    else:
        tails += 1
print()
if heads > tails:
    print(f'Нужно перевернуть {tails} монет(ы)')
else:
    print(f'Нужно перевернуть {heads} монет(ы)')