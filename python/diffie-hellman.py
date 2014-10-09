#!usr/bin/env python2
import math
import time
from random import randint


def getPrime(v):
    while True:
        p = randint(v - 50000,v + 50000)
        if isPrime(p):
            return p

def isPrime(n):
    if n % 2 == 0:
        return False
    for i in range(3,int(math.ceil(math.sqrt(n)))):
        if n % i == 0:
            return False
    return True

def getFactors(n):
    factors = []
    for i in range(2,int(math.ceil(math.sqrt(n)))):
        if n % i == 0:
            factors.append(i)
            factors.append(n/i)
    return factors

  
def quickexp(b,p,m):
    res = 1
    pot = b % m
    while p:
        if p % 2 == 1:
            res = (pot * res) % m
        pot = (pot * pot) % m
        p = p >> 1;
    return res

def isGenerator(p,g):
    factors = getFactors(p-1)
    for factor in factors:
        if (quickexp(g,factor,p) == 1):
            return False
    return True
                
def generatePairPG(value):
    p = getPrime(value)
    while True:
        g = randint( 2, p - 1)
        if isGenerator(p,g):
            return p , g


def diffie_hellman(n):
	p, g = generatePairPG(n)
	x = randint(1,p-1)
	y = randint(1,p-1)
	fx = quickexp(g,x,p)
	fy = quickexp(g,y,p)
	k1 = quickexp(fx , y , p)
	k2 = quickexp(fy , x , p)
	if(k1 == k2):
		return p, g, fx, fy , k1
	else:
		print "error"
		return 0, 0, 0, 0 

def brute_force(p,g,fx,fy):
	for i in range(p):
		if (fx == quickexp(g,i,p)):
			return quickexp(fy, i, p)
		elif(fy == quickexp(g,i,p)):
			return quickexp(fx,i,p)
			

f = open('generate.dat', 'w')
f2 = open('brute_force.dat', 'w')

for i in range(1):
    t1 = 0
    t2 = 0 
    for a in range(1):
	tb = int(round(time.time() * 1000))
       	p,g,fx,fy,k1 = diffie_hellman(100000000000000)
	ta = int(round(time.time() * 1000))
	t1 += (ta - tb)
        """
        if (a <= 1):
            tbb = int(round(time.time() * 1000))
            brute_force_key = brute_force(p,g,fx,fy)
            tba = int(round(time.time() * 1000))
            t2 += (tba - tbb)
            if(brute_force_key != k1):
                print "error" """
    d1 = t1 / 1.0
    print d1
    d2 = t2 / 1.0
    print d2
    f.write(""+ str(i) + " " + str(d1) + "\n")
    f2.write(""+ str(i) + " " + str(d2) + "\n")	
f.close()
f2.close()
