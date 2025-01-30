import sys
input = lambda: sys.stdin.readline().rstrip()

li = []
mn = -1

for i in range(9):
    a = list(map(int,input().split()))
    for j in range(9):
        if a[j] > mn:
            mn = a[j]
            pn = (i+1,j+1)
print(mn)
print(*pn)


#  제출 번호 : 85403020, 메모리 : 31120, 시간 : 32