import random
suma1 = 0
suma2 = 0
suma3 = 0
#A
n = int(input('Δώσε την διάσταση του τετραγώνου\n'))
pinakas = [[None]*n]*n 



for _ in range(100):
 
    #B #Φτιάχνουμε πρώτα εναν πίνακα helpfularray(1D, γεμίζωντάς τα μισά κελιά του στην τύχη με 1) και έπειτα τον μετατράπουμε στον pinakas(2D)  

    plithostheseon = n*n
    list_range = [*range(plithostheseon)]      
    helpfularray = [0]*plithostheseon
    while sum(helpfularray)!=int(plithostheseon/2):
        helpfularray[random.choice(list_range)] = 1 
 
    pinakas = []
    for i in range(0, plithostheseon, n):
        k = helpfularray[i:i+n]
        pinakas.append(list(k))
 
    orizontio_pl = 0
    katheto_pl = 0
    diag_pl = 0

    for i in range(n):
        for j in range(n):
            if pinakas[i][j]==1:
                if sum(pinakas[i])>=4:
                    try:              #για οριζόντια
                        if (pinakas[i][j+1]==1 and pinakas[i][j+2]==1 and pinakas[i][j+3]==1) :
                            orizontio_pl += 1
                    except:  
                        continue
                    try:               #για καθετα
                        if (pinakas[i+1][j]==1 and pinakas[i+2][j]==1 and pinakas[i+3][j]==1) :
                            katheto_pl += 1
                    except: 
                        continue
                try:                    #και για διαγώνια
                    if (pinakas[i+1][j+1]==1 and pinakas[i+2][j+2]==1 and pinakas[i+3][j+3]==1) :
                        diag_pl += 1
                except: 
                    continue    
    suma1 +=orizontio_pl       
    suma2 +=katheto_pl       
    suma3 +=diag_pl       
   
print('__________________________________________________________________')    
print('Ο Μέσος όρος τετράδων οριζόντια είναι',    suma1/100)    
print('Ο Μέσος όρος τετράδων κάθετα είναι',    suma2/100)    
print('Ο μέσος όρος τετράδων διαγώνια (κύρια διαγώνιος) είν', suma3/100)