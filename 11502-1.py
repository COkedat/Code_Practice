import math
primes = []
num = 1000
array = [True for i in range(num + 1)] 
for i in range(2, int(math.sqrt(num)) + 1):
    if array[i] == True: 
        j = 2
        while i * j <= num:
            array[i * j] = False
            j += 1
for i in range(2, len(array)):
    if (array[i]):
        primes.append(i)

def findPrimes(N, p):
    for i in p:
        for j in p:
            for k in p:
                if(i+j+k==N):
                    print(f"{i} {j} {k}")
                    return
    print(0)

import sys
T = int(input())
for _ in range(T):
    N = int(sys.stdin.readline())
    findPrimes(N, primes)
    