n,m = map(int,input().split())
li = list(map(int,input().split()))
pl = []
for i in range(n-1):
  pl.append((li[i]*m)+(li[i+1]*m))
print(min(pl))#  제출 번호 : 79800391, 메모리 : 42036, 시간 : 84