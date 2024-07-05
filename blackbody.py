import numpy as np
import matplotlib.pyplot as plt

#光速の定義
c=2.99792458
#プランク定数の定義
h=6.62607015
#ボルツマン定数の定義
k=1.380649

plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

v=np.linspace(3,23,10**5)
def f(v,t):
    return np.log10(2*h/c**2) -47 +3*v - np.log10(np.exp(h*10**v/k/10**(t+11))-1)

for i in range(9):
    b=f(v,i)
    la="T=10^"+str(i)+"K"
    plt.plot(v,b, label=la)

plt.xlim(4, 23)
plt.ylim(-21, 15)
plt.xlabel("ν [log10(Hz)]")
plt.ylabel("Bν [log10(erg sec^-1 cm^-2 Hz^-1 ster^-1)]")
plt.xticks(np.arange(4,24,2))
plt.yticks(np.arange(-20,16,4))
plt.legend()
plt.show()