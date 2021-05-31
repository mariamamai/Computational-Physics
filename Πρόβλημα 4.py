import numpy as np

def Uniform(a,b):
    U = np.random.rand()
    res = (b-a)*U + a
    return res

#Ερώτημα α

print('\n     Ερώτημα α \n')

def plate_mass(x,y):
    return (20/13.)*(x+y)

N   = 1000
m   = 0
Sf  = 0
Sf2 = 0

for i in range(N):
    x = Uniform(0,1)
    y = Uniform(0,1)
    if x >= 0 and y <= 1 and y <= x**2:
        m   += 1
        Sf  = plate_mass(x,y)
        Sf2 += plate_mass(x,y)**2
        
V   = m/N
μf  = Sf/m       
σf2 = (m/(m-1))*((Sf2/m) - μf**2) 
σf  = σf2**0.5
I   = V*μf
δI  = (V*σf)/m**0.5

print('V = %2.3f'%(V))
print('I = %2.3f +/- %2.3f'%(I,δI))


#Ερώτημα β

print('\n     Ερώτημα β \n')

def Uniform(a,b):
    U = np.random.rand()
    res = (b-a)*U + a
    return res

def cube_mass(x,y,z):
    return (12/31)*(x**2 + y*z)

N   = 1000
n   = 0
Sf  = 0
Sf2 = 0

for i in range(N):
    x = Uniform(0,1)
    y = Uniform(1,2)
    z = Uniform(1,2)
    if x >= 0 and x <= 1 and y >= 1 and y <= 2 and z >= 1 and z <= 2:
        n   += 1
        Sf  += cube_mass(x,y,z)
        Sf2 += cube_mass(x,y,z)**2
    
V   = n/N
μf  = Sf/n
σf2 = (n/(n-1))*(Sf2/n - μf**2)
σf  = σf2**0.5
I   = V*μf
δI   = V*σf/n**0.5

print('V = %2.3f'%(V))
print('I = %2.4f +/- %2.4f'%(I,δI))



