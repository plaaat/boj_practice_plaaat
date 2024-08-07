import sys
input = lambda:sys.stdin.readline().rstrip()

a,b,c = map(int,input().split())
if c%2 == 0:
    print((a^b)^b)
else:
    print(a^b)


#  제출 번호 : 81176531, 메모리 : 31120, 시간 : 32