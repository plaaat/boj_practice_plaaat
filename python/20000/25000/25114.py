import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if a == b:
    print(0)
else:
    pn = 0
    for i in range(n - 1):
        if a[i] != b[i]:
            x = a[i] ^ b[i]
            a[i] ^= x
            a[i + 1] ^= x
            pn += 1
    
    print(pn if a == b else -1)
    
# 제출 번호 : 84558871, 메모리 : 195004, 시간 : 1032
# 제출 번호 : 84558836, 메모리 : 330436, 시간 : 656   By.pypy3