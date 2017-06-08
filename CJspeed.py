
import numpy as np
from cantera import *
from SDToolbox import *

from matplotlib.pylab import *

# Ethylene-Oxygen
Tmin = 300
Tmax = 800
Pmin = 101325
Pmax = 405300
fimin = float(0.2)
fimax = float(1.5)

q = 'C2H4:1 O2:3';
mech = 'gri30_highT.cti';

# Number of iterations
npoints = 20

Ti = np.zeros(npoints, 'd')
Pi = np.zeros(npoints, 'd')
fi = np.zeros(npoints, 'd')
Tcj = np.zeros(npoints, 'd')
s = np.zeros(npoints, 'd')
Pcj = np.zeros(npoints, 'd')
vcj = np.zeros(npoints, 'd')


#######################Temperature function###############
for i in range(npoints):
    Ti[i] = Tmin + (Tmax - Tmin) * i / (npoints - 1)
    [cj_speed, R2] = CJspeed(101325, Ti[i], q, mech, 0)
    gas = PostShock_eq(cj_speed, 101325, Ti[i], q, mech)
    vcj[i] = gas.density
    Pcj[i] = gas.P / 100000
    Tcj[i] = gas.T
    s[i] = cj_speed
    print 'CJ Speed is %.2f m/s' % s[i]

# creates plot temperature CJ
plot(Ti,s, '-', color = 'orange')
xlabel(r'Ti [K]', fontsize=20)
ylabel("V [m\s]")
title(r'CJ speed (Ti)',
fontsize=22,horizontalalignment='center')
axis([200,1000,2300,2400])
grid()
#show()
savefig('CJ_T.png', bbox_inches='tight')

# creates plot temperature CJ
plot(Ti,Tcj, '-', color = 'orange')
xlabel(r'Ti [K]', fontsize=20)
ylabel("Temperature CJ [K]")
title(r'Temperature CJ (Ti)',
fontsize=22,horizontalalignment='center')
axis([200,1000,3700,4000])
grid()
#show()
savefig('CJ_Tcj.png', bbox_inches='tight')

# creates plot pressure CJ
plot(Ti,Pcj, '-', color = 'orange')
xlabel(r'Ti [K]', fontsize=20)
ylabel("Pressure CJ [bar]")
title(r'Pressure CJ (Ti)',
fontsize=22,horizontalalignment='center')
axis([200,1000,10,35])
grid()
#show()
savefig('CJ_Pcj.png', bbox_inches='tight')

# creates plot density CJ
plot(Ti,vcj, '-', color = 'orange')
xlabel(r'Ti [K]', fontsize=20)
ylabel("Density CJ [kg/m3]")
title(r'Density CJ (Ti)',
fontsize=22,horizontalalignment='center')
axis([200,1000,0.5,2.5])
grid()
#show()
savefig('CJ_rocj.png', bbox_inches='tight')

for i in range(npoints):
    Pi[i] = Pmin + (Pmax - Pmin) * i / (npoints - 1)
    [cj_speed, R2] = CJspeed(Pi[i], 300, q, mech, 0)
    gas = PostShock_eq(cj_speed, Pi[i], 300, q, mech)
    vcj[i] = gas.density
    Pcj[i] = gas.P / 100000
    Tcj[i] = gas.T
    s[i] = cj_speed
    print 'CJ Speed is %.2f m/s' % s[i]

# creates plot CJ speed
plot(Pi,s, '-', color = 'orange')
xlabel(r'Pi [Pa]', fontsize=20)
ylabel("V [m\s]")
title(r'CJ speed (P)',
fontsize=22,horizontalalignment='center')
axis([80000,420000,2300,2500])
grid()
#show()
savefig('CJ_P.png', bbox_inches='tight')

# creates plot temperature CJ
plot(Pi,Tcj, '-', color = 'orange')
xlabel(r'Pi [Pa]]', fontsize=20)
ylabel("Temperature CJ [K]")
title(r'Temperature CJ (Pi)',
fontsize=22,horizontalalignment='center')
axis([80000,420000,3800,4400])
grid()
#show()
savefig('CJ_Tcj2.png', bbox_inches='tight')

# creates plot pressure CJ
plot(Pi,Pcj, '-', color = 'orange')
xlabel(r'Pi [Pa]', fontsize=20)
ylabel("Pressure CJ [bar]")
title(r'Pressure CJ (Pi)',
fontsize=22,horizontalalignment='center')
axis([80000,420000,20,150])
grid()
#show()
savefig('CJ_Pcj2.png', bbox_inches='tight')

# creates plot density CJ
plot(Pi,vcj, '-', color = 'orange')
xlabel(r'Pi [Pa]', fontsize=20)
ylabel("Density CJ [kg/m3]")
title(r'Density CJ (Pi)',
fontsize=22,horizontalalignment='center')
axis([80000,420000,1,11])
grid()
#show()
savefig('CJ_rocj2.png', bbox_inches='tight')
#######################Fi function###############
for i in range(npoints):
    fi[i] = fimin + (fimax - fimin) * i / (npoints - 1)
    no = float(2 / fi[i])  # Number of O2 moles
    q = 'CH4:1 O2:' + str(no)
    [cj_speed, R2] = CJspeed(101325, 300, q, mech, 0)
    gas = PostShock_eq(cj_speed, 101325, 300, q, mech)
    vcj[i] = gas.density
    Pcj[i] = gas.P / 100000
    Tcj[i] = gas.T
    s[i] = cj_speed
    print 'CJ Speed is %.2f m/s' % s[i]

# creates plot CJ speed
plot(fi,s, '-', color = 'orange')
xlabel(r'phi [-]', fontsize=20)
ylabel("V [m\s]")
title(r'CJ speed (fi)',
fontsize=22,horizontalalignment='center')
axis([float(0.0),float(1.8),1600,2800])
grid()
#show()
savefig('CJ_fi.png', bbox_inches='tight')

# creates plot temperature CJ
plot(fi,Tcj, '-', color = 'orange')
xlabel(r'phi [-]', fontsize=20)
ylabel("Temperature [K]")
title(r'Temperature CJ(phi)',
fontsize=22,horizontalalignment='center')
axis([float(0.0),float(1.8),2000,4000])
grid()
#show()
savefig('CJ_Tcj3.png', bbox_inches='tight')

# creates plot pressure CJ
plot(fi,Pcj, '-', color = 'orange')
xlabel(r'phi [-]', fontsize=20)
ylabel("Pressure CJ [bar]")
title(r'Pressure CJ(phi)',
fontsize=22,horizontalalignment='center')
axis([float(0.0),float(1.8),15,35])
grid()
#show()
savefig('CJ_Pcj3.png', bbox_inches='tight')

# creates plot density CJ
plot(fi,vcj, '-', color = 'orange')
xlabel(r'phi [-]', fontsize=20)
ylabel("Density CJ [kg/m3]")
title(r'Density CJ (phi)',
fontsize=22,horizontalalignment='center')
axis([float(0.0),float(1.8),1,2.5])
grid()
#show()
savefig('CJ_rocj3.png', bbox_inches='tight')
