import sys
input = lambda: sys.stdin.readline().rstrip()

a, b = map(int, input().split())

ch = [True] * (b - a + 1)

for i in range(2, int(b ** 0.5) + 1):
    sq = ((a + i ** 2 - 1)//i**2)*i**2
    ed = sq
    ste = 0
    while ed <= b:
        ste += 1
        ed += i ** 2
    ch[sq-a:ed-a:i ** 2] = [False] * ste

res = sum(1 for i in ch if i)
print(res)

# 제출 번호 : 102522147, 메모리 : 44136, 시간 : 1200