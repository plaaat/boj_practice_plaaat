import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    rec = [
        [],
        [1],
        [2,4,8,6],
        [3,9,7,1],
        [4,6],
        [5],
        [6],
        [7,9,3,1],
        [8,4,2,6],
        [9,1]
    ]
    fina = a % 10
    if fina == 0:
        print(10)
    else:
        print(rec[fina][(b - 1) % len(rec[fina])])

# 제출 번호 : 95378630, 메모리 : 32412, 시간 : 36