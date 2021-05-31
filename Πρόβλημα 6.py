import numpy as np
import mpmath as mp

#Ερώτημα 1α

print('\n     Ερώτημα 1α \n')

def f(x): 
    return np.tan(x) - x/(1-x**2)

a = 2  
b = 4
n = 0  
e = 1.e-100
while( b - a > e and n < 15):
    c = 0.5*(a + b)
    if f(c)*f(b) < 0:
        a = c
    else: 
        b = c
    n += 1

print('Μετά από n = ', n,'επαναλήψεις, η τελική εκτίμηση της ρίζας είναι c = ', c)
print('f(c) = ', f(c))



#Ερώτημα 1β

print('\n     Ερώτημα 1β \n')


def f(x): 
    return mp.tan(x) - x/(1-x**2)
def df(x): 
    return (mp.sec(x))**2 - (x**2 + 1)/(x**2 - 1)**2


x = 3.0 
n1 = 0
e = 1.e-100
while( abs(f(x)) > e and n1 < 15):
    x  -= f(x)/df(x)
    n1 += 1
  
print('Μετά από n = ', n1,'επαναλήψεις, η τελική εκτίμηση της ρίζας είναι x = ', x)
print('f(x) = ', f(x))
  
  
#βλέπω πως η μέθοδος Newton - Raphson δίνει πιο ακριβές αποτέλεσμα 




#Ερώτημα 2

print('\n     Ερώτημα 2 \n')

def f(x): 
    return np.tan(x) - x/(1-x**2)

a = 4  
b = 10
n = 0  
e = 1.e-100
while( b - a > e and n < 15):
    c = 0.5*(a + b)
    if f(c)*f(b) < 0:
        a = c
    else: 
        b = c
    n += 1

print('Μετά από n = ', n,'επαναλήψεις, η τελική εκτίμηση της ρίζας είναι c = ', c)
print('f(c) = ', f(c))

#άρα υπάρχει ρίζα και στο διάστημα [4,10]
  
  