import torch

tensors1 = torch.randn((10,1))
tensors2 = torch.randn((10,1))
print(tensors1)
print(tensors2)
'''
tensor([[-0.2597],
        [ 1.5007],
        [-0.0675],
        [ 1.8926],
        [-0.6182],
        [-1.3026],
        [-1.8432],
        [-1.2632],
        [-1.1295],
        [-1.0896]])
tensor([[ 1.1837],
        [-0.1587],
        [ 1.3663],
        [ 1.3077],
        [ 0.8071],
        [-0.5317],
        [-0.4326],
        [ 0.0545],
        [ 0.6399],
        [ 0.0967]])
        
'''

random_perm = torch.randperm(10)
print(random_perm)
print(random_perm.size())
'''
tensor([ 9,  1,  5,  6,  7,  4,  8,  2,  0,  3])
torch.Size([10])
'''

tensors1 = tensors1[random_perm]
tensors2 = tensors2[random_perm]
print(tensors1)
print(tensors2)

'''
tensor([[-1.0896],
        [ 1.5007],
        [-1.3026],
        [-1.8432],
        [-1.2632],
        [-0.6182],
        [-1.1295],
        [-0.0675],
        [-0.2597],
        [ 1.8926]])
tensor([[ 0.0967],
        [-0.1587],
        [-0.5317],
        [-0.4326],
        [ 0.0545],
        [ 0.8071],
        [ 0.6399],
        [ 1.3663],
        [ 1.1837],
        [ 1.3077]])
'''