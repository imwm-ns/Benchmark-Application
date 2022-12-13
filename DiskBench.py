import random
import time
import math
from CPUBench import primeNum

def BenchMarkDisk(n, primeNum):    
    with open('test.txt', 'w') as file :
        for i in range(n):
            file.write(str(random.choice(primeNum)) + '\n')

    with open('test.txt', 'r') as file :
        line = file.readlines()

def Disk_Benchmark():
    n = 100000000
    prime = primeNum(100)
    start = time.time()
    BenchMarkDisk(n, prime)
    end = time.time()
    return math.ceil(1000000 / (end - start))
