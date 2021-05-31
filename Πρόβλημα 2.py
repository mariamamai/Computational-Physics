import numpy as np
import random
import matplotlib.pyplot as plt


f = open('dice_drop.txt' , "r")
a = np.array(f.read().splitlines())
a = a.astype(int)

def game():
    
    n = 0  
    pos = 0

    while pos < 26:
        dice = random.choice(a)
        pos += dice
        n += 1
        if pos == 3 : pos == 24  
        if pos == 21 : pos == 7  
    return(n)

games = [game() for i in range(200)]
    
plt.hist(games, bins = range(0,20,), histtype = "bar", ec = 'black')     
plt.show()
 
plt.hist(a, bins = range(0,8), histtype = "bar", ec = 'black' )

#σε σχέση με το ιστόγραμμα της τάξης βλέπω πως έχω μια μορφή γκαουσιανής συγκεντρωμένη γύρω από το 7.5 που είναι αναμενόμενο,
#αλλά δεν έχω εύκολα τις ακρέες τιμές γύρω από το 2.5 ή πάνω από 15
#αν τρέξω το ιστόγραμμα του α βλέπω πως έχω πολλά 3 οπότε θα μπορούσε να έχει παραπάνω τιμές γύρω από το 2.5 το ιστρόγραμμα του games. Οπότε εδώ δεν ξέρω τι συμβαίνει

    
    
    
    
    
    
    
    