import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
nli = list(map(int,input().split()))
ntt = sum(x**2 for x in nli)
sn = sum(nli)

print((sn ** 2 - ntt)//2)

# 제출 번호 : 101218297, 메모리 : 42660, 시간 : 60