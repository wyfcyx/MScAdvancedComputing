import matplotlib.pyplot as plt
import numpy as np

# stage1: ruu & lsq
def plot_ruu(
    ruu,
    log_ruu,
    sim_ipc,
    ruu_full,
    lsq_full,
    totpwr
):
    ax1 = plt.subplot(311)
    plt.plot(log_ruu, sim_ipc, '*-')
    plt.ylabel('IPC')
    for i in range(0,log_ruu.size):
        plt.text(log_ruu[i], sim_ipc[i], '%.2lf' % sim_ipc[i])
    plt.title('LSQ  size=%d' % ruu)

    ax2 = plt.subplot(312)
    plt.plot(log_ruu, ruu_full, '*-', label='ruu_full')
    plt.plot(log_ruu, lsq_full, '*-', label='lsq_full')
    plt.ylabel('Probability')
    plt.legend()

    ax3 = plt.subplot(313)
    plt.plot(log_ruu, totpwr, '*-')
    plt.xlabel(r'$\log_2(\mathrm{RUU size})$')
    plt.ylabel(r'$\mathrm{Total Energy}(10^8nJ)$')
    for i in range(0,log_ruu.size):
        plt.text(log_ruu[i], totpwr[i], '%.2lf' % totpwr[i])

    plt.savefig('lsq_%d.png' % ruu)
    plt.cla()

log_ruu = np.array([1,2,3,4,5,6,7,8])
sim_ipc = np.array([0.4505, 0.7022, 0.9465, 1.1133, 1.1128, 1.1128, 1.1128, 1.1128])
ruu_full = np.array([
        .9736, .9535, .9248, .3927, .0001, .0000, .0000, .0000
])
lsq_full = np.array([
        .0000, .0000, .0000, .6400, .8044, .8044, .8044, .8044
])
totpwr = np.array([
        14.1375,
        11.8550,
        10.5830,
        9.8871,
        10.9935,
        12.3398,
        14.5444,
        18.8403,
])
#plot_ruu(8, log_ruu, sim_ipc, ruu_full, lsq_full, totpwr)
sim_ipc = np.array([.4505, .7022, .9465, 1.1261, 1.3740, 1.3824, 1.3824, 1.3824])
ruu_full = np.array([.9736, .9535, .9248, .8850, .1611, .0000, .0000, .0000])
lsq_full = np.array([.0000, .0000, .0000, .0000, .5129, .6175, .6175, .6175])
totpwr = np.array([
    14.1753,
    11.9001,
    10.6338,
    9.4833,
    9.8806,
    10.9078,
    12.6941,
    16.1830,
])
#plot_ruu(16, log_ruu, sim_ipc, ruu_full, lsq_full, totpwr)
sim_ipc = np.array([.4505, .7022, .9465, 1.1261, 1.4181, 1.7749, 1.7761, 1.7761])
ruu_full = np.array([.9736, .9535, .9248, .8850, .6809, .0850, .0000, .0000])
lsq_full = np.array([.0000, .0000, .0000, .0000, .0000, .3554, .3989, .3989])
totpwr = np.array([
    14.2523,
    11.9906,
    10.7359,
    9.5753,
    9.7562,
    9.8484,
    11.4212,
    14.5536,
])
#plot_ruu(32, log_ruu, sim_ipc, ruu_full, lsq_full, totpwr)
sim_ipc = np.array([.4505, .7022, .9465, 1.1261, 1.4181, 1.7606, 1.9467, 1.9465])
ruu_full = np.array([.9736, .9535, .9248, .8850, .6809, .4595, .0246, .0000])
lsq_full = np.array([.0000, .0000, .0000, .0000, .0000, .0000, .2385, .2564])
totpwr = np.array([
    14.4096,
    12.1737,
    10.9409,
    9.7600,
    9.9223,
    10.0698,
    11.4796,
    14.5693,
])
#plot_ruu(64, log_ruu, sim_ipc, ruu_full, lsq_full, totpwr)
sim_ipc = np.array([.4505, .7022, .9465, 1.1261, 1.4181, 1.7606, 1.9964, 2.0637])
ruu_full = np.array([.9736, .9535, .9248, .8850, .6809, .4595, .2123, .0263])
lsq_full = np.array([.0000, .0000, .0000, .0000, .0000, .0000, .0000, .0035])
totpwr = np.array([
    14.7363,
    12.5467,
    11.3541,
    10.1328,
    10.2384,
    10.3797,
    11.8736,
    14.9993,
])
#plot_ruu(128, log_ruu, sim_ipc, ruu_full, lsq_full, totpwr)
