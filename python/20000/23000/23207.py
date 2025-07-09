import sys
input = lambda: sys.stdin.readline().rstrip()

s = list(input())
sst = set(s)
ls = len(s)
st = 0
wot = set(['B','C','D','F'])
wo = ['A','B','C']
if 'A' in sst:
    st = 0
elif 'B' in sst:
    wot.remove('B')
    st = 1
elif 'C' in sst:
    wot.remove('C')
    st = 2
else:
    st = 3

if st == 3:
    s = ['A'] * ls
else:
    for i in range(ls):
        if s[i] in wot:
            s[i] = wo[st]

print(*s, sep='')

# 제출 번호 : 96151450, 메모리 : 32412, 시간 : 40