# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 11:49:59 2023

@author: Arda
"""
import numpy as np
states=[0,1]
decision=[0,1]
decion_cost=np.array(([40,150],[0,20]))
probability=np.array([[[0.4,0.6],[1,0]],[[0.7,0.3],[0.4,0.6]]])
backward_step=4

decision_matrix=np.zeros((backward_step,len(states)))

j_matrix=np.matrix(np.ones((backward_step,len(states))) * np.inf)

for i in range(backward_step):
    for s in states:
        for u in decision:
            if i==0:
                cost=(probability[s,u,1]*-100)+decion_cost[s,u]
                if j_matrix[i,s]>cost:
                    j_matrix[i,s]=cost
                    decision_matrix[i,s]=u
            else:
                cost=(probability[s,u,1]*(-100+j_matrix[i-1,1]))+decion_cost[s,u]+(probability[s,u,0]*j_matrix[i-1,0])
                if j_matrix[i,s]>cost:
                    j_matrix[i,s]=cost
                    decision_matrix[i,s]=u

