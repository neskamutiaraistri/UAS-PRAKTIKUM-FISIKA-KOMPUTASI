import numpy as np
def PosisiParabolaKetikaT(t):
    h0 = 0
    alpha = np.radians(90)
    g = 9.8
    v0 = 2

    v0x = v0*np.cos(alpha)
    v0y = v0*np.sin(alpha)

    ##"Jarak Horizontal Maksimum = ",X," m"
    X = ((v0**2)*np.sin(2*alpha))/(2*g)
    ##"Jarak Vertikal Maksimum = ",Y," m")
    Y = ((v0**2)*(np.sin(alpha)**2))/(2*g)
    ##"Waktu Mencapai Jarak Horizontal Maksimum = ",T," s")
    T = (2*v0*np.sin(alpha))/g     

    #t = np.arange(0.0, T, 0.01)

    y = h0 + v0y*t - 0.5*g*t**2
    x = v0x*t

    print(t,',',round(x,2),',',round(y,2))
    '''
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set(xlabel='x (m)', ylabel= 'y (m)' , title='Grafik Gerak Parabola')
    ax.grid()
    plt.show()
    '''
print( 't , x , y')
for i in range(0,17):
    t = 0.1*i
    PosisiParabolaKetikaT(round(t,2))
