import sys
input = lambda: sys.stdin.readline().rstrip()

while True: 
    r,c = input().split("c")
    r = int(r.rstrip("R"))
    c = int(c)
    if r == 0 and c == 0:
        break
    