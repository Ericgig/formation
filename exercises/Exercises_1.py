# -*- coding: utf-8 -*-
"""
@author: EG
"""

import numpy
import glob
import matplotlib


# 1 Échange de valeur
a = 1
b = 2
a,b = b,a
#Que vallent a et b maintenant?

# 2 Slicing avec des indices négatives
atome = "Oxygène"
# Que donne atome[-3], atome[:-3], atome[-3:]?


# 3 Le  script suivant présente la moyenne, le max et le min des données d'inflammation
#   Modifiez le pour ajouter la dérivation standart (std) 
#    et affichez les 4 graphiques dans une grille 2x2 
data = numpy.loadtxt('C:/Users/EG/python/python-novice-inflammation-data\inflammation-01.csv',delimiter=',')

fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.plot(numpy.mean(data, axis=0),"ko:")

axes2.set_ylabel('max')
axes2.plot(numpy.max(data, axis=0),"r*-")

axes3.set_ylabel('min')
axes3.plot(numpy.min(data, axis=0),"gx--")

fig.tight_layout()

matplotlib.pyplot.show()

