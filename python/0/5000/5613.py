n = 0
while True:
        t = input()
        if t == '+':
            n+=int(input())
        elif t == '-':
            n-=int(input())
        elif t == '*':
            n*=int(input())
        elif t == '/':
            n//=int(input())
        elif t == '=':
            print(n)
            break
        else:
            n+=int(t)

#  ���� ��ȣ : 80439387, �޸� : 31120, �ð� : 36