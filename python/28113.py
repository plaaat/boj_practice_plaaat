a,b,c = map(int,input().split())
if max(a,c) > b:
    print('Bus')
elif max(a,c) == b:
    print('Anything')
else:
    print('Subway')