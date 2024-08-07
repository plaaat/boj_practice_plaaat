import sys
input = lambda: sys.stdin.readline().rstrip()
sn = int(input())
m = int(input())
if m > 0:
    mli = set(map(int, input().split()))
else:
    mli = set()
pn = abs(100 - sn)
def fi(n):
    for i in str(n):
        if int(i) in mli:
            return 1
    return 0
for i in range(1000001):
    if fi(i) == 0:
        pn = min(pn, len(str(i)) + abs(i - sn))
print(pn)


#  제출 번호 : 79660155, 메모리 : 31120, 시간 : 1452