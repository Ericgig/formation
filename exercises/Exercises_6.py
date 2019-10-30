# -*- coding: utf-8 -*-
"""
@author: EG
"""

# 1 Choix multiple

# 1.1 Code:
f = 0
k = 0

def f2k(f):
  k = ((f-32)*(5.0/9.0)) + 273.15
  return k

f2k(8)
f2k(41)
f2k(32)

print(k)

#a 259.81666666666666
#b 287.15
#c 273.15
#d 0

# 1.2 Code:
a = 3
b = 7

def swap(a, b):
    temp = a
    a = b
    b = temp

swap(a, b)

print(a, b)

#a 7 3
#b 3 7
#c 3 3
#d 7 7

# 1.3 Code:
def numbers(one, two=2, three, four=4):
    n = str(one) + str(two) + str(three) + str(four)
    return n

print(numbers(1, three=3))

#a 1234
#b one2three4
#c 1239
#d SyntaxError

# 1.3 Code:
def func(a, b = 3, c = 6):
  print('a: ', a, 'b: ', b,'c:', c)

func(-1, 2)
#a a: b: 3 c: 6
#b a: -1 b: 3 c: 6
#c a: -1 b: 2 c: 6
#d a: b: -1 c: 2


# 2 Créez les fonctions suivantes:
fence('name', '*') -> *name*
outer('helium') -> hm


arr = array([4,6,8,7,4])
rescale(arr) -> [0,0.5,1,0.75,0.25]
#rescale retourne un array avec les valeurs entre 0 et 1 de façon à ce que max(arr)->1, min(arr)->0 

rescale(arr,low = 1, high = 3) -> [1,2,3,2.5,1.5]
#rescale retourne un array avec les valeurs entre low et high 

#Documentez rescale
help(rescale)