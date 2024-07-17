import sys
input = lambda:sys.stdin.readline().rstrip()
tf = True
for s in range(1,6):
    wo = input()
    if 'FBI' in wo:
        print(s, end = ' ')
        tf = False
if tf:print('HE GOT AWAY!')