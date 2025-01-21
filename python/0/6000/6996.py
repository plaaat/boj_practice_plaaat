import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    a,b = input().split()
    la = list(a)
    lb = list(b)
    la.sort()
    lb.sort()
    if la != lb:
        print(f"{a} & {b} are NOT anagrams.")
    else:
        print(f"{a} & {b} are anagrams.")
    
# 제출번호 : 88758892, 메모리 : 32412, 시간 : 36