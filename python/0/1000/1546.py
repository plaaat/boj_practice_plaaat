a = int(input())
b = sorted(list(map(int,input().split())))
c = b[a-1]
d = []
for i in range(a):
  d.append((b[i]/c)*100)
print(sum(d)/a)


#  제출 번호 : 79658682, 메모리 : 31252, 시간 : 44