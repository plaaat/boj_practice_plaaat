import sys
input = lambda:sys.stdin.readline().rstrip()

dic = {}
sol = 0
pen = 0

while True:
    try:
        t,p,a = input().split()
        if a == 'right':
            sol+=1
            if p in dic:
                pen+=(dic[p]*20+int(t))
            else:pen+=int(t)
        else:
            if p in dic:
                dic[p]+=1
            else:
                dic[p] = 1
    except:
        print(sol,pen)
        break#  ���� ��ȣ : 81518787, �޸� : 31120, �ð� : 40