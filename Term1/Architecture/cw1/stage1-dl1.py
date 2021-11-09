import matplotlib.pyplot as plt
import numpy as np

# stage2: dl1
asso = np.array([1,2,4,8])
pwr_nsets_1 = np.array([
    10.2003,
    9.2662,
    8.9010,
    8.8962,
])
pwr_nsets_2 = np.array([
    9.2691,
    8.8963,
    8.7741,
    8.7947,
])
pwr_nsets_4 = np.array([
    8.9929,
    8.7331,
    8.7007,
    8.8021,
])
pwr_nsets_8 = np.array([
    8.8482,
    8.6901,
    8.7131,
    8.8506,
])
pwr_nsets_16 = np.array([
    8.7681,
    8.6952,
    8.7661,
    8.9517,
])
pwr_nsets_32 = np.array([
    8.7604,
    8.7511,
    8.8761,
    9.1478,
])
pwr_nsets_64 = np.array([
    8.7944,
    8.8874,
    9.1049,
    9.5511,
])
pwr_nsets_128 = np.array([
    8.9055,
    9.0801,
    9.4833,
    10.1175,
])
plt.plot(asso, pwr_nsets_1, 'o-', label = 'dl1.nsets=1')
plt.plot(asso, pwr_nsets_2, 'o-', label = 'dl1.nsets=2')
plt.plot(asso, pwr_nsets_4, 'o-', label = 'dl1.nsets=4')
plt.plot(asso, pwr_nsets_8, '*-', label = 'dl1.nsets=8')
for i in range(asso.size):
    plt.text(asso[i], pwr_nsets_8[i], '%.2lf' % pwr_nsets_8[i])
plt.plot(asso, pwr_nsets_16, 'o-', label = 'dl1.nsets=16')
plt.plot(asso, pwr_nsets_32, 'o-', label = 'dl1.nsets=32')
plt.plot(asso, pwr_nsets_64, 'o-', label = 'dl1.nsets=64')
plt.plot(asso, pwr_nsets_128, 'o-', label = 'dl1.nsets=128')
plt.xlabel('dl1 associativity')
plt.ylabel('Total Energy $(10^8nJ)$')
plt.title('dl1.block_size=32')
plt.legend()
plt.show()