# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 14:15:48 2023

@author: Arda
"""
import numpy as np

cost_matrix=np.array([[np.inf,30,60,25,np.inf,np.inf],[np.inf,np.inf,np.inf,np.inf,np.inf,50],[np.inf,np.inf,np.inf,35,np.inf,np.inf],[np.inf,np.inf,np.inf,np.inf,15,np.inf],[np.inf,np.inf,np.inf,np.inf,np.inf,15]])
shape=np.shape(cost_matrix)
j_matrix=np.zeros((step_size,shape[0]))
u_matrix=np.zeros((step_size,shape[0]))
step_size=6


for s in range(step_size,-1,-1):
    u=u_matrix[s+1,current]
    prevcost=j_matrix[s+1,current]
    for jump in range(shape[0]):
      costn=cost_matrix[current,jump]+j_matrix[(s+1),jump]
      if costn<prevcost:
        prevcost=costn
        u=jump
    u_matrix[s,current]=u
    j_matrix[s,current]=prevcost
    
        
        
    
    