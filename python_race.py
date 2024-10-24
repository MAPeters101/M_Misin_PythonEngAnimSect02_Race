import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

# Set up the duration for your animation
t0=0 # [hrs]
t_end=2 # [hrs]
dt=0.005 # [hrs]

# Create array for time
t=np.arange(t0,t_end+dt,dt)

# Create an x array
a=400
n2=2
x=a*t**n2 # [km]

# Create a y array
altitude=2 # [km]
y=np.ones(len(t))*altitude

# Speed in the x direction
speed_x=n2*a*t**(n2-1)
#################### ANIMATION ####################
frame_amount=len(t)
dot=np.zeros(frame_amount)
n=20
for i in range(0,frame_amount):
    if i==n:
        dot[i]=x[n]
        n+=20
    else:
        dot[i]=x[n-20]

def update_plot(num):

    # 1st subplot
    plane_trajectory.set_data(dot[0:num],y[0:num])

    plane_1.set_data([x[num]-40,x[num]+20],[y[num],y[num]])
    plane_2.set_data([x[num]-20,x[num]],[y[num]+0.3,y[num]])
    plane_3.set_data([x[num]-20,x[num]],[y[num]-0.3,y[num]])
    plane_4.set_data([x[num]-40,x[num]-30],[y[num]+0.15,y[num]])
    plane_5.set_data([x[num]-40,x[num]-30],[y[num]-0.15,y[num]])

    # 2nd subplot
    x_dist.set_data(t[0:num],x[0:num])

    # 3rd subplot
    speed.set_data(t[0:num],speed_x[0:num])


    return plane_trajectory,plane_1,plane_2,plane_3,plane_4,plane_5,\
        x_dist,speed,


fig=plt.figure(figsize=(16,9),dpi=80,facecolor=(0.8,0.8,0.8))
gs=gridspec.GridSpec(2,2)

# Subplot 1
ax0=fig.add_subplot(gs[0,:],facecolor=(0.9,0.9,0.9))

# Line following the airplane
plane_trajectory,=ax0.plot([],[],'r:o',linewidth=2)

# Airplane lines
plane_1,=ax0.plot([],[],'k',linewidth=10)
plane_2,=ax0.plot([],[],'k',linewidth=5)
plane_3,=ax0.plot([],[],'k',linewidth=5)
plane_4,=ax0.plot([],[],'k',linewidth=3)
plane_5,=ax0.plot([],[],'k',linewidth=3)


# Subplot properties
plt.xlim(x[0],x[-1])
plt.ylim(0,y[0]+1)
plt.xticks(np.arange(x[0],x[-1]+1,x[-1]/4),size=15)
plt.yticks(np.arange(0,y[-1]+2,1),size=15)
plt.xlabel('x-distance',fontsize=15)
plt.ylabel('y-distance',fontsize=15)
plt.title('Airplane',fontsize=20)
plt.grid(True)


# Subplot 2
ax2=fig.add_subplot(gs[1,0],facecolor=(0.9,0.9,0.9))
x_dist,=ax2.plot([],[],'-b',linewidth=3,label='X = '+str(a)+'*t^'+str(n2))
plt.xlim(t[0],t[-1])
plt.ylim(x[0],x[-1])
plt.xticks(np.arange(t[0],t[-1]+dt,t[-1]/4))
plt.yticks(np.arange(x[0],x[-1]+1,x[-1]/4))
plt.xlabel('time [hrs]',fontsize=15)
plt.ylabel('x-distance [km]',fontsize=15)
plt.title('X-distance VS time',fontsize=15)
plt.grid(True)
plt.legend(loc='upper left',fontsize='x-large')

# Subplot 3
ax4=fig.add_subplot(gs[1,1],facecolor=(0.9,0.9,0.9))
speed,=ax4.plot([],[],'-b',linewidth=3,label='dX/dt = '+str(n2*a)+'*t^('+str(n2-1)+')')
plt.xlim(t[0],t[-1])
plt.ylim(x[0],speed_x[-1]*2)
plt.xticks(np.arange(t[0],t[-1]+dt,t[-1]/4),size=10)
plt.yticks(np.arange(0,speed_x[-1]*2+1,speed_x[-1]*2/4),size=10)
plt.xlabel('time [hrs]',fontsize=15)
plt.ylabel('speed [km/hr]',fontsize=15)
plt.title('Speed as a function of time',fontsize=15)
plt.grid(True)
plt.legend(loc='upper right',fontsize='x-large')



plane_ani=animation.FuncAnimation(fig,update_plot,frames=frame_amount,interval=20,repeat=True,blit=True)
plt.show()
