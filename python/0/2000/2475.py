a = input().split()
c = []
d = 0
for i in range(5):
  b = int(a[i])**2
  c.append(b)
for i in range(5):
  d += c[i]
print(d%10)


#  제출 번호 : 79659082, 메모리 : 31120, 시간 : 40