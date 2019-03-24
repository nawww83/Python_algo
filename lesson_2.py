# Задание №1
print('\nЗадание 1')

import operator

operations = {
    '+': operator.add,
    '*': operator.mul,
    '/': operator.truediv,
    '-': operator.sub
}

def calc(op, x, y):
    return operations[op](x, y)

def inp_data():
    try:
        x, y = map(float, input('Введите через пробел два числа, x и y: ').split())
        op = input('Введите операцию, +,-,/,* (0 - выход): ')
    except:
        print('Данные введены неверно')
        return []
    else:
        return [op, x, y]

d = inp_data()
while d:
    if d[0] == '0':
        break
    elif d[0] in ['+','-','*','/']:
        if d[2] == 0 and d[0] == '/':
            res = 'inf'
        else:
            res = calc(d[0], d[1], d[2])
        print('Результат операции: ' + str(res))
    d = inp_data()


# Задание №2
print('\nЗадание 2')
x = input('Введите натуральное число: ')
x = abs(int(x))
odd = even = 0
while 1:
    x, res = divmod(x, 10)
    odd += res & 1
    even += (res & 1) ^ 1
    if x == 0:
        break
print('НЕчетных цифр: ' + str(odd))
print('Четных цифр: ' + str(even))


# Задание №3
print('\nЗадание 3')
x = input('Введите натуральное число: ')
x = str(abs(int(x)))
y = ''
for d in x[::-1]:
    y += d
print(int(y))


# Задание №4
print('\nЗадание 4')
n = int(input('Введите число слагаемых ряда: '))
sum = 1
pow = -2
for i in range(2, n):
    sum += 1/pow
    pow *= -2
print('Частичная сумма ряда равна: ' + str(sum))


# Задание №5
print('\nЗадание 5')
start = 32
stop = 127
cols = 10
rows = round( (stop - start + 1) / cols )
print('Таблица ASCII')
print('--------------------')
print('Десятичный код | Символ')
print('--------------------')
for i in range(rows):
    for j in range(cols):
        num = start + i * cols + j
        if num > stop:
            break
        else:
            print('{:<3} {:<4}'.format(num, chr(num)), end = '')
    print('')


# Задание №6
print('\nЗадание 6')

import random

x = random.randint(0, 100)
N = 10
for n in range(N):
    print('Попытка номер {}'.format(n+1))
    y = int(input('Введите число от 0 до 100: '))
    if (x == y):
        print('\n Вы победили!')
        break
    elif (x > y):
        print('Загаданное число больше')
    else:
        print('Загаданное число меньше')
else:
    print('\n Вы проиграли. Загаданное число: {}'.format(x))


# Задание №7
print('\nЗадание 7')
checked = True
k = 1
Niter = 10
while k <= Niter:
    x = random.randint(1, 10000)
    sum_analytic = x * (x + 1) // 2
    sum_directly = 0
    for n in range(x):
        sum_directly += n + 1
    checked = sum_directly == sum_analytic
    if not checked:
        print('Опа-на...')
    print('Номер опыта {}, N = {}, sum = {}, ok = {}'.format(k, x, sum_analytic, checked))
    k += 1


# Задание №8
print('\nЗадание 8')
N = int(input('Введите количество чисел: '))
d = input('Введите цифру: ')
nl = []
for i in range(N):
    n = input('Введите число: ')
    nl.append(n)

ds = ''
for i in nl:
    ds += i
print('Количество вхождений цифры {} в введенную последовательность чисел: {}'.format(d, ds.count(d)))


# Задание №9
print('\nЗадание 9')

def sumd(n):
    ns = str(n)
    sum = 0
    for d in ns:
        sum += int(d)
    return sum

N = int(input('Введите количество чисел: '))
nl = []
for i in range(N):
    n = input('Введите число: ')
    nl.append(n)
nm = 0
sd = 0
for n in nl:
    tmp = sumd(n)
    over = tmp > sd
    sd = tmp if over else sd
    nm = n if over else nm

print('Число с максимальной суммой цифр {}'.format(nm))
print(' сумма цифр {}'.format(sd))

