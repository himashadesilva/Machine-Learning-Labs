import matplotlib
import matplotlib.pyplot as plt
import numpy as np


matplotlib.rc('xtick',labelsize = 30)
matplotlib.rc('ytick',labelsize = 30)
matplotlib.rc('axes',titlesize = 30)
matplotlib.rc('legend', fontsize = 30)

fig = plt.figure(figsize=(10,10))
fig.subplots_adjust(hspace = 0.5)

axes = plt.subplot(5,1,1)

x = np.linspace(0,10,100)
y = np.cos(x)
axes.plot(x,y,linewidth=4.0, ls='--',color='r',marker="o")
axes.legend("cos(x)",loc="upper right")
axes.set_title("Title for (5,1)subplot")
axes.set_xlabel('xlabel')
axes.set_ylabel('ylabel')

axes.set_autoscaley_on(False)
axes.set_ylim([0,-1])
axes.xaxis.set(ticks = range(1,10))

#plt.savefig('cosine.png', dpi = 400 ,bbpx_inches='tight')

plt.show(axes)