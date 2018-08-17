import numpy as np

def NN(m1, m2, w1, w2, b):

    z = m1 * w1 + m2 * w1 + b
    return sigmoid(z)

def sigmoid(x):

    return 1 / (1 + np.exp(-x))

w1 = np.random.rand()
w2 = np.random.rand()
b = np.random.rand()

result = NN(2, 1, w1, w2, b)

print(result)

