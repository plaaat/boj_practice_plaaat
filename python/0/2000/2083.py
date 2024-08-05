while True:
    a,b,c = input().split()
    if a == '#':break
    b,c = int(b),int(c)
    if b >17 or c>=80:
        print(a,'Senior')
    else:
        print(a,'Junior')#  제출 번호 : 81291755, 메모리 : 31120, 시간 : 44