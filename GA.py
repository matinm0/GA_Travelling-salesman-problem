import random
from random import randint as rndnt

# open file
try:
    op = open('test_case.txt','r')
except: # if error happen , print error
    print('an error ocured')

#read file line by line
lines = op.readlines()

# asign each line to definite variable
n_city = int(lines[0])
n_mut  = int(lines[1])
p_mut  = float(lines[2])
p_cross= float(lines[3])
n_pop  = int(lines[4])

# asigne cities distance 
cities_matrix = []
ln = [[i] for i in range(n_city)]
for j in range(n_city):
    for k in range(n_city):
        ln[j] . append (int((lines[5+j].split(' '))[k]))
cities_matrix = ln
op.close()


# give length of chromosome and make chromosome
def rnd_chr(n):
    l1 = []
    while (1):
        a = rndnt(1,n)
        if a not in l1:
            l1.append(a)
        if len(l1) == n:
            return l1
        
# give chromosome and probability of mutation and mutate our chromosome
def mutation(ci , p_mut):
    for i in  range(len(ci)):
        rnd1 = rndnt(0,5)
        rnd2 = rndnt(0,5)
        if rnd1 > rnd2:
            for i in range((rnd1-rnd2)//2):
                ci[rnd1-i] , ci[rnd2+i] = ci[rnd2+i] , ci[rnd1-i]
        
    return ci
            
# give two chromosome and probability of cross over and cross over two parrent and make one childeren 
#  make simillar indecies !!!!!
def crossover(ci , cj , p_cross):
    cc = []
    for i in range(len(ci)):
        if len(ci) != len(cj) or len(ci) != n_city :
            raise Exception('cancer detected :)')
               # print('cancer detected :)')
        rnd = rndnt(1,n_city)
        cc1 = ci[rnd:]+cj[:rnd]
        cc2 = cj[rnd:]+ci[:rnd]
        cc = [cc1,cc2]
    return cc

# fitness function give a chromosome and return sum of destination that chromosome take. 
#  and then i create [fitness(chromosome) ,  chromosome] and then sort them descending so 
#    we don't need to reverse fitness it is more efficient way "store integer rather than float"
def f(c1):
    fit = 0
    for i in range(n_city-1):
#         print(i)
        fit += cities_matrix[c1[i]-1][c1[i+1]-1]
    return fit

# we create a pool of gene that start point of algorithm 
def gn_pl(n_ch):
    gn_pool = []
    for i in range(n_ch):
        c1 = rnd_chr(n_city)
        gn_pool . append([f(c1),c1])
    return gn_pool
#         gn_pool . append([f()])


# c1_encoded = bin(c1)
def encode(c1):
    str1 = ''
    for i in c1:
        str1 += bin(i)[2:]
    if (len(str1) < 3*n_city):
        lenn = 3*n_city - len(str1)
        str2 = 0*lenn
        str1 = str2+str1

    return(bin(str1))
   
    
def decode(c1):
    return(int(c1))


# write function
try:
#     rnd = rndnt(0,10)
#     op1 = open('out_put_{}.txt'.format(rnd),'a')
    op1 = open('out_put.txt','w')
    op1.close()
    op1 = open('out_put.txt','w')
except: # if error happen , print error
    print('an error ocured')
# this function should iterate 200 times and write output on the file 

        
        
def genetic():
generation = 1
n_pl = 10  #number of pool
gene_pool = gn_pl(n_pl)
while (generation < n_mut):
gene_pool.sort()

# genrate child
c1,c2 = gene_pool[0][1],gene_pool[1][1]
c1_encoded = encode(c1)
c2_encoded = encode(c2)
child1_encoded , child2_encoded = crossover(c1_encoded , c2_encoded , p_cross)

child1 = decode(child1_encode)
child2 = decode(child2_encode)
# print generation
#         print(generation)
#print child
#         print(child1 , child2)
# mutate
child1 = mutation(child1 , p_mut)
child2 = mutation(child2 , p_mut)
#print child

#         print(child1 , child2)
#add child to gene_pool
gene_pool . append([f(child1), child1])
gene_pool . append([f(child2), child2])
#sort by fitness
gene_pool.sort()

#         print(gene_pool)
 op1.write(str(generation))
 op1.write("\n")
 for i in range(5):
     str1 = ''
     try:
         str1 = str(gene_pool[i][1]) + str(1/gene_pool[i][0])
                    
     except:
         str1 = str(gene_pool[i][1]) + '1'
 op1.write(str1)
 op1.write("\n")
 generation += 1

generation += 1
        
            
        
        
        
    
g1 = genetic()


genetic()
op1.close()
