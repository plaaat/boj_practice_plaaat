import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int,input().split())
k = int(input())
wo = input()

def dm(x):
    if x == 1:
        return 2
    else:
        return 1

for w in wo:
    if w == 'A':
        n = n - 2 if n > 2 else n + 2
    elif w == 'B':
        n = n + 1 if n % 2 else n - 1
        m = dm(m)
    elif w == 'C':
        if n == 1:
            n = 4
        elif n == 4:
            n = 1
        elif n == 3:
            n = 2
        else:
            n = 3
        m = dm(m)
    else:
        if m == 1:
            if n == 1:
                m = 2
            else:
                n -= 1
        else:
            if n == 4:
                m = 1
            else:
                n += 1
print(n,m)

# 제출 번호 : 97059083, 메모리 : 32412, 시간 : 44