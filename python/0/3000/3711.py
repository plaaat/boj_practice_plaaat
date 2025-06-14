import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())

for _ in range(t):
    g = int(input())
    gli = [int(input()) for _ in range(g)]
    res = 0
    while True:
        res += 1
        modst = set()
        for i in gli:
            i = i % res
            if i in modst:
                break
            else:
                modst.add(i)
        else:
            print(res)
            break

# 제출 번호 : 95355007, 메모리: 32412, 시간 : 888