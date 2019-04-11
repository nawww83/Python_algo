# Tested on Python 3.7.3, windows 64 bit

import random as rnd

# Задание 1, Bubble sort
print('\nЗадание 1. Сортировка пузырьком')

n = 50
a = [rnd.randint(-100,100) for i in range(n)]

print('Исходный массив:')
print(a)

def bubble_sort(v, n):
	counter = 0
	for i in range(n):
		for j in range(n - i - 1):
			counter += 1
			if v[j] > v[j + 1]:
				v[j + 1],v[j] = v[j],v[j + 1]
	return counter

def insert_sort(v, n):
	counter = 0
	for i in range(1, n):		
		t = v[i]
		j = i - 1
		while j >= 0 and v[j] > t:
			counter += 1
			v[j + 1] = v[j]
			j -= 1
		v[j + 1] = t
	return counter

def insert_sort_2(v, n):
	counter = 0
	for i in range(1, n):
		t = v[i]
		for j in range(i - 1, -1, -1):
			counter += 1
			if v[j] <= t:
				v[j + 1] = t
				break
			v[j + 1] = v[j]					
		else:
			v[0] = t
	return counter

a_temp = a.copy()
a_temp_2 = a.copy()

print('Сортировка пузырьком:')
nc = bubble_sort(a, n)
print(' Число проходов {}, {}'.format(nc, nc/n/n))
print('Сортировка вставками:')
nc = insert_sort(a_temp, n)
print(' Число проходов {}, {}'.format(nc, nc/n/n))
print('Сортировка вставками 2:')
nc = insert_sort_2(a_temp_2, n)
print(' Число проходов {}, {}'.format(nc, nc/n/n))

print('Отсортированные массивы:')
print(' Пузырьком:')
print(a)
print(' Вставками:')
print(a_temp)
print(' Вставками 2:')
print(a_temp_2)

print('Тест на идентичность списков после работы алгоритмов сортировки:')
print('    ', a == a_temp and a == a_temp_2 and a_temp == a_temp_2)

'''
Вывод: сортировка пузырьком требует 1/2 * N^2 проходов цикла,
сортировка вставками - 1/4 * N^2.
Попытался перевести цикл While на For в алгоритме сортировки вставками,
получился незначительный проигрыш по количеству проходов.
'''

# Задание 2. Merge sort 
print('\nЗадание 2. Сортировка слиянием')

n = 50

# Recursive merge sort
# v - input list
# l - lower bound, u - upper bound
def merge_sort(v, l, u):
	if (l < u):
		h = (l + u) // 2
		merge_sort(v, l, h)
		merge_sort(v, h+1, u)
		merge(v, l, h, u)

# Merge sorted ac and bc into a[l:u+1]
def merge(a, l, h, u):
	#print('Before merge: ', l, lh, u, a)
	ac = a[l : h + 1]
	bc = a[h + 1 : u + 1]
	#print('ac: ', ac, ' bc: ', bc)
	t = []
	while ac and bc:
		if (ac[0] < bc[0]):
			t.append(ac.pop(0))
		else:
			t.append(bc.pop(0))
	#print('t: ', t)
	if ac: # хвост
		t += ac
		#print('tail: ', ac)
	if bc:
		t += bc
		#print('tail: ', bc)
	a[l : u + 1] = t
	#print(' after merge: ', a)

a = [rnd.randint(0,50) for i in range(n)]

print('Исходный массив:')
print(a)

a_temp = a.copy()

nc = merge_sort(a, 0, n)
print('\nОтсортированный массив:')
print(a)

nc = bubble_sort(a_temp, n)
print('Сравнение результата работы сортировки слиянием с результатом \
сортировки пузырьком:')
print('    ', a == a_temp)
