# tested in Python 3.7.3
import random

# Задание 1
print('\nЗадание 1')
a = [i for i in range(2,100)]
b = [i for i in range(2,10)]

nc = []
for r in b:
	f = lambda x: not (x % r)
	nc.append(sum(map(f, a)))
print('Количество чисел от 2 до 99, кратных ')
print(b)
print('соответственно, равно')
print(nc)


# Задание 2
print('\nЗадание 2')
n = 10
a = [random.randint(0,100) for i in range(n)]
f = lambda x: not (x % 2)
ea = map(f, a)
ne = [i for i,v in enumerate(ea) if v == True]
print('В массиве ')
print(a)
print('четные элементы имеют следующие индексы:')
print(ne)


# Задание 3
print('\nЗадание 3')
n = 10
a = [random.randint(0,100) for i in range(n)]
mx = max([v for v in set(a)])
mn = min([v for v in set(a)])
print('В массиве')
print(a)
print('найден максимум и минимум')
print(mx, mn, end='')
print(', соответственно')
imn = a.index(mn)
imx = a.index(mx)
a[imn], a[imx] = mx, mn
print('Массив после перестановки максимума и минимума:')
print(a)


# Задание 4
print('\nЗадание 4')
n = 100
a = [random.randint(0,100) for i in range(n)]
sa = set(a) # для уникальности ключа
dc = {}
for v in sa:
	f = lambda x: x == v
	dc[v] = sum(map(f, a))
mx = max(zip(dc.values(), dc.keys()))
print('В массиве:')
print(a)
print('\n чаще всего встречается число: ', mx[1])
print('\n число вхождений: ', mx[0])


# Задание 5
print('\nЗадание 5')
n = 20
a = [random.randint(-100,100) for i in range(n)]
mxn = max([v for v in set(a) if v < 0])
print('В массиве')
print(a)
print('найден  отрицательный максимум')
print(mxn, end='')
print(', его индекс: ', a.index(mxn))


# Задание 6
print('\nЗадание 6')
n = 20
a = [random.randint(0,100) for i in range(n)]
mx = max(set(a))
mn = min(set(a))
start = min(a.index(mx), a.index(mn))
stop = max(a.index(mx), a.index(mn))
total = sum(a[start+1:stop])
print('В массиве')
print(a)
print('сумма элементов между')
print(a[start], a[stop])
print('равна')
print(total)


# Задание 7
print('\nЗадание 7')
n = 20
a = [random.randint(0,100) for i in range(n)]
print('В массиве')
print(a)
a.sort()
print('два наименьших элемента равны')
print(a[0], a[1])


# Задание 8
print('\nЗадание 8')
m = []
for n in range(5):
    print('Ввод строки номер', n+1)
    a = list(map(float, input('Введите через пробел три вещественных числа:').split()))
    a = a[:3]
    a.append(sum(a))
    m.append(a)
print('Искомая матрица 5x4 равна:')
for v in m:
    print(v)


# Задание 9
print('\nЗадание 9')
mt = list(zip(*m))
mn = []
for v in mt:
    mn.append(min(v))
print('Наибольший среди минимальных элементов столбцов матрицы 5x4:')
print(max(mn))

