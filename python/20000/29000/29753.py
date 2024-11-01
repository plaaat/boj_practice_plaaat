import sys
from decimal import *
getcontext().rounding = ROUND_DOWN
input = lambda: sys.stdin.readline().rstrip()

n,m = input().split()
n = int(n)
m = Decimal(m)

tot = 0
num = 0
dic = {'A+':4.5,
       'A0':4.0,
       'B+':3.5,
       'B0':3.0,
       'C+':2.5,
       'C0':2.0,
       'D+':1.5,
       'D0':1.0,
       'F':0}

for _ in range(n-1):
    a,b = input().split()
    a = int(a)
    tot += Decimal(str(dic[b])) * a
    num += a

x = int(input())
num += x

t = ''

for v,n in reversed(dic.items()):
    n = str(n)
    if round((tot + Decimal(n) * x)/num,2) > m:
        print(v)
        break
else:
    print('impossible')