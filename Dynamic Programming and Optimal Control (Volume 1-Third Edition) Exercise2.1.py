# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 15:13:19 2023

@author: Arda
"""

import numpy as np
cost_matrix=np.array([[np.inf,4,1,5,np.inf,8],[np.inf,np.inf,1,1,np.inf,np.inf],[np.inf,np.inf,np.inf,np.inf,5,9],[np.inf,np.inf,np.inf,np.inf,np.inf,2],[np.inf,np.inf,0,np.inf,np.inf,5],[np.inf,np.inf,np.inf,np.inf,np.inf,0]])
step=5
shape=np.shape(cost_matrix)
j_matrix=np.zeros((step,shape[0]))
u_matrix=np.zeros((step,shape[0]))
j_matrix[4,:]=[np.inf,np.inf,np.inf,np.inf,np.inf,0]
costn=0


for s in range(3,-1,-1):

  for current in range(shape[0]):
    u=u_matrix[s+1,current]
    prevcost=j_matrix[s+1,current]
    for jump in range(shape[0]):
      costn=cost_matrix[current,jump]+j_matrix[(s+1),jump]
      if costn<prevcost:
        prevcost=costn
        u=jump
    u_matrix[s,current]=u
    j_matrix[s,current]=prevcost
    
    


print(j_matrix)
print(u_matrix)
