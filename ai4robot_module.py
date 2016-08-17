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
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1


def sense(p, Z):
    '''
    Description:
    
    Args:
        p (array of integers): All possible states of the robot including its current
        
    '''
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    '''
    Description:
    
    Args:
        p (array of integers): All possible states of the robot including its current
        U (int): Desired position the robot wants to move
    '''
    # q represents the new array/vector of states accounting for the desired position and its probability 
    q = []
    for i in range(len(p)):
        pos = pExact * p[(i-U)%len(p)]
        ''' 
            (i-U) represents the previous position in the p array
            when divided by the length of the array or probable positions it can move
            the remainder represents the current position of the q array based on the index of p
            here the -1 and +1 added to (i-U) to increase(overshoot) and decrease(undershoot)
            the index of p. This p index would be the current state/element in the array of q.
            Multiplied by the probability of course and add to account for additional probabilities.
            See notes in your notebook on the explanation you looked up
        '''
        pos = pos + pUndershoot * p[(i-U+1)%len(p)]
        pos = pos + pOvershoot * p[(i-U-1)%len(p)]
        # final probabilistic based position
        q.append(pos)

    return q

print(move(p, 1))
# print(str(-1 % 4))
# print(str(0 % 4))
# print(str(1 % 4))
# print(str(2 % 4))
