import numpy as np
import matplotlib.pyplot as plt


def step_fun():
    x = 1
    y = 0
    z = complex(x,y)
    U = np.random.rand()
    if 0.25 < U < 0.50 : z = complex(0,1)
    if 0.50 < U < 0.75 : z = complex(-1,0)
    if 0.75 < U < 1.00 : z = complex(0,-1)
    return z

n = 1000 
N = 100 
xarray = [] 
yarray = [] 

for i in range(n):
    z = 0
    for i in range(N):
        z  += step_fun()
    xarray += [z.real]
    yarray += [z.imag]

plt.figure(1)
plt.hist(xarray, bins = range(-60,61), color= 'b')
plt.title('κίνηση στον x άξονα για 1000 σωματίδια')
plt.figure(2)
plt.hist(yarray, bins = range(-60,61), color= 'y')
plt.title('κίνηση στον y άξονα για 1000 σωματίδια')
plt.figure(3)
plt.scatter(xarray,yarray, color= 'g')
plt.title('συνολική κίνηση των σωματιδίων')

#για την μέση τιμή και την τυπική απόκλιση

xarray = np.array(xarray)
print('Ο μέσος όρος της απόστασης που διανύεται στον x άξονα είναι = ', xarray.mean(), 'και η τυπική απόκλιση = ', xarray.std())
yarray = np.array(yarray)
print('Ο μέσος όρος της απόστασης που διανύεται στον y άξονα είναι = ', yarray.mean(), 'και η τυπική απόκλιση = ', yarray.std())



