while True:
    a,b,c = input().split()
    if a == '#':break
    b,c = int(b),int(c)
    if b >17 or c>=80:
        print(a,'Senior')
    else:
        print(a,'Junior')#  ���� ��ȣ : 81291755, �޸� : 31120, �ð� : 44