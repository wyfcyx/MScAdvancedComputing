import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

asso = np.array([0,1,2,3,4,5,6,7,8])
total_nsets_1 = np.array([
    11.5541,
    11.4298,
    11.4917,
    11.5190,
    9.8872,
    9.9615,
    10.4668,
    10.8041,
    13.5213,
])
total_nsets_2 = np.array([
    11.4014,
    11.4347,
    11.4050,
    9.6919,
    9.5860,
    9.7710,
    9.4396,
    10.8468,
])
total_nsets_4 = np.array([
    11.3901,
    10.5831,
    9.5939,
    9.4080,
    9.3967,
    8.7601,
    9.5080,
])
total_nsets_8 = np.array([
    10.1678,
    9.5280,
    9.4155,
    8.9291,
    8.4654,
    8.9217,
])
total_nsets_16 = np.array([
    9.4765,
    9.3602,
    8.6936,
    8.3231,
    8.6295,
])
total_nsets_32 = np.array([
    9.3397,
    8.5402,
    8.2637,
    8.4902,
    8.9438,
])
total_nsets_64 = np.array([
    8.3746,
    8.2704,
    8.4560,
    8.8307,
    9.5808,
])
total_nsets_128 = np.array([
    8.4258,
    8.4261,
    8.7605,
    9.3102,
    10.5195,
])
total_nsets_256 = np.array([
    8.4244,
    8.7187,
    9.1770,
    9.8150,
    11.2963,
])
plt.plot(asso[:total_nsets_1.size], total_nsets_1, 'o-', label = 'il1.nsets=1')
plt.plot(asso[:total_nsets_2.size], total_nsets_2, 'o-', label = 'il1.nsets=2')
plt.plot(asso[:total_nsets_4.size], total_nsets_4, 'o-', label = 'il1.nsets=4')
plt.plot(asso[:total_nsets_8.size], total_nsets_8, 'o-', label = 'il1.nsets=8')
plt.plot(asso[:total_nsets_16.size], total_nsets_16, 'o-', label = 'il1.nsets=16')
plt.plot(asso[:total_nsets_32.size], total_nsets_32, 'o-', label = 'il1.nsets=32')
plt.plot(asso[:total_nsets_64.size], total_nsets_64, 'o-', label = 'il1.nsets=64')
plt.plot(asso[:total_nsets_128.size], total_nsets_128, 'o-', label = 'il1.nsets=128')
plt.plot(asso[:total_nsets_256.size], total_nsets_256, 'o-', label = 'il1.nsets=256')
plt.text(0, total_nsets_128[0], '%.2lf' % total_nsets_128[0])
plt.text(1, total_nsets_64[1], '%.2lf' % total_nsets_64[1])
plt.text(2, total_nsets_32[2], '%.2lf' % total_nsets_32[2])
plt.text(3, total_nsets_16[3], '%.2lf' % total_nsets_16[3])
plt.text(4, total_nsets_8[4], '%.2lf' % total_nsets_8[4])
plt.text(5, total_nsets_4[5], '%.2lf' % total_nsets_4[5])
plt.text(6, total_nsets_2[6], '%.2lf' % total_nsets_2[6])
plt.text(7, total_nsets_1[7], '%.2lf' % total_nsets_1[7])
convex = np.array([
    total_nsets_128[0],
    total_nsets_64[1],
    total_nsets_32[2],
    total_nsets_16[3],
    total_nsets_8[4],
    total_nsets_4[5],
    total_nsets_2[6],
    total_nsets_1[7],
])
curve = make_interp_spline(asso[:convex.size], convex)
X = np.linspace(0, 8, 500)
Y = curve(X)
plt.plot(X, Y, '--', label = 'il1.nsets*il1.associavity=128')
plt.xlabel('$\log_2$(il1.associativity)')
plt.ylabel('Total Energy$(10^8nJ)$')
plt.title('il1.block_size=32')
plt.legend()
plt.show()