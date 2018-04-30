#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 05:57:57 2018

@author: villacorta
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def finIntersection(fun1, fun2, x0):
    return fsolve(lambda x: fun1(x) - fun2(x), x0)

x = np.linspace(0, 45, 10000)
myfunc = lambda x: np.cos(x/5) * np.sin(x/2)
linefunc = lambda x: 0.01*x - 0.5





























































































