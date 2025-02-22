import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())

for _ in range(t):
    n = int(input())
    if n == 0:
        print(0)
        continue
    flag = True
    
    if n < 0:
        flag = False
        n = abs(n)
    
    nli = []
    while n > 0:
        nam = n % 3
        if nam == 2:
            nli.append(-1)
            n = (n + 1) // 3
        elif nam == 1:
            nli.append(1)
            n = (n - 1) // 3
        else:
            nli.append(0)
            n = n // 3
    
    nli.reverse()
    res = []
    if flag:
        for d in nli:
            if d == 1:
                res.append('1')
            elif d == 0:
                res.append('0')
            else:
                res.append('-')
    else:
        for d in nli:
            if d == 1:
                res.append('-')
            elif d == 0:
                res.append('0')
            else:
                res.append('1')
    
    print(''.join(res))
