# tested in Python 3.7.3 on Windows

from collections import defaultdict
from collections import Counter

# Задание 1
print('\nЗадание 1')
n = int(input('Введите число предприятий:'))

dc = Counter(defaultdict(float))
for i in range(n):
	dt = input('Введите название предприятия:')
	print('Введите через Enter прибыль за 4 квартала:')
	for i in range(4):
		dc[dt] += float(input())

avs = sum(dc.values()) / len(dc)
print('Средняя прибыль всех предприятий:{0:.2f}'.format(avs))

print('Предприятия с прибылью ниже (или равной) средней:')
dc_less = Counter({ x: count for x, count in dc.items() if dc[x] <= avs })
for k, v in dc_less.items():
    print(' ', k, 'с прибылью', v)

print('Предприятия с прибылью выше средней:')
for k, v in (dc - dc_less).items(): # Использовали вычитание
    print(' ', k, 'с прибылью', v)
