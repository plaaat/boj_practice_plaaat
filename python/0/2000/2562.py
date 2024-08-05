a = int(input())
c = 1
for i in range(8):
    b = int(input())
    if b > a:
        a = b
        c = i+2
    else:
       continue
print(a)
print(c)
#  제출 번호 : 79659050, 메모리 : 31120, 시간 : 32