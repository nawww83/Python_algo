# Задание №1
print('Задание 1')

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
print('Задание 2')
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
print('Задание 3')
print()
