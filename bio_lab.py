import numpy as np
import matplotlib.pyplot as plt

time = np.array([0,10,20,30,40,50])

disc_1_0 = np.array([0,6,6,9.2,9.2,14.1])
disc_1_1 = np.array([0,1.9,1.9,5.4,5.6,9.3])
disc_1_0_g = np.gradient(disc_1_0)/10
disc_1_1_g = np.gradient(disc_1_1)/10

disc_2_0 = np.array([0,7,10.01,13.8,16.9,20.1])
disc_2_1 = np.array([0,7.1,10.3,12.5,14.7,19.3])
disc_2_0_g = np.gradient(disc_2_0)/10
disc_2_1_g = np.gradient(disc_2_1)/10

disc_3_0 = np.array([0,17.8,18.7,19.6,19.6,27.3])
disc_3_1 = np.array([0,17.8,22.2,26.6,31.6,36.4])
disc_3_0_g = np.gradient(disc_3_0)/10
disc_3_1_g = np.gradient(disc_3_1)/10

disc_4_0 = np.array([0,11.7,28.6,35.7,47,47])
disc_4_1 = np.array([0,10.1,17.8,24.2,28,32.8])
disc_4_0_g = np.gradient(disc_4_0)/10
disc_4_1_g = np.gradient(disc_4_1)/10

disc_1 = np.average([disc_1_0,disc_1_1],axis=0)
disc_2 = np.average([disc_2_0,disc_2_1],axis=0)
disc_3 = np.average([disc_3_0,disc_3_1],axis=0)
disc_4 = np.average([disc_4_0,disc_4_1],axis=0)
disc_1_g = np.average([disc_1_0_g,disc_1_1_g],axis=0)
disc_2_g = np.average([disc_2_0_g,disc_2_1_g],axis=0)
disc_3_g = np.average([disc_3_0_g,disc_3_1_g],axis=0)
disc_4_g = np.average([disc_4_0_g,disc_4_1_g],axis=0)


std_1 = np.std([disc_1_0,disc_1_1],axis=0)
std_2 = np.std([disc_2_0,disc_2_1],axis=0)
std_3 = np.std([disc_3_0,disc_3_1],axis=0)
std_4 = np.std([disc_4_0,disc_4_1],axis=0)
std_1_g = np.std([disc_1_0_g,disc_1_1_g],axis=0)
std_2_g = np.std([disc_2_0_g,disc_2_1_g],axis=0)
std_3_g = np.std([disc_3_0_g,disc_3_1_g],axis=0)
std_4_g = np.std([disc_4_0_g,disc_4_1_g],axis=0)

fig_0, bar_slope = plt.subplots()
fig_1, rate_fit = plt.subplots()
fig_2, grad_fit = plt.subplots()
fig_3, (ax_real,ax_rate) = plt.subplots(2)

# VOLUME GRAPH
ax_real.errorbar(time,disc_1,yerr=std_1,label="1 Disc",capsize=2)
ax_real.errorbar(time,disc_2,yerr=std_2,label="2 Discs",capsize=2)
ax_real.errorbar(time,disc_3,yerr=std_3,label="3 Discs",capsize=2)
ax_real.errorbar(time,disc_4,yerr=std_4,label="4 Discs",capsize=2)

ax_real.fill_between(time, disc_1+std_1, disc_1-std_1,alpha=0.3, fc='#089FFF')
ax_real.fill_between(time, disc_2+std_2, disc_2-std_2,alpha=0.3, fc='#FF8419')
ax_real.fill_between(time, disc_3+std_3, disc_3-std_3,alpha=0.3, fc='#65BC85')
ax_real.fill_between(time, disc_4+std_4, disc_4-std_4,alpha=0.3, fc='#D62728')

ax_real.legend()
ax_real.set_title("Volume of gas vs. time")
ax_real.set_xlabel("Time (s)")
ax_real.set_ylim(0,50)
ax_real.set_xlim(0,50)
ax_real.set_ylabel("Volume (mL)")

