import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
st = {}
mn = 1

def gcd(a,b):
    while b != 0:
        r = a % b
        a,b = b,r
    return abs(a)

for _ in range(n):
    x,y = map(int,input().split())
    lx = 'l' if x < 0 else 'r'
    ly = 'l' if y < 0 else 'r'
    g = gcd(x,y)
    a = (x // g, y // g)
    an = f'{ly}{lx}{a}'
    if an in st:
        st[an] += 1
        mn = max(mn,st[an])
    else:
        st[an] = 1

print(mn)

# 제출 번호 : 96372427, 메모리 : 44188, 시간 : 328
