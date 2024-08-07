li = [1,1,2,2,2,8]
pl = list(map(int,input().split()))
p = []
for i in range(6):
  p.append(li[i]-pl[i])
print(*p)


#  제출 번호 : 79799754, 메모리 : 31120, 시간 : 40