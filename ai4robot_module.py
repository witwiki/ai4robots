''' 
@author: Vikram Udyawer
@note: Created on the 24 July 2016
@license: MIT License
@status: In Development
@version: 0.1

@summary: This module is for AI for Robots with Udacity. 
        A list of functions created during the progression of the lessons 
'''

p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    q = []
    for i in range(len(p)):
        '''   Appending values based on the previous position where
            i is the current state and U is the state desired. 
        '''
        q.append(p[(i-U) % len(p)])
    return q

print(move(p, 1))
