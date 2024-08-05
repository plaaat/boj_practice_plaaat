a = list(input())
while int(a[0])>0:
    b = int((len(a)/2))
    c = list(reversed(a))
    if a[:b] == c[:b]:
      print('yes')
    else:
      print('no')
    a = list(input())#  제출 번호 : 79658673, 메모리 : 31120, 시간 : 44