import sys
input = lambda: sys.stdin.readline().rstrip()

q = int(input())
for _ in range(q):
    a, m = map(int, input().split())
    print((176*a*m)//100000)

# 제출 번호 : 102598129, 메모리 : 32412, 시간 : 40