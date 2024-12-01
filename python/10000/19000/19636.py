import sys
input = lambda: sys.stdin.readline().rstrip()

bw, bi, bt = map(int, input().split())
d, i, a = map(int, input().split())

pw1, pw2 = bw, bw
pi = bi

for _ in range(d):
    pw1 += i - bi - a
    pw2 += i - pi - a
    
    if abs(i - (pi + a)) > bt:
        pi += (i - (pi + a)) // 2

if pw1 <= 0:
    print("Danger Diet")
else:
    print(pw1, bi)

if pw2 <= 0 or pi <= 0:
    print("Danger Diet")
else:
    print(pw2, pi, end=" ")
    if bi > pi:
        print("YOYO")
    else:
        print("NO")

# 제출번호 : 87047736, 메모리 : 31120, 시간 : 36