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

#  제출 번호 : 80439387, 메모리 : 31120, 시간 : 36