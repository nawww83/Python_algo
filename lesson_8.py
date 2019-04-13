# tested on Python 3.5.2
# Задание 1

print('\nЗадание 1')

import hashlib
import random

n = 10

s = ''.join( [chr(random.randint(ord('a'),ord('z'))) for _ in range(n)] )

print('Строка \n', s)

from collections import defaultdict

def n_sub(v, n):
    d = defaultdict(int)
    for i in range(n):
        for j in range(n-i):
            #print(s[j:i+j+1])
            h = hashlib.sha1(s[j:i+j+1].encode('utf-8')).hexdigest()
            d[h] += 1
    return d

d = n_sub(s, n)
#print(d)

print('Количество различных подстрок в строке: {}'.format(len(d)))
