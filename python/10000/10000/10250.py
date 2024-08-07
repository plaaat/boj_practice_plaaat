a = int(input())
for i in range(a):
    b,c,d = map(int,input().split())
    e = d%b
    if e == 0:
      f = d//b
      e = b
    else:
      f = d//b+1
    print(e*100+f)


#  제출 번호 : 79658860, 메모리 : 31120, 시간 : 48