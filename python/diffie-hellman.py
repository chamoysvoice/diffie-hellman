#!usr/bin/env python2
import math
from random import randint


def getPrime():
    while True:
        p = randint(3,999999999)
        if isPrime(p):
            return p

def isPrime(n):
    if n % 2 == 0:
        return False
    for i in range(3,n,2):
        if i % n == 0:
            return False
    return True
                
for i in range(20):
    print getPrime()
