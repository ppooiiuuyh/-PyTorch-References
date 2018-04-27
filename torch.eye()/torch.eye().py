import torch
import numpy as np

eye = torch.eye(3)
print(eye)
''' result 
tensor([[ 1.,  0.,  0.],
        [ 0.,  1.,  0.],
        [ 0.,  0.,  1.]])
'''

eye  = torch.eye(3,m= 2)
print(eye)
''' result
tensor([[ 1.,  0.],
        [ 0.,  1.],
        [ 0.,  0.]])
'''


eye = torch.eye(4)[ [2,1,3] ]
print(eye)
''' result 
tensor([[ 0.,  0.,  1.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  0.,  0.,  1.]])
'''


torch.eye(4,out = eye)
print(eye)
''' result 
tensor([[ 1.,  0.,  0.,  0.],
        [ 0.,  1.,  0.,  0.],
        [ 0.,  0.,  1.,  0.],
        [ 0.,  0.,  0.,  1.]])
'''

eye = np.reshape(torch.eye(4) , [2,-1])
print(eye)
''' result 
tensor([[ 1.,  0.,  0.,  0.,  0.,  1.,  0.,  0.],
        [ 0.,  0.,  1.,  0.,  0.,  0.,  0.,  1.]])
'''