# moduli.py

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from matplotlib import rc

rc('font', **{'family': 'serif', 'serif': ['Computer Modern'], 'size': 12})
rc('text', usetex=True)

mpl.use("QtAgg")

##########

def plot_moduli(moduli_labels:list[str], path:str, model:str, moduli:str, vin:np.float64, dt:np.float64) -> None:

    colors = ["r","k","g","b","y","m"]

    # load data
    if moduli == "aB":
        a   = np.load(f"{path}/a_v=-{vin}.npy")
        da  = np.load(f"{path}/da_v=-{vin}.npy")
        b   = np.load(f"{path}/b_v=-{vin}.npy")
        db  = np.load(f"{path}/db_v=-{vin}.npy")
        
        M = [a,da,b,db]

    # time axis
    T = np.arange(0,len(M[0]),1)
    
    # plots
    for i,Mi in enumerate(M):
        plt.plot(T,Mi,f'{colors[i]}-',label=fr"${moduli_labels[i]}$")

    plt.title(f"$v_\mathrm{{in}} = {vin}$")
 
    # x axis format
   
    t0 = 0; tf = 150
    N = int(tf/dt)
    
    xoriginal = np.linspace(0, N, N+1)
    xrescaled = np.linspace(0, N*dt, N+1)
    xticks = [0, N*dt*1/5, N*dt*2/5, N*dt*3/5, N*dt*4/5, N*dt]
    xtick_pos = [np.argmin(np.abs(xrescaled - val)) for val in xticks]
    plt.minorticks_on()
    plt.xticks(xtick_pos, xticks)
    plt.xlabel(r"$t$")

    # axis limits
    plt.xlim([0,N+1])
    plt.ylim([-2,12])

    # plot
    plt.legend(facecolor='white', edgecolor='black', fancybox=False)
    plt.show()
