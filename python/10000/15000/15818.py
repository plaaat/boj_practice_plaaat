pn = 1
n,m = map(int,input().split())
li = list(map(int,input().split()))

for i in li:
    pn*=(i%m)
print(pn%m)#  제출 번호 : 80439577, 메모리 : 31120, 시간 : 32