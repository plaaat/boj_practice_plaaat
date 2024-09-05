import sys
import random

input = lambda: sys.stdin.readline().rstrip()

def finder(a, n):
    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True
    for _ in range(s - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return True
    return False

def checker(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    for _ in range(5):
        a = random.randint(2, n - 2)
        if not finder(a, n):
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    while True:
        if checker(n):
            print(n)
            break
        n += 1