'''
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа.
4 4 -> 2 2
5 6 -> 2 3
'''

amount = int(input('Задай сумму двух чисел: '))
multiplication = int(input('Задай произведение чисел: '))
for x in range(amount):
    for y in range(amount):
        if x + y == amount and x * y == multiplication:
            print(f'первое число ="{x}", второе число ="{y}"')

