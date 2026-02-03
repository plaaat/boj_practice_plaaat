import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    inpli = input().split()
    res = float(inpli[0])
    for i in range(1,len(inpli)):
        if inpli[i] == '@':
            res *= 3
        elif inpli[i] == '%':
            res += 5
        else:
            res -= 7
    print(f'{res:0.2f}')

# 제출 번호 : 102597503, 메모리 : 32412, 시간 : 36