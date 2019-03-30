# tested on Python 3.5.2

import random as rnd
import timeit

# Задание 1
# Выбрал алгоритм нахождения наиболее часто встречающегося числа в списке
print('\nЗадание 1')

def hist1(v):
    sv = set(v)
    df = dict()
    for uv in sv:
        df[uv] = 0 # инициализация словаря нулевыми частотами
    for uv in v:
        df[uv] += 1
    return df

def hist2(v):
    sv = set(v)
    df = dict()
    for uv in sv:
        df[uv] = 0 # инициализация словаря нулевыми частотами
        for uuv in v:
            df[uv] += uuv == uv
    return df

n = 50
niter = 5000
D = 100
a = [rnd.randint(0,D) for i in range(n)]

def test1():
    dfreq = hist1(a)

def test2():
    dfreq = hist2(a)

dfreq = hist2(a)
print('В массиве')
print(a)
print('\nчастоты встречаемости чисел следующие:')
print(dfreq)


print('Время выполнения test1')
t1 = timeit.timeit('test1()',setup='from __main__ import test1', number = niter) / niter
print('{0:.2E} сек.'.format(t1))
print('для массива из ', n, ' элементов.')

print('Время выполнения test2')
t2 = timeit.timeit('test2()',setup='from __main__ import test2', number = niter) / niter
print('{0:.2E} сек.'.format(t2))
print('для массива из ', n, ' элементов.')

'''
Взяв для примера число испытаний
50000
и длины массива от 50 до 800,
измерил время работы первого алгоритма, t1,
а также во сколько раз второй медленнее первого:
----------
n   - t1,     t2/t1
50  - 8.1e-6, 27
100 - 1.3e-5, 46
200 - 2.4e-5, 67
400 - 4.0e-5, 92
800 - 7.2e-5, 102

Аналитика такова:
- Считая, что затраты на присвоение 0 и на инкремент одинаковы, определяем, что
время работы первого алгоритма пропорционально M+n, где M - размер множества.
Размер множества M зависит от n и от диапазона случайных чисел D. При n >> D размер
множества с большой вероятностью равен D=const, а потому время работы D+n~n при большом n.
- Аналогично допуская, определяем, что время работы второго алгоритма пропорционально
произведению Mn, а при большом n получим Dn.
- при n=400 и n=800 видим, что t2/t1 примерно равно D=100.
'''


# Задание 2
print('\nЗадание 2')

def prime_resheto(i):
    a = list(range(2,i+1))
    p = a[0]
    ps = []
    ps.append(p)
    a.remove(p)
    while a:
        for v in range(2*p,i+1,p):       
            try:
                a.remove(v)
            except:
                pass
        p = a[0]
        ps.append(p)
        a.remove(p)
    return ps

def prime(i):
    ps = [2]
    for v in range(3,i+1):
        prostoe = True
        for uv in ps:
            prostoe = prostoe and (v % uv)
            if not prostoe:
                break
        if prostoe:
            ps.append(v)
    return ps

n = 1600
niter = 10000

def fpr1():
    pr1 = prime_resheto(n)

def fpr2():
    pr2 = prime(n)

pr1 = prime_resheto(n)
print(pr1)

pr2 = prime(n)
print(pr2)

print('Время выполнения prime resheto')
t1 = timeit.timeit('fpr1()',setup='from __main__ import fpr1', number = niter) / niter
print('{0:.2E} сек.'.format(t1))
print('для массива из ', n, ' элементов.')

print('Время выполнения prime')
t1 = timeit.timeit('fpr2()',setup='from __main__ import fpr2', number = niter) / niter
print('{0:.2E} сек.'.format(t1))
print('для массива из ', n, ' элементов.')

'''
Для простых чисел менее 200, решето Эратосфена в три раза медленнее наивного алгоритма
Видимо, это связано с вычеркиванием составных чисел, которое я реализовал через удаление
из списка (remove). С ростом диапазона простых чисел отношение времен выполнения растет.
Провел эксперимент до 1600 - отношение выросло до 6.
Про сложность ничего не могу сказать, так как здесь не тривиально. Из источников, сложность
пропорциональна ln ln N.
'''

