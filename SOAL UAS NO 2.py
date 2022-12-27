# SOAL NOMOR 2
import numpy as np
import matplotlib.pyplot as plt
print("Soal 2:")
print("Perhitungan jarak horizontal atau vertikal pada gerak parabola")
print("x = V0^2sin2(alpha)/2g (bekerja di command window)")

#Penyelesaian
print("Penyelesaian:")
#Diketahui
alpha = np.radians(45)
g = 9.8 #Percepatan gravitasi (m/s^2)
V0 = 2 #Kecepatan awal (m/s)

V0x = V0*np.cos(alpha) #Kecepatan awal pada sumbu-x (m/s)
V0y = V0*np.sin(alpha) #Kecepatan awal pada sumbu-y (m/s)

X = ((V0**2)*np.sin(2*alpha))/(g) #h terjauh
print("Jarak horizontal maksimum = ",X," m")
Y = ((V0**2)*(np.sin(alpha)**2))/(2*g) #h maksimum
print("Jarak vertikal maksimum = ",Y," m")
T = (2*V0*np.sin(alpha))/g #t terjauh
print("Waktu mencapai jarak horizontal maksimum = ",T," s")
print("\n")

t = np.arange(0.0, T, 0.01)
y = V0y*t - 0.5*g*t**2
x = V0x*t

plt.plot(x, y) #menampilkan grafik sin dan cos
plt.title('Grafik gerak parabola') #nama grafiknya
plt.xlabel('x (m)') #memberi label
plt.ylabel('y (m)') #memberi label
plt.grid(True) #memberi batas
plt.show() #menampilkan grafik
