import time 
import math

def MemoryBench():
    start = time.time()
    fibonacciNumber = [fibonacci_of(num) for num in range(20000)]
    end = time.time()
    return math.ceil(1000000 / (end - start))

def fibonacci_of(num):
    firstNumber = 0
    secondNumber = 1
    count = 0

    while (count <= num):
        fibonacci = firstNumber + secondNumber
        firstNumber = secondNumber
        secondNumber = fibonacci
        count += 1
    return fibonacci