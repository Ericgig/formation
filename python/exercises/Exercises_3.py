# -*- coding: utf-8 -*-
"""
@author: EG
"""

import numpy as np

# 1 Slicing 
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
# Si primes[0:12:3] = [2, 7, 17, 29]
# et primes[2:12:3] = [5, 13, 23, 37]

# Comment obtenir "I notpssgre ntesae" à partir de
beatles = "In an octopus's garden in the shade"

# 2 list vs array
# Les 2 loop suivante donne le même output:
print('list')
liste = list(range(3))
for i in liste:
    print(i)
    
print('array')
array = np.arange(3)
for i in array:
    print(i)

#Mais les loops suivante ne donne pas le même résultat, pourquoi?
print('list')
for i in liste*2:
    print(i)
    
print('array')
for i in array*2:
    print(i)

# 3 Utilisez une loop pour tranformer un mot en list
# "Hello" -> ['H','e','l','l','o']


