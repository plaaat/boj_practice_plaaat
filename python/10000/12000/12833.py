import sys
input = lambda:sys.stdin.readline().rstrip()

a,b,c = map(int,input().split())
if c%2 == 0:
    print((a^b)^b)
else:
    print(a^b)#  ���� ��ȣ : 81176531, �޸� : 31120, �ð� : 32