import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    wn = input()
    lwn = len(wn)
    if lwn == 1:
        print(wn)
        continue
    n = int(wn)
    nowd = 1
    
    while nowd != lwn:
        n = ((n + 5 * (10 ** (nowd - 1))) // 10 ** nowd) * (10 ** nowd)
        nowd += 1
    print(n)

# 제출 번호 : 101592198, 메모리 : 32412, 시간 : 32