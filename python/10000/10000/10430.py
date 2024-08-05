A,B,C = map(int,input().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C) #  제출 번호 : 81382731, 메모리 : 31120, 시간 : 44