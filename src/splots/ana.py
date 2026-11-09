# ana.py

import numpy as np
import matplotlib as mpl
mpl.use("QtAgg")
import matplotlib.pyplot as plt

import json

##########

def phi_res(path_omega:str,path_T:str,model:str,moduli:str):

    dv = 0.0005
    vs = np.round(np.arange(0.1,0.3,dv),4)

    omegas = np.zeros(len(vs))
    Ts = np.load(f"{path_T}/periods_{model}_{moduli}.npy")

    Phi = np.zeros(len(vs))
    dPhi = np.zeros(len(vs))
   
    # phase
    
    for v_idx,v in enumerate(vs):

        with open(f"{path_omega}/omega_flight_{model}_{moduli}_v={v}.json", "r") as f: data = json.load(f)
        omega = data["omega"]

        omegas[v_idx] = omega
        Phi[v_idx] = omega*Ts[v_idx]    

    # derivative

    for v_idx in range(1,len(vs)-1):

        dPhi[v_idx] = (Phi[v_idx+1] - Phi[v_idx-1])/(2*dv)

    #

    plt.xlabel("$v_\mathrm{in}$")

    plt.plot(vs,omegas,'y-',label="$\omega(v_\mathrm{in})$") 
    plt.xlim([0.1,0.3])
    plt.ylim([1.5,1.75])
    plt.ylabel("$\omega(v)$")
    plt.show()

    plt.plot(vs,Ts,'g-',label="$T(v_\mathrm{in})$") 
    plt.xlim([0.1,0.3])
    plt.ylabel("$T(v)$")
    plt.show()

    plt.plot(vs,Phi,'k-',label="$\Phi(v_\mathrm{in})$")
    plt.xlim([0.1,0.3])
    plt.ylabel("$\Phi(v)$")
    plt.show()

    plt.plot(vs,dPhi,'b--',label="$\mathrm{d} \Phi/\mathrm{d} v$")
    plt.xlim([0.1,0.3])
    plt.ylabel("$\mathrm{d}\Phi / \mathrm{d}v$")
    plt.show()   

    return Phi, dPhi

