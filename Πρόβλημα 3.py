import numpy as np
import matplotlib.pyplot as plt

#Ερώτημα α

print('\n     Ερώτημα α \n')

def Uniform(a,b):
    U = np.random.rand()
    res = (b-a)*U + a
    return res

def f(x): return np.exp(x)

Sf  = 0
Sf2 = 0
n   = 1000
a,b = 0,10

for i in range(n):
    x  = Uniform(a,b)
    y  = f(x)
    Sf += y
    Sf2 += y**2
    
V     = b - a
μf    = Sf/n
σf2   = (n/(n-1))*((Sf2/n) - μf**2)
σf    = σf2**0.5

I  = V*μf
δI = (V*σf)/(n**0.5)
σχετικό_σφάλμα = δI/I

print('I +- dI = %2.2f +- %2.2f' %(I,δI)) 
print('δI/I = %2.5f' %(σχετικό_σφάλμα))




#Ερώτημα β

print('\n     Ερώτημα β \n')

Iexact   = f(10) - f(0)
μfexact  = (f(10) - f(0))/(b-a)
μf2exact = (f(20)-f(0))/((b-a)*2)

σf2exact = μf2exact - μfexact**2
σfexact  = σf2exact**0.5
δIexact  = V*σfexact

σχετικό_exact = δIexact/Iexact

print('I +- dI = %2.2f +- %2.2f' %(Iexact,δIexact))
print('δI/I = %2.5f' %(σχετικό_exact))




#Ερώτημα γ

print('\n     Ερώτημα γ \n')


def many_integ():
    a   = 0
    b   = 10
    n   = 1000
    Sf  = 0  #αρχικοποιώ ξανά στο Σf
    Sf2 = 0 
    
    for i in range(n):
        x  = Uniform(a,b)
        y  = f(x)
        Sf += y
        Sf2 += y**2
   
    V   = b - a
    μf  = Sf/n
    σf2 = (n/(n-1))*((Sf2/n) - μf**2)
    σf  = σf2**2
    I   = V*μf
    δI  = (V*σf)/n**0.5
    σχετικό_σφάλμα = δI/I
    return I

integ_40000 = [many_integ() for i in range(40000)]
plt.hist(integ_40000, bins=100)
plt.show()

#παρατηρώ πως η κατανομή προσεγγίζει την κανονική κατανομή

δI = np.array(integ_40000).std()
print('\nδI = %2.1f' %(δI))

#παρατηρώ πως έχω μικρές διαφορές στα σφάλματα




#Ερώτημα δ

print('\n     Ερώτημα δ \n')

n = 500

Iexact1 =  f(5) - f(0)
μf1     = (f(5) - f(0))/5
μf12    = (1/5)*(1/2)*(f(10)-f(0))

σf12 = μf12 - μf1**2
σf1  = σf12**0.5
δIexact1  = (5*σf1)/n**0.5
σχετικό_exact1 = δIexact1/Iexact1 

Iexact2 =  f(10) - f(5)
μf2     = (f(10) - f(5))/5
μf22    = (1/5)*(1/2)*(f(20)-f(10))

σf22 = μf22 - μf2**2
σf2  = σf22**0.5
δIexact2  = (5*σf2)/n**0.5
σχετικό_exact2 = δIexact2/Iexact2

Iexact_tot        = Iexact1 + Iexact2
δIexact_tot       = δIexact1 + δIexact2
σχετικό_exact_tot = σχετικό_exact1 + σχετικό_exact2

print('I +- δI = %2.2f + %2.2f' %(Iexact_tot,δIexact_tot))
print('δI/I = %2.5f' %(σχετικό_exact_tot))

#βλέπουμε πως δIexact1 + δIexact2 < δIexact (δI του α και β ερωτήματος)
#δηλαδή η αβεβαιότητα μικραίνει όταν στάω το ολοκλήρωμα σε δύο διαστήματα



#Ερώτημα ε

print('\n     Ερώτημα εi \n')
 
a,b = 0,10
n   = 1000
m   = 0

fmax = f(10)
for i in range(n):
    x = Uniform(a,b)
    y = Uniform(0,fmax)
    if y < f(x):
        m += 1
        
V  = (b - a)*(fmax - 0)
p  = m/n
I  = V/p        
δI = (V*((p*(1-p))**0.5))/n**0.5
σχετικό_σφάλμα = δI/I
print('I +- dI = %2.2f +- %2.2f' %(I,δI)) 
print('δI/I = %2.5f' %(σχετικό_σφάλμα))


print('\n     Ερώτημα εii \n')

p2  = (f(10) - f(0))/V
I2   = V/p2        
δI2  = (V*((p2*(1-p2))**0.5))/n**0.5
σχετικό_σφάλμα = δI2/I2
Iexact =  f(10) - f(0)
print('δI = %2.1f' %(δI2))
print('Iexact = %2.1f' %(Iexact))
print('δI/I = %2.5f' %(σχετικό_σφάλμα))


print('\n     Ερώτημα εiii \n')

def int_hitormiss(a,b,n):
    m = 0
    fmax = f(10)
    for i in range(n):
        x = Uniform(a,b)
        y = Uniform(0,fmax)
        if y < f(x):
            m += 1
    
    V  = (b - a)*(fmax - 0)
    p  = m/n
    I  = V/p 
    return I

my_int = [int_hitormiss(0,10,1000) for i in range(0,40000)]
plt.hist(my_int, bins = 100)
plt.show()
δI = np.array(my_int).std()

print('δI = %2.1f' %(δI))








