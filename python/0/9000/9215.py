import sys
from math import gcd
input = lambda: sys.stdin.readline().rstrip()

num = 0
while True:
    n = int(input())
    num += 1
    if n == 0:
        break
    a,b,c = [],[],[0]
    for _ in range(n):
        x = input()
        if len(x) == 1:
            c.append(int(x))
        elif x[1] == ',':
            x,y,z = map(int,(x[0],x[2],x[4]))
            a.append(y)
            b.append(z)
            c.append(x)
        else:
            x,y = map(int,x.split('/'))
            a.append(x)
            b.append(y)
    
    m = b[0]
    for i in b[1:]:
        m = (m * i) // gcd(m,i)
    k = 0
    for i in range(len(a)):
        k += int(a[i] * (m/b[i]))
    c = sum(c)
    print(f'Test {num}: ',end='')
    
    if k % m == 0:
        c += k // m
        print(c)
    elif k > m:
        c += k//m
        k -= (k//m) * m
        while m % k == 0:
            if k == 1:break
            t = gcd(m,k)
            m //= t
            k //= t
        print(f'{c},{k}/{m}')
    else:
        while m % k == 0:
            if k == 1:
                break
            t = gcd(m,k)
            m //= t
            k //= t
        print(f'{c},' if c !=0 else '',end='')
        print(f'{k}/{m}')

# 제줄 번호 : 85051389, 메모리 : 33240, 시간 : 32