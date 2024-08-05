import sys
input = sys.stdin.readline
m, n = map(int, input().split())
for i in range(m, n + 1):
    if i == 1:
        continue
    a = True
    for j in range(2, int(i**(1/2) + 1)):
        if i % j == 0:
            a = False
            break
    if a:
        print(i)#  제출 번호 : 79654116, 메모리 : 31120, 시간 : 5320