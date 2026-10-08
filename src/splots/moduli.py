# moduli.py

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from matplotlib import rc

rc('font', **{'family': 'serif', 'serif': ['Computer Modern'], 'size': 12})
rc('text', usetex=True)

mpl.use("QtAgg")

##########

def plot_moduli(moduli_labels:list[str], path:str, model:str, moduli:str, vin:np.float64, dt:np.float64, dx:np.float64) -> None:

    colors = ["r","k","g","b","y","m"]

    # load data
    if moduli == "aB":
        a   = np.load(f"{path}/a_v=-{vin}_dt={dt}_dx={dx}.npy")
        da  = np.load(f"{path}/da_v=-{vin}_dt={dt}_dx={dx}.npy")
        b   = np.load(f"{path}/b_v=-{vin}_dt={dt}_dx={dx}.npy")
        db  = np.load(f"{path}/db_v=-{vin}_dt={dt}_dx={dx}.npy")
        
        M = [a,da,b,db]

    if moduli == "maB":
        a   = np.load(f"{path}/a_v=-{vin}_dt={dt}_dx={dx}.npy")
        da  = np.load(f"{path}/da_v=-{vin}_dt={dt}_dx={dx}.npy")
        b   = np.load(f"{path}/b_v=-{vin}_dt={dt}_dx={dx}.npy")
        db  = np.load(f"{path}/db_v=-{vin}_dt={dt}_dx={dx}.npy")
        
        M = [a,da,b,db]

    if moduli == "pR":
        a   = np.load(f"{path}/a_v=-{vin}_dt={dt}_dx={dx}.npy")
        da  = np.load(f"{path}/da_v=-{vin}_dt={dt}_dx={dx}.npy")
        c1   = np.load(f"{path}/b_v=-{vin}_dt={dt}_dx={dx}.npy")
        dc1  = np.load(f"{path}/db_v=-{vin}_dt={dt}_dx={dx}.npy")
        
        M = [a,da,c1,dc1]

    if moduli == "mpR":
        a   = np.load(f"{path}/a_v=-{vin}_dt={dt}_dx={dx}.npy")
        da  = np.load(f"{path}/da_v=-{vin}_dt={dt}_dx={dx}.npy")
        c1   = np.load(f"{path}/b_v=-{vin}_dt={dt}_dx={dx}.npy")
        dc1  = np.load(f"{path}/db_v=-{vin}_dt={dt}_dx={dx}.npy")
        
        M = [a,da,c1,dc1]

    if moduli == "pR2":
        a   = np.load(f"{path}/a_v=-{vin}_dt={dt}_dx={dx}.npy")
        da  = np.load(f"{path}/da_v=-{vin}_dt={dt}_dx={dx}.npy")
        c1   = np.load(f"{path}/c1_v=-{vin}_dt={dt}_dx={dx}.npy")
        dc1  = np.load(f"{path}/dc1_v=-{vin}_dt={dt}_dx={dx}.npy")
        c2   = np.load(f"{path}/c2_v=-{vin}_dt={dt}_dx={dx}.npy")
        dc2  = np.load(f"{path}/dc2_v=-{vin}_dt={dt}_dx={dx}.npy")

        M = [a,da,c1,dc1,c2,dc2]

    if moduli == "mpR2":
        a   = np.load(f"{path}/a_v=-{vin}_dt={dt}_dx={dx}.npy")
        da  = np.load(f"{path}/da_v=-{vin}_dt={dt}_dx={dx}.npy")
        c1   = np.load(f"{path}/c1_v=-{vin}_dt={dt}_dx={dx}.npy")
        dc1  = np.load(f"{path}/dc1_v=-{vin}_dt={dt}_dx={dx}.npy")
        c2   = np.load(f"{path}/c2_v=-{vin}_dt={dt}_dx={dx}.npy")
        dc2  = np.load(f"{path}/dc2_v=-{vin}_dt={dt}_dx={dx}.npy")
        
        M = [a,da,c1,dc1,c2,dc2]

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

def plot_vout(path:str, typ:str, model:str, moduli:str, dt:np.float64, dx:np.float64) -> list[np.float64]:

    v_start = 0.1
    v_stop = 0.3
    step = 0.0005
    num = int(round((v_stop - v_start) / step))
    vs = np.round(np.linspace(v_start, v_start + step * (num - 1), num),4)

    t0 = 0.
    tf = 150.
    N = int(tf/dt)

    #

    fs = np.load(f"{path}/kak_origin_vals_{typ}_{model}_{moduli}_dt={dt}_dx={dx}.npy")

    vouts = []
    for idx,vin in enumerate(vs):
        a = np.load(f"{path}/a_v=-{vin}_dt={dt}_dx={dx}.npy")
        v = np.load(f"{path}/da_v=-{vin}_dt={dt}_dx={dx}.npy")

        idx_max = next((i for i, x in enumerate(a) if x >= 12), len(a))

        v_sect = v[idx_max-50000:idx_max] # take big enough range!

        if max(abs(v_sect)) > 0.35:
            vout = 0.
        else:
            vout = abs(np.average(v_sect))

        vouts.append(float(vout))

    # plot

    plt.figure(figsize=(10, 2.5))
    plt.minorticks_on()

    plt.xlabel(r'$v_\mathrm{in}$')
    plt.ylabel(r'$v_\mathrm{out}$')
    plt.title(f'{moduli}')

    plt.xlim([0.1,0.3])
    plt.ylim([0.,0.4])

    #

    plt.plot(vs,vouts,"r-")

    #

    R = np.arange(0.1,0.3,0.0005)

    plt.plot(R,R,"k--")

    #

    plt.tight_layout()
    plt.show()

    return vouts
