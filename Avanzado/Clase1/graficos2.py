#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 11:09:26 2019

@author: arianafm
"""
#Figura 2:

import matplotlib.pyplot as plt
import scipy as sp

plt.figure(2)
#linspace : divide el eje
ejeX = sp.linspace(10,50,20)

g = sp.sin(ejeX)

plt.plot(ejeX,g,'r--')

plt.show()