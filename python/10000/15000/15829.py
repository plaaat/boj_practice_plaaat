a = int(input())
b = list(input())
d = 0
for i in range(a):
  c = ord(b[i])-96
  d+=c*((31)**(i))

print(d%1234567891)


#  제출 번호 : 79658658, 메모리 : 31120, 시간 : 44