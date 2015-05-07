import math
import random
import sys

L=float(sys.argv[2])       # lengte van de naald
N=int(sys.argv[1])         # aantal herhalingen van het experiment
if(len(sys.argv)>3):
    random.seed(float(sys.argv[3]))


if L>1:
    print('AssertionError: L should be smaller than 1')
    exit(1)

def drop_needle(L):
    x0=random.random()                    # uniform in [0,1]
    a=random.vonmisesvariate(0,0)         # uniform in [0,2pi]
    x1=x0+L*math.cos(a)                   # andere eindpunt berekenen
    if x1<=0 or x1>=1:
        return True
    else:
        return False

i=0
hits=0
while i<N:
    if drop_needle(L)==True:
        hits=hits+1
    i=i+1

print(hits, "hits in", N,  "tries")
print('pi =', 2*L/(hits/N))