#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 05:46:41 2018

@author: villacorta
"""

import numpy as np
from matplotlib import pyplot

x = np.linspace(4.3, 8*np.pi, 400)
y = np.sin(x)

pyplot.plot(x,y)
pyplot.show()

