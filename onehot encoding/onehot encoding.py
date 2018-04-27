import torch
import numpy as np


num_classes = 5
a = np.array([3,4])
onehot = torch.eye( num_classes )[a]
print(onehot)
''' result
tensor([[ 0.,  0.,  0.,  1.,  0.],
        [ 0.,  0.,  0.,  0.,  1.]])
'''