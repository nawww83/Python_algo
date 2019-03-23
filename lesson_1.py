# Задание №1
print('Задание 2')
a = int(input('Введите трехзначное число: '))

# Расщепление числа на цифры
a0 = a % 10
a = (a - a0) // 10

a1 = a % 10
a = (a - a1) // 10

a2 = a % 10
a = (a - a2) // 10

print('Сумма цифр введенного числа: ' + str(a0+a1+a2))
print('Произведение цифр введенного числа: ' + str(a0*a1*a2))


# Задание №1
print('Задание 2')
a = 5
b = 6
print('a: ' + str(a))
print('b: ' + str(b))
print('Логическое побитовое И, a & b: ' + str(a & b))
print('Логическое побитовое ИЛИ, a | b: ' + str(a | b))
print('Побитовый сдвиг вправо на 2 бита, a >> 2: ' + str(a >> 2))
print('Побитовый сдвиг влево на 2 бита, a << 2: ' + str(a << 2))

# Объяснение
# 5 & 6 = 101 & 110 = 100 = 4
# 5 | 6 = 101 | 110 = 111 = 7
# 5 >> 2 = 101 >> 2 = 1 = 1 (т.е. 5//2=2, 2//2=1)
# 5 << 2 = 101 << 2 = 10100 = 20 (т.е. 5*2*2=20)


# Задание №3
print('Задание 3')
try:
    a, b = map(int, input('Введите координаты точки 1 через пробел: ').split())
    c, d = map(int, input('Введите координаты точки 2 через пробел: ').split())
except:
    print('Неправильно вы, дядя Фёдор, точки вводите')
else:
    point_equals = (c == a and d == b)
    vertical_line = (c == a)
    kk = 'any' if point_equals else ('inf' if vertical_line else (d-b)/(c-a))
    bb = str(b) + ' - any * ' + str(a) if point_equals else ('any' if vertical_line else b - kk * a)
    print('Уравнение прямой y(x), проходящей через две введенные точки: ' + 'y(x) = ' + str(kk) + ' * x + ' + str(bb))


# Задание №4
print('Задание 4')
import random
try:
    a, b = map(int, input('Введите через пробел отрезок целых чисел [a, b]: ').split())
    c, d = map(float, input('Введите через пробел отрезок вещественных чисел [c, d]: ').split())
    e, f = map(str, input('Введите через пробел отрезок букв [e, f]: ').split())
except:
    print('Неправильно вы, дядя Фёдор, объект вводите')
else:
    print('Случайное целое число: ' + str(random.randint(a, b)))
    print('Случайное вещественное число: ' + str(random.uniform(c, d)))
    print('Случайная буква: ' + chr(random.randint(ord(e), ord(f))))


# Задание №5
print('Задание 5')
try:
    e, f = map(str, input('Введите через пробел две буквы [e, f]: ').lower().split())
except:
    print('Неправильно вы, дядя Фёдор, буквы вводите')
else:
    latFirst = ord('a')
    cyrFirst = ord('а')
    cyrLast = ord('я')
    cyrilic = ord(e) >= cyrFirst and ord(e) <= cyrLast
    start_point = latFirst if not cyrilic else cyrFirst
    print('Буква ' + e + ' стоит на ' + str( ord(e) - start_point + 1 ) + ' месте')
    print('Буква ' + f + ' стоит на ' + str( ord(f) - start_point + 1 ) + ' месте')
    print('Между введенными буквами ' + str( abs(ord(f) - ord(e)) ) + ' знакомест')


# Задание №6
print('Задание 6')
a = int(input('Введите номер буквы латинского алфавита (от ' + str(ord('a')) + ' до ' + str(ord('z')) + '): '))
print('Это буква \'' + chr(a) + '\'')


# Задание №7
print('Задание 7')
a, b, c = map(float, input('Введите через пробел три длины: ').split())
ok1 = c < (a + b)
ok2 = a < (c + b)
ok3 = b < (a + c)
rs = a == b == c
rb = not rs and (a == b or b == c or a == c)
if ok1 and ok2 and ok3:
    print('Треугольник с введенными длинами существует')
    if rs:
        print('Треугольник равносторонний')
    elif rb:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')
else:
    print('Треугольника с введенными длинами НЕ существует')


# Задание №8
print('Задание 8')
a = int(input('Введите год: '))
visokos = ((a % 4 == 0) and ((a % 100 != 0) or (a % 400 == 0)))
if visokos:
    print('Год ' + str(a) + ' является високосным')
else:
    print('Год ' + str(a) + ' високосным НЕ является')


# Задание №9
print('Задание 9')
l = list(map(float, input('Введите через пробел три числа: ').split()))
l.sort()
print('Среднее число равно: ' + str(l[1]))

