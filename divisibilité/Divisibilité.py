from math import *

Nombrepremier = [2,3,5,7,9,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

def EstPremier(n):
    for k in range(2, floor(sqrt(n))+1):
        if n%k==0:
            return False

def FacteursPremiers(n):
    l = []
    k=0
    while n!=1:
        p = Nombrepremier[k]
        if n%p==0:
            n=n//p
            l.append(p)
        else:
            k+=1
    return l


#test
print(EstPremier(122))