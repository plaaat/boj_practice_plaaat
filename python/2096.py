import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
tl = list(map(int,input().split()))
mal = tl
mil = tl
for j in range(n-1):
    i = list(map(int,input().split()))
    mal = [i[0]+max(mal[0],mal[1]),i[1]+max(mal),i[2]+max(mal[1],mal[2])]
    mil = [i[0]+min(mil[0],mil[1]),i[1]+min(mil),i[2]+min(mil[1],mil[2])]

print(max(mal),min(mil))