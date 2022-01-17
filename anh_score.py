#!/usr/bin/env python3
#for i in $(seq 1 1 10); do echo $i; done
#echo chi=10
import matplotlib.pyplot as plt
import numpy as np
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
def read_file(data_file): 
  f = np.loadtxt(data_file)
  f_har=f[:,1]
  f_ai =f[:,2] 
  f_anh=f[:,3]
  n=f_har.size
  meanf_anh= np.mean(f_anh)
  meanf_ai = np.mean(f_ai)
  meansqf_anh=np.mean(f_anh**2)
  meansqf_ai =np.mean(f_ai**2)
  anh_score=np.std(f_anh)/np.std(f_ai)
  return print("Anharmonic score : ", anh_score)
#data_file='F_HARM.dat_300K'
#read_file(data_file)

