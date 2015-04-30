import time
import sys

N=int(sys.argv[1])
PrimeList=list(range(0,N))
PrimeList[1]=0
echtepriemgetallen=[]

T1 = time.perf_counter()

for i in range(1,N):
    if PrimeList[i] != 0:
        echtepriemgetallen.append(PrimeList[i])
        for j in range(2*i,N,i):
            PrimeList[j] = 0

T2 = time.perf_counter() 

fout=open(sys.argv[2], 'w')
fout.write("\n".join(map(str, echtepriemgetallen)))

print('Found ' + str(len(echtepriemgetallen)) + ' Prime numbers smaller than ' + sys.argv[1] + ' in ' + str(T2-T1) + ' sec.')

#print(len(echtepriemgetallen))