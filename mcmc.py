import numpy as np
import random
import matplotlib.pyplot as plt
def gaussian(x, mu = 0.5, sigma = 0.1):
    return 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-(x-mu)**2 / (2*sigma**2))

def mcmc_uniform_gaussian(sample_num = 10000, skip_num = 1000):
    x_0 = 0
    i = 0
    sample_list = []
    j = 0
    while len(sample_list) < sample_num:
        while True:
            x_1  = random.random()
            q_i = gaussian(x_0)
            q_j = gaussian(x_1)
            alpha = min(q_j / q_i, 1.0)
            r = random.random()
            if r <= alpha:
                x_0 = x_1
                if j >= skip_num: #到达稳态之后再进行取样
                    sample_list.append(x_0)
                    break
                j += 1

    return sample_list


samples = mcmc_uniform_gaussian()
print(len(samples))
plt.figure()
plt.hist(samples)
plt.show()