import torch

eye = torch.eye(3)
print(eye)
''' result 
tensor([[ 1.,  0.,  0.],
        [ 0.,  1.,  0.],
        [ 0.,  0.,  1.]])
'''

print(eye.size())
''' result
torch.Size([3, 3])
'''

print(eye.size()[0])
''' result
3
'''