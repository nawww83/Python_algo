# tested in Python 3.7.3 on Windows 64 bit

# Задание 1

import sys
#import time
from memory_profiler import profile

#import cProfile

@profile
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

@profile
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

def main():
	n = 1000
	
	#start = time.time()
	pr1 = prime_resheto(n)
	#stop = time.time()
	pr2 = prime(n)
	#stop1 = time.time()
	
	#print(stop-start)
	#print(stop1-stop)
	
	print('Искать простые числа до {}'.format(n))
	print('Под список простых выделено {} байт'.format(sys.getsizeof(pr1)))
	print('Под список простых выделено {} байт'.format(sys.getsizeof(pr2)))
	print('Количество простых чисел {}'.format(len(pr1)))

if __name__ == '__main__':
	main()
	#cProfile.run('main()')
	#Заметил, когда в python передаешь параметр -m memory_profiler, 
	# print() некорректно выводит символы кириллицы!
	# поэтому подключил profiler выше
	print('Тестовое сообщение')
	
'''
1. Профилировка	памяти для двух функций
	
	$ python lesson_6.py
Filename: lesson_6.py

Line #    Mem usage    Increment   Line Contents
================================================
    11     14.3 MiB     14.3 MiB   @profile
    12                             def prime_resheto(i):
    13     14.3 MiB      0.0 MiB       a = list(range(2,i+1))
    14     14.3 MiB      0.0 MiB       p = a[0]
    15     14.3 MiB      0.0 MiB       ps = []
    16     14.3 MiB      0.0 MiB       ps.append(p)
    17     14.3 MiB      0.0 MiB       a.remove(p)
    18     14.4 MiB      0.0 MiB       while a:
    19     14.4 MiB      0.0 MiB           for v in range(2*p,i+1,p):
    20     14.3 MiB      0.0 MiB               try:
    21     14.3 MiB      0.0 MiB                   a.remove(v)
    22     14.3 MiB      0.0 MiB               except:
    23     14.3 MiB      0.0 MiB                   pass
    24     14.4 MiB      0.0 MiB           p = a[0]
    25     14.4 MiB      0.0 MiB           ps.append(p)
    26     14.4 MiB      0.0 MiB           a.remove(p)
    27     14.4 MiB      0.0 MiB       return ps


Filename: lesson_6.py

Line #    Mem usage    Increment   Line Contents
================================================
    29     14.4 MiB     14.4 MiB   @profile
    30                             def prime(i):
    31     14.4 MiB      0.0 MiB       ps = [2]
    32     14.4 MiB      0.0 MiB       for v in range(3,i+1):
    33     14.4 MiB      0.0 MiB           prostoe = True
    34     14.4 MiB      0.0 MiB           for uv in ps:
    35     14.4 MiB      0.0 MiB               prostoe = prostoe and (v % uv)
    36     14.4 MiB      0.0 MiB               if not prostoe:
    37     14.4 MiB      0.0 MiB                   break
    38     14.4 MiB      0.0 MiB           if prostoe:
    39     14.4 MiB      0.0 MiB               ps.append(v)
    40     14.4 MiB      0.0 MiB       return ps


Искать простые числа до 1000
Под список простых выделено 1448 байт
Под список простых выделено 1480 байт
Количество простых чисел 168

Вывод: по потреблению памяти две функции практически не отличаются.
Причина: видимо, Python при вызовах .remove() элементы удаляет, но
память при этом по факту не освобождает (prime_resheto()).
С 14 MiB хотелось бы разобраться подробнее, но не пойму как это сделать...
Ведь для списка простых выделено всего то ~1.5KiB

2. Высянение затрат памяти на список простых в зависимости
от верхнего предела простого числа

Выяснилось, что под int Python 64 bit отдает 8 байт (64 бита)
Размер списка при добавлении в него int инкрементируется 
8 байтами:
>>> sys.getsizeof(a)
72
>>> a = [34, 45]
>>> sys.getsizeof(a)
80
>>> a = [34, 45, 39]
>>> sys.getsizeof(a)
88
>>> a = [34, 45, 39, 123]
>>> sys.getsizeof(a)
96



$ python lesson_6.py
Искать простые числа до 100
Под список простых выделено 264 байт
Под список простых выделено 272 байт
Количество простых чисел 25
Тестовое сообщение

$ python lesson_6.py
Искать простые числа до 1000
Под список простых выделено 1448 байт
Под список простых выделено 1480 байт
Количество простых чисел 168
Тестовое сообщение

$ python lesson_6.py
Искать простые числа до 10000
Под список простых выделено 10200 байт
Под список простых выделено 10408 байт
Количество простых чисел 1229
Тестовое сообщение

$ python lesson_6.py
Искать простые числа до 50000
Под список простых выделено 43040 байт
Под список простых выделено 43912 байт
Количество простых чисел 5133
Тестовое сообщение

Анализ последних 4-х измерений показывает, что
средний инкремент-то здесь поболее 8 байт будет (он дробный)
Например, 1448-264=1184 - на столько байт возрос список при
увеличении количества элементов на 168-25=143, но 143*8=1144<1184.
Ну а то, что две функции возвращают одинаковые по содержанию списки,
но память, выделяемая под них, несколько отличается (264 и 272), это загадка...

	'''