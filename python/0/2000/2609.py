a,b = map(int,sorted(input().split()))
c = a*b
if b>a: a,b=b,a

while b!=0:
  a=a%b
  a,b=b,a
print(a)
print(int(c/a))


#  제출 번호 : 79658643, 메모리 : 31120, 시간 : 44