import sys
input = lambda: sys.stdin.readline().rstrip()

hw, aw, hm, am = map(int, input().split())
sk, re = map(int, input().split())

wnum = hw / am

if 0 < (hm - sk) % aw <= aw - sk:
    mnum = hm / aw
else:
    mnum = (hm + re) / aw
chan = lambda x: int(x) if int(x) == x else int(x)+1
mnum = chan(mnum)
wnum = chan(wnum)

print('Victory!' if mnum <= wnum else 'gg')

# 제출 번호 : 85390134, 메모리 : 31120, 시간 : 36
