import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())

pn = n // 5
n5 = n % 5

if n5 == 0:
    print(pn)
elif n5 == 1 and pn >= 1:
    print(pn + 1)
elif n5 == 2 and pn >= 2:
    print(pn + 2)
elif n5 == 3:
    print(pn + 1)
elif n5 == 4 and pn >= 1:
    print(pn + 2)
else:
    print(-1)
    
# 제출 번호 : 84364338, 메모리 : 31252, 시간 : 40 