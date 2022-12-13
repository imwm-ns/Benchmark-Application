import math
import time

def primeNum(n):
    answer = []
    for x in range(2, n+1):
        prime = True
        for i in range(2, x):
            if x != i and x % i == 0:
                prime = False
                break
        if prime:
            answer.append(x)
    return answer

def CPU_Benchmark():
    n = 200000
    start = time.time()
    primeNum(n)
    end = time.time()
    return math.ceil(1000000 / (end - start))