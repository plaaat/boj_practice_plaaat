import sys
input = lambda: sys.stdin.readline().rstrip()

r,c = map(int,input().split())
n = int(input())
dic = {}
mn = (-1,-1)

for _ in range(n):
    a,b,c = map(int,input().split())
    if a in dic:
        mib,mic = dic[a][0]
        mab,mac = dic[a][1]
        mib = min(mib,b)
        mic = min(mic,c)
        mab = max(mab,b)
        mac = max(mac,c)

        dic[a] = [(mib,mic),(mab,mac)]
    else:
        dic[a] = [(b,c),(b,c)]
    
tn = (abs(dic[a][0][0] - dic[a][1][0]) + 1) * (abs(dic[a][0][1] - dic[a][1][1]) + 1)
if mn[1] < tn:
    mn = (a,tn)
elif mn[1] == tn:
    if mn[0] > a:
        mn = (a,tn)

print(*mn)

# 제출번호 : 91548278, 메모리 : 56476, 시간 : 376