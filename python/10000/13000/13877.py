import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())

for _ in range(t):
    i,n = input().split()
    print(i,(int(n,8) if max(list(n)) < "8" else 0),int(n),int(n,16))

# 제출 번호 : 95354874, 메모리 : 32412, 시간 : 32