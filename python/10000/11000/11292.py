import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    t = int(input())
    if t == 0:break
    mn = -1
    ans = []
    for _ in range(t):
        inp1 = input().split()
        name = inp1[0]
        hei = float(inp1[1])
        if hei > mn:
            mn = hei
            ans = [name]
        elif hei == mn:
            ans.append(name)
    print(*ans)

# 제출 번호 : 95921038, 메모리 : 32412, 시간 : 32