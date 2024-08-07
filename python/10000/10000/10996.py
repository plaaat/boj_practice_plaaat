n = int(input())
for i in range(1, n*2+1):
    if i % 2 == 0:
        print(' *' * int(n//2))
    else:
        if n % 2 == 1:
            print('* ' * int(n//2) + '*')
        else:
            print('* ' * int(n//2))


#  제출 번호 : 80439674, 메모리 : 31120, 시간 : 48