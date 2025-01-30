import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int,input().split()))
mn = 0
tn = 0

for i in a:
    if i == 0:
        mn = max(mn,tn)
        tn = 0
    else:
        tn += 1
print(max(mn,tn))


#  제출 번호 : 84634779, 메모리 : 31120, 시간 : 32