import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['axes.prop_cycle'] = matplotlib.cycler(color=['#377eb8',  '#4daf4a','#ff7f00',
                  '#f781bf', '#a65628', '#984ea3',
                  '#999999', '#e41a1c', '#dede00']) 

matplotlib.rc('lines', linewidth=2)
filename = input("Open from : plotdatanew/")
f = open('plotdatanew/' + filename, 'r') # Replace with desired input file name
output = f.read()
output = output.split("\n")
# results = output[1:]
results = output[:]
print(len(results[0].split(",")))
e1 = [float(res.split(",")[0]) for res in results]
e1_iqr = [float(res.split(",")[1])/2 for res in results]
e2 = [float(res.split(",")[2]) for res in results]
e2_iqr = [float(res.split(",")[3])/2 for res in results]
x_list = [float(res.split(",")[4]) for res in results]




l1=[x/e1[0] for x in e1] # Error normalization
l2=[x/e2[0] for x in e2] # Error normalization



r1=[(x_list[0]**3)/(x**3) for x in x_list]
r2=[(x_list[0]**5)/(x**5) for x in x_list]
r3=[(x_list[0]**(0.5))/(x**(0.5)) for x in x_list]




plt.plot(x_list, l1, linestyle='solid', label=r'Random Reshuffle')
plt.plot(x_list, l2, linestyle='solid', label=r'FlipFlop with RR')
plt.plot(x_list, r1, linestyle='dashed', label=r'$1/K^3$')
plt.plot(x_list, r2, linestyle='dashed', label=r'$1/K^5$')
plt.plot(x_list, r3, linestyle='dashed', label=r'$1/K^{0.5}$')

e1_low=list((np.array(e1)-np.array(e1_iqr))/e1[0])
e1_high=list((np.array(e1)+np.array(e1_iqr))/e1[0])
plt.fill_between(x_list,e1_low,e1_high,alpha=.5)

e2_low=list((np.array(e2)-np.array(e2_iqr))/e2[0])
e2_high=list((np.array(e2)+np.array(e2_iqr))/e2[0])
plt.fill_between(x_list,e2_low,e2_high,alpha=.5)

plt.yscale('log')
plt.xscale('log')
plt.legend(loc='lower left',fontsize=18,ncol=2)
plt.xlabel(r'Number of epochs $K$',fontsize=18)
plt.ylabel(r'Normalized error',fontsize=18)

ax1 = plt.gca()
ax1.set_xticks([30, 40, 60, 90, 150, 220, 300])
ax1.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())


plt.savefig(filename + '.pdf')  

