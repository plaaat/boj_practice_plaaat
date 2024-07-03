pn = 1
n,m = map(int,input().split())
li = list(map(int,input().split()))

for i in li:
    pn*=(i%m)
print(pn%m)