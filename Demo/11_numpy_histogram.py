import numpy as np
import matplotlib.pyplot as plt

rg = np.random.default_rng(1)
mu, sigma = 2, 0.5
v = rg.normal(mu, sigma, 10_000)

# plot histogram
plt.hist(v, bins=50, density=1)
# plt.show()

# plot outline
(n, bins) = np.histogram(v, bins=50, density=True)
# print(f'n = {n}')
# print(f'bins = {bins}')
# print(f'bins[1:] = {bins[1:]}')
# print(f'bins[:-1] = {bins[:-1]}')
plt.plot(.5 * (bins[1:] + bins[:-1]), n)

# display plot
plt.show()
