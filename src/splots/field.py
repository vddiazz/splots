# moduli.py

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from matplotlib import rc

rc('font', **{'family': 'serif', 'serif': ['Computer Modern'], 'size': 12})
rc('text', usetex=True)

mpl.use("QtAgg")

##########

def plot_origin_field(path:str, model:str, moduli:str, dt:np.float64) -> None:
    
    # import data   
    jump = 10 
    fs  = np.load(f"{path}/kak_origin_vals_fr_{model}_{moduli}_dt={dt}.npy").T[::jump,:]
    
    # fill nan with 1
    fs  = np.nan_to_num(fs, nan=1.0)

    # x axis format
    v_start = 0.1
    v_stop  = 0.3
    step    = 0.0005
    num     = int(round((v_stop - v_start) / step))
    vs      = np.round(np.linspace(v_start, v_start + step * (num - 1), num),4)

    xoriginal   = np.linspace(0, len(vs), len(vs)+1)
    xrescaled   = np.linspace(0.1, 0.3, len(vs)+1)
    xticks      = [0.1, 0.15, 0.2, 0.25, 0.3]
    xtick_pos   = [np.argmin(np.abs(xrescaled - val)) for val in xticks]
    
    # y axis format
    t0  = 0.
    tf  = 150.
    N   = int(tf/dt)
 
    yoriginal   = np.linspace(0, len(fs[:,0]), len(fs[:,0])+1)
    yrescaled   = np.linspace(0, tf, len(fs[:,0])+1)
    yticks      = [0, tf*1/5., tf*2/5., tf*3/5., tf*4/5., tf]
    ytick_pos   = [np.argmin(np.abs(yrescaled - val)) for val in yticks]
    
    # figure
    plt.figure(figsize=(12, 6))

    plt.minorticks_on()
    
    plt.xticks(xtick_pos, xticks)
    plt.yticks(ytick_pos, yticks)
   
    plt.xlim([0,num]) 
    plt.ylim([0,N/jump])

    plt.xlabel(r'$v_\mathrm{in}$')
    plt.ylabel(r'$t$')
    plt.title(f'{moduli}')
    
    plt.imshow(fs, vmin=-1.25, vmax=1.25, aspect='auto', origin='lower',  cmap='Spectral')
    plt.colorbar()
    plt.tight_layout()
    plt.show()

def plot_gamma_comp(path:str, model:str, moduli:str, dt:np.float64) -> None:
    
    # import data   
    jump    = 10 
    gs      = np.load(f"{path}/gamma_vals_{model}_{moduli}_dt={dt}.npy").T[::jump,:]

    # x axis format
    v_start = 0.1
    v_stop  = 0.3
    step    = 0.0005
    num     = int(round((v_stop - v_start) / step))
    vs      = np.round(np.linspace(v_start, v_start + step * (num - 1), num),4)

    xoriginal   = np.linspace(0, len(vs), len(vs)+1)
    xrescaled   = np.linspace(0.1, 0.3, len(vs)+1)
    xticks      = [0.1, 0.15, 0.2, 0.25, 0.3]
    xtick_pos   = [np.argmin(np.abs(xrescaled - val)) for val in xticks]
    
    # y axis format
    t0  = 0.
    tf  = 150.
    N   = int(tf/dt)
 
    yoriginal   = np.linspace(0, len(gs[:,0]), len(gs[:,0])+1)
    yrescaled   = np.linspace(0, tf, len(gs[:,0])+1)
    yticks      = [0, tf*1/5., tf*2/5., tf*3/5., tf*4/5., tf]
    ytick_pos   = [np.argmin(np.abs(yrescaled - val)) for val in yticks]

    # compute diff
    gss = np.zeros_like(gs)
    
    for v_idx,v in enumerate(vs):
        gss[:,v_idx] = 1/np.sqrt(1-v**2) - gs[:,v_idx] 
    
    # figure
    plt.figure(figsize=(12, 6))

    plt.minorticks_on()
    
    plt.xticks(xtick_pos, xticks)
    plt.yticks(ytick_pos, yticks)
   
    plt.xlim([0,num]) 
    plt.ylim([0,N/jump])

    plt.xlabel(r'$\gamma(v_\mathrm{{in}}) - \gamma(t)$')
    plt.ylabel(r'$t$')
    plt.title(f'{moduli}')
    
    plt.imshow(gss, vmin=-1.25, vmax=1.25, aspect='auto', origin='lower',  cmap='Spectral')
    plt.colorbar()
    plt.tight_layout()
    plt.show()
