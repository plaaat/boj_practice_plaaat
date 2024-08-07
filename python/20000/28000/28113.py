a,b,c = map(int,input().split())
if max(a,c) > b:
    print('Bus')
elif max(a,c) == b:
    print('Anything')
else:
    print('Subway')


#  제출 번호 : 81175827, 메모리 : 31120, 시간 : 36