a = list(input())
while int(a[0])>0:
    b = int((len(a)/2))
    c = list(reversed(a))
    if a[:b] == c[:b]:
      print('yes')
    else:
      print('no')
    a = list(input())#  ���� ��ȣ : 79658673, �޸� : 31120, �ð� : 44