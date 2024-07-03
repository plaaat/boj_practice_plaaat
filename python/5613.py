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

