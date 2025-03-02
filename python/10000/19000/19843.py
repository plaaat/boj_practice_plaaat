import sys
input = lambda: sys.stdin.readline().rstrip()

t,n = map(int,input().split())
day = {
    'Mon':0,
    'Tue':1,
    'Wed':2,
    'Thu':3,
    'Fri':4
}

slp = 0
for _ in range(n):
    inp = input().split()
    slp += (day[inp[2]] * 24 + int(inp[3])) - (day[inp[0]] * 24 + int(inp[1]))

if t > slp + 48:
    print(-1)
else:
    if t < slp:
        print(0)
    else:
        print(t - slp)