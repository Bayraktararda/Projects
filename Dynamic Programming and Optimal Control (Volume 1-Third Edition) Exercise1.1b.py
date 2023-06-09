# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 22:55:22 2023

@author: Arda
"""


import numpy as np

number_of_steps=4
decisions=[0,1,2,3,4,5]
states=[0,1,2,3,4,5]

total_cost=np.zeros((number_of_steps,len(states)))
j_matrix=np.matrix(np.ones((number_of_steps,len(states))) * np.inf)
decision_matrix=np.zeros((number_of_steps,len(states)))
cost=0

for i in range(number_of_steps):
    
    for s in states:
        
        for u in decisions:
            if s+u>5:
                continue
            else:
                if i==0:
                    if s+u==5:
                        if j_matrix[i,s]>s**2+u**2:
                            j_matrix[i,s]=s**2+u**2
                            decision_matrix[i,s]=u
                else:
                    if j_matrix[i,s]>s**2+u**2+j_matrix[i-1,(s+u)]:
                        j_matrix[i,s]=s**2+u**2+j_matrix[i-1,(s+u)]
                        decision_matrix[i,s]=u
