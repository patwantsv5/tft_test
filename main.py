import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

# Params
N = 100 # Numbers of samples
L = 1000 # Length of each sample
T = 20 # Width of wave

x = np.empty((N,L),np.float32)
x[:] = np.array(range(L)) + np.random.randint(-4*T, 4*T, N).reshape(N,1)
y -