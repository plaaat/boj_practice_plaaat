import sys
input = sys.stdin.readline
sl = set()
def deq(x):
    global sl
    x = x.strip().split()
    if x[0] == 'add':
        sl.add(int(x[1]))
    elif x[0] == 'remove':
        sl.discard(int(x[1]))
    elif x[0] == 'check':
        if int(x[1]) in sl:
            print('1')
        else:
            print('0')
    elif x[0] == 'toggle':
        if int(x[1]) in sl:
            sl.remove(int(x[1]))
        else:
            sl.add(int(x[1]))
    elif x[0] == 'all':
        sl = set(map(int,range(1, 21)))
    elif x[0] == 'empty':
        sl = set()
for i in range(int(input())):
    deq(input())


#  제출 번호 : 79653907, 메모리 : 31120, 시간 : 6468