import ast
import collections

f = open('dictfile.txt', 'r')        
temp = f.read()
leksiko = ast.literal_eval(temp)        

lista = []

def forcount(d):
    if type(d) == dict:                   #αν το d είναι τύπου λεξικό τότε..
        for item in d.keys():
            if isinstance(d[item], (list, tuple, dict)):     #ελέγχει αν το d[item] είναι ή list ή tuple ή dict              
                k= forcount(d[item])
            lista.append(item)         #προσθέτει κάθε φορά το item στην lista
            
    elif type(d) == list or type(d) == tuple:
        for item in d:
            if isinstance(item, (list, tuple, dict)):
                k= forcount(item)

forcount(leksiko)    
plithos_counter = collections.Counter(lista)

plithos_list = list(plithos_counter)

print('Εμφανίζονται περισσότερες φορές τα κλειδιά:')
for i in range(3):
    print(plithos_list[i])