# RATE GRAPH
ax_rate.errorbar(time,disc_1_g,yerr=std_1_g,label="1 Disc",capsize=2)
ax_rate.errorbar(time,disc_2_g,yerr=std_2_g,label="2 Discs",capsize=2)
ax_rate.errorbar(time,disc_3_g,yerr=std_3_g,label="3 Discs",capsize=2)
ax_rate.errorbar(time,disc_4_g,yerr=std_4_g,label="4 Discs",capsize=2)

ax_rate.fill_between(time, disc_1_g+std_1_g, disc_1_g-std_1_g,alpha=0.3, fc='#089FFF')
ax_rate.fill_between(time, disc_2_g+std_2_g, disc_2_g-std_2_g,alpha=0.3, fc='#FF8419')
ax_rate.fill_between(time, disc_3_g+std_3_g, disc_3_g-std_3_g,alpha=0.3, fc='#65BC85')
ax_rate.fill_between(time, disc_4_g+std_4_g, disc_4_g-std_4_g,alpha=0.3, fc='#D62728')
ax_rate.legend()
ax_rate.set_title("Rate of gas production vs. time")
ax_rate.set_xlabel("Time (s)")
ax_rate.set_ylabel("Rate (mL/s)")

# BAR GRAPH
a1_0,b = np.polyfit(time,disc_1_0,1)
a1_1,b = np.polyfit(time,disc_1_1,1)

a2_0,b = np.polyfit(time,disc_2_0,1)
a2_1,b = np.polyfit(time,disc_2_1,1)

a3_0,b = np.polyfit(time,disc_3_0,1)
a3_1,b = np.polyfit(time,disc_3_1,1)

a4_0,b = np.polyfit(time,disc_4_0,1)
a4_1,b = np.polyfit(time,disc_4_1,1)

data = np.array([[a1_0,a1_1],[a2_0,a2_1],[a3_0,a3_1],[a4_0,a4_1]])
color = ['#089FFF','#FF8419','#65BC85','#D62728']

bar_slope.bar(["1 Disc","2 Discs","3 Discs","4 Discs"],np.average(data,axis=1),capsize=2,color=color,yerr=np.std(data,axis=1))
bar_slope.yaxis.grid(True, linestyle='--', which='major',color='grey', alpha=.25)
bar_slope.set_title("Slope of Best Fit Line for Volume of Gas vs. Time")


a,b,c = np.polyfit(time,disc_1,2)
rate_fit.plot(time,a*time*time+b*time,label="1 Disc Best Fit", ls="--",color='#089FFF')
grad_fit.plot(time,np.gradient(a*time*time+b*time)/10,label="1 Disc LoBF Slope", ls="--",color='#089FFF')

a,b,c = np.polyfit(time,disc_2,2)
rate_fit.plot(time,a*time*time+b*time,label="2 Disc Best Fit", ls="--",color='#FF8419')
grad_fit.plot(time,np.gradient(a*time*time+b*time)/10,label="2 Disc LoBF Slope", ls="--",color='#FF8419')

a,b,c = np.polyfit(time,disc_3,2)
rate_fit.plot(time,a*time*time+b*time,label="3 Disc Best Fit", ls="--",color='#65BC85')
grad_fit.plot(time,np.gradient(a*time*time+b*time)/10,label="3 Disc LoBF Slope", ls="--",color='#65BC85')

a,b,c = np.polyfit(time,disc_4,2)
rate_fit.plot(time,a*time*time+b*time,label="4 Disc Best Fit", ls="--",color='#D62728')
grad_fit.plot(time,np.gradient(a*time*time+b*time)/10,label="4 Disc LoBF Slope", ls="--",color='#D62728')

rate_fit.legend()
rate_fit.set_title("Volume of Reaction vs. Time (Best Fit Curves)")
rate_fit.set_xlabel("Time (s)")
rate_fit.set_ylabel("Volume (mL)")
rate_fit.grid(True, linestyle='--', which='major',color='grey', alpha=.25)

grad_fit.legend()
grad_fit.set_title("Rate of Reaction vs. Time (Slope of LoBF)")
grad_fit.set_xlabel("Time (s)")
grad_fit.set_ylabel("Rate (mL/s)")
grad_fit.grid(True, linestyle='--', which='major',color='grey', alpha=.25)



plt.tight_layout()
plt.show()
