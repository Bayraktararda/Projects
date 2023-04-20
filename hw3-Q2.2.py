# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 16:05:37 2023

@author: Arda
"""
import numpy as np
import random

open_list=[]
copy=[]
cost_matrix=np.array([[np.inf,2,1,np.inf,np.inf],[np.inf,np.inf,1,1,0],[np.inf,1,np.inf,3,np.inf],[np.inf,np.inf,np.inf,np.inf,0],[np.inf,np.inf,np.inf,np.inf,0]])
current_node=0
upper=np.inf
cost=[0,0]
x=1

while True:
    

    #depth first search
    if current_node==0 & x==1:
        #candidate finding
        while True:
            for i in range(5):
                if cost_matrix[current_node,i]!=np.inf: 
                    if [current_node,i] in copy:
                        continue
                    else:
                        open_list.append([current_node,i])
                        copy.append([current_node,i])
            
            
            while True:
                next_step=random.choice(open_list)
                if next_step[0]==current_node:
                    cost[0]=cost_matrix[next_step[0],next_step[1]]
                    cost[1]+=cost_matrix[next_step[0],next_step[1]]
                    open_list.pop(open_list.index(next_step))
                    current_node=next_step[1]
                    break
            
            if current_node==4:
                upper=cost
                x==0
                break
    #if open list empty algortim finishes     
    if not open_list:
            break
    
    
    
    for i in open_list:
        
        if i[0]==current_node-1:
            next_step=i
            
            
            #candidate finding
            for j in range(5):
                if cost_matrix[current_node,j]!=np.inf: 
                    if [current_node,j] in copy:
                        continue
                    else:
                        open_list.append([current_node,j])
                        copy.append([current_node,j])
                break
        
        elif i[0]==current_node-2:
            
            #candidate finding
            for j in range(5):
                if cost_matrix[current_node,j]!=np.inf: 
                    if [current_node,j] in copy:
                        continue
                    else:
                        open_list.append([current_node,j])
                        copy.append([current_node,j])
            
            
        elif i[0]==current_node-3:
            
            #candidate finding
            for i in range(5):
                if cost_matrix[current_node,i]!=np.inf: 
                    if [current_node,i] in copy:
                        continue
                    else:
                        open_list.append([current_node,i])
                        copy.append([current_node,i])
        
        elif i[0]==current_node-4:
            
            #candidate finding
            for i in range(5):
                if cost_matrix[current_node,i]!=np.inf: 
                    if [current_node,i] in copy:
                        continue
                    else:
                        open_list.append([current_node,i])
                        copy.append([current_node,i])
            
        
        
            
            
    
        
    
    
    
    