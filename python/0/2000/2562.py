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
#  ���� ��ȣ : 79659050, �޸� : 31120, �ð� : 32