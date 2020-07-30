import random
import numpy as np
import matplotlib.pyplot as plt
mu = 0.5 # 期望
sigma = 0.1  # 方差
skip = 700 # 收敛步数
num = 10000 # 采样点数

# Gaussian 表示待采样函数
def Gaussian(x):
    return 1/(sigma*np.sqrt(2*np.pi)) * np.exp(-(x-mu)**2 /(2*sigma**2))

# M_H 算法
def M_H():
    x_0 = 0
    samples = []
    j = 1
    while len(samples) <= num:
        if j < 800:
            print(j)
        while True:
            x_next = random.random()  # 转移函数
            q_j = Gaussian(x_next)
            q_i = Gaussian(x_0)
            alpha = min(q_j / q_i, 1.0)
            u = random.random()    # 阈值的采样函数
            if u <= alpha:
                x_0 = x_next
                if j >= skip:
                    samples.append(x_next)
                j += 1
                break
    return samples
norm_samples = M_H()
print(len(norm_samples))
plt.hist(norm_samples)
plt.show()