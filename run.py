#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
from anh_score import *

# Anharmoonic score of a material
"""
Carbogno et al., Phys. Rev. Mater. 4, 083809
doi = {10.1103/PhysRevMaterials.4.083809},

The anharmonic score for a materail is:
    sigmaA = sigma(F^A)/sigma(F) at each T
    
     sigma(F^A) = 
        Al_300K                 Zr 400K
Sigma  : 0.14883033175544202    0.6297295594467531
SigmaT : 0.24274645161471037    0.7738292582424595

"""

#data_file='F_HARM.dat_300K'
read_file('F_HARM.dat_300K')
