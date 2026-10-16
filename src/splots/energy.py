# moduli.py

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from matplotlib import rc

rc('font', **{'family': 'serif', 'serif': ['Computer Modern'], 'size': 12})
rc('text', usetex=True)

mpl.use("QtAgg")

##########

def plot_energy(moduli_labels:list[str], path:str, model:str, moduli:str, vin:np.float64, dt:np.float64, dx:np.float64) -> None:

    reds = ["#FFCCCC","#FF9999","#FF6666","#FF3333","#FF0000","#E60000","#CC0000","#990000","#660000"]

    # load data
    T = np.load(f"{path}/T_v=-{vin}_dt={dt}_dx={dx}.npy")
    V = np.load(f"{path}/V_v=-{vin}_dt={dt}_dx={dx}.npy")
    E = np.load(f"{path}/E_v=-{vin}_dt={dt}_dx={dx}.npy")
        
    # time axis
    time = np.arange(0,len(E),1)
    
    # plots
    k = 1
    for i,Mi in enumerate(moduli_labels):
        for j, Mj in enumerate(moduli_labels):
            plt.plot(time,T[:,i,j],color=reds[::-1][k],linestyle='-',label=fr"$T_{{{moduli_labels[i]}{moduli_labels[j]}}}(t)$")
            k = k+1

    plt.plot(time,V,'b-',label=r'$V(t)$')

    plt.plot(time,E,'k--',label=r'$E(t)$')

    plt.title(f"$v_\mathrm{{in}} = {vin}$")
 
    # x axis format
   
    t0 = 0; tf = 150
    N = len(E)
    
    xoriginal = np.linspace(0, N, N+1)
    xrescaled = np.linspace(0, N*dt, N+1)
    xticks = [0, N*dt*1/5, N*dt*2/5, N*dt*3/5, N*dt*4/5, N*dt]
    xtick_pos = [np.argmin(np.abs(xrescaled - val)) for val in xticks]
    plt.minorticks_on()
    plt.xticks(xtick_pos, xticks)
    plt.xlabel(r"$t$")

    # axis limits
    plt.xlim([0,N+1])
    plt.ylim([-1.,3.5])

    # plot
    plt.legend(facecolor='white', edgecolor='black', fancybox=False)
    plt.show()
