import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
nli = list(map(int,input().split()))

l, r = 0, n-1
mn = float('inf')
rs1,rs2 = 0,0
while l < r:
    a,b = nli[l],nli[r]
    if abs(a + b) < mn:
        mn = abs(a + b)
        rs1,rs2 = a,b
    if a + b < 0:
        l += 1
    elif a + b > 0:
        r -= 1
    else:
        break

print(rs1,rs2)

# 제출번호 : 96583643, 메모리 : 44748, 시간 : 132