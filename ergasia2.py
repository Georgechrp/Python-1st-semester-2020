import random
n = int(input('Δώσε το n\n'))


#Ευρεση αριθμού Fibonacci
i = 0
j = 1
for _ in range(n-1):
    p = i + j
    i = j
    j = p

# Ελεγχος a^p=a mod p
i=0
while i<20:
    a = random.randrange(1, p)    #τυχαίους αριθμούς ευρους=[1, p)
    if pow(a, p, p)==a:           #(a^p) MOD p 
        i += 1
    else:
        break
        
        
if i==20:
    print('Ο αριθμός', p, 'είναι πρώτος!')
else:
    print('Ο αριθμός', p, 'δεν είναι πρώτος!')
