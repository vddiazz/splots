# field.py

import numpy as np

import matplotlib as mpl
mpl.use("QtAgg")
import matplotlib.pyplot as plt

##########

def plot_origin_field(path:str, typ:str, model:str, moduli:str, dt:np.float64, dx:np.float64) -> None:
    
    # import data   
    jump = 10 
    fs  = np.load(f"{path}/kak_origin_vals_fr_{model}_{moduli}_dt={dt}_dx={dx}.npy").T[::jump,:]
    
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
    yticks      = [int(0), int(tf*1/5.), int(tf*2/5.), int(tf*3/5.), int(tf*4/5.), int(tf)]
    ytick_pos   = [np.argmin(np.abs(yrescaled - val)) for val in yticks]
    
    # figure
    plt.figure(figsize=(10, 5))

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
    xtick_pos   = [np.argmin(np.abs(vs - val)) for val in xticks]
    
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

def plot_a_vals(path:str, typ:str, model:str, moduli:str, dt:np.float64, dx:np.float64) -> None:
     
    jump = 10

    # x axis format
    v_start = 0.1
    v_stop  = 0.3
    step    = 0.0005
    num     = int(round((v_stop - v_start) / step))
    vs      = np.round(np.linspace(v_start, v_start + step * (num - 1), num),4)

    xoriginal   = np.linspace(0, len(vs), len(vs)+1)
    xrescaled   = np.linspace(0.1, 0.3, len(vs)+1)
    xticks      = [0.1, 0.15, 0.2, 0.25, 0.3]
    xtick_pos   = [np.argmin(np.abs(vs - val)) for val in xticks]
    
    # y axis format
    t0  = 0.
    tf  = 150.
    N   = int(tf/dt)
 
    yoriginal   = np.linspace(0, int(N/jump), int(N/jump)+1)
    yrescaled   = np.linspace(0, tf, int(N/jump)+1)
    yticks      = [int(0), int(tf*1/5.), int(tf*2/5.), int(tf*3/5.), int(tf*4/5.), int(tf)]
    ytick_pos   = [np.argmin(np.abs(yrescaled - val)) for val in yticks]
    
    # import data   
    a_vals = np.zeros((num,int(N/jump)))

    for idx,v in enumerate(vs):
        a_temp = np.load(f"{path}/a_v=-{v}_dt={dt}_dx={dx}.npy")[::jump]

        a_vals[idx,:] = a_temp

    # fill nan with 12
    a_vals  = np.nan_to_num(a_vals, nan=12.)

    # figure
    plt.figure(figsize=(10, 5))

    plt.minorticks_on()
    
    plt.xticks(xtick_pos, xticks)
    plt.yticks(ytick_pos, yticks)
   
    plt.xlim([0,num]) 
    plt.ylim([0,N/jump])

    plt.xlabel(r'$v_\mathrm{in}$')
    plt.ylabel(r'$t$')
    plt.title(f'$a(t)$ for {moduli}')
    
    plt.imshow(a_vals.T, vmin=-1.5, vmax=12., aspect='auto', origin='lower',  cmap='Spectral')
    plt.colorbar()
    plt.tight_layout()
    plt.show()

def plot_da_vals(path:str, typ:str, model:str, moduli:str, dt:np.float64, dx:np.float64) -> None:
     
    jump = 10

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
 
    yoriginal   = np.linspace(0, int(N/jump), int(N/jump)+1)
    yrescaled   = np.linspace(0, tf, int(N/jump)+1)
    yticks      = [int(0), int(tf*1/5.), int(tf*2/5.), int(tf*3/5.), int(tf*4/5.), int(tf)]
    ytick_pos   = [np.argmin(np.abs(yrescaled - val)) for val in yticks]
    
    # import data   
    da_vals = np.zeros((num,int(N/jump)))

    for idx,v in enumerate(vs):
        da_temp = np.load(f"{path}/b_v=-{v}_dt={dt}_dx={dx}.npy")[::jump]

        da_vals[idx,:] = da_temp

    # figure
    plt.figure(figsize=(10, 5))

    plt.minorticks_on()
    
    plt.xticks(xtick_pos, xticks)
    plt.yticks(ytick_pos, yticks)
   
    plt.xlim([0,num]) 
    plt.ylim([0,N/jump])

    plt.xlabel(r'$v_\mathrm{in}$')
    plt.ylabel(r'$t$')
    plt.title(f'$v(t)$ for {moduli}')
    
    plt.imshow(da_vals.T, vmin=-1.5, vmax=1.5, aspect='auto', origin='lower',  cmap='Spectral')
    plt.colorbar()
    plt.tight_layout()
    plt.show()

#def plot_ff_origin_field(path:str, model:str, dt:np.float64, dx:np.float64) -> None:
  
    # get from ff_fractal_plot.py

##########

def ff_moduli_extract(path:str, model:str, vin:np.float64, dt:np.float64, dx:np.float64) -> None:
    
    tf = 150.

    # import data   
    f  = np.load(f"{path}/kak_ff_{model}_v={vin}.npy")

    X = np.arange(-15,15,dx)

    T = np.arange(0.,tf,dt)

    tol = 1e-2

    # energy
    Dx = np.zeros((len(X),len(T)))
    for i in range(1,len(X)-1):
        for j in range(len(T)):
            Dx[i,j] = (f[i+1,j]-f[i-1,j])/(2*dx)

    Dt = np.zeros((len(X),len(T)))
    for i in range(len(X)):
        for j in range(1,len(T)-1):
            Dt[i,j] = (f[i,j+1]-f[i,j-1])/(2*dt)

    E = np.zeros((len(X),len(T)))
    for i in range(1,len(X)-1):
        for j in range(1,len(T)-1):
            E[i,j] = 0.5*Dt[i,j]**2 - 0.5*Dx[i,j]**2 + (1-f[i,j]**2)**2

    # separation
    a = np.zeros(len(T))

    for t in range(len(T)):
        indices_a = np.where(np.abs(f[:,t]) < tol)[0]
        if len(indices_a) == 2:
            a[t] = abs(X[indices_a[0]] - X[indices_a[1]])/2.
        else:        
            a[t] = np.nan

    # velocity   
    v = np.zeros(len(T))    

    for t in range(1,len(T)-1):
        v[t] = (a[t+1]-a[t-1])/2*dt

    # figure
    plt.figure(figsize=(10, 5))

    plt.minorticks_on()
    
    plt.xlim([0,tf]) 
    plt.ylim([-1.5,10.5])

    plt.xlabel(r'$t$')
    plt.ylabel(r'Moduli')
    
    plt.plot(T,a,'r.',label=r"$a(t)$")
    plt.plot(T,v,'k.',label=r"$\dot{a}(t)$")
    plt.tight_layout()
    plt.show()

    print(a)
    print(v)


