import sys
input = lambda: sys.stdin.readline().strip()

n, m = input(), input()
st = ''.join(n[i] + m[i] for i in range(8))

for _ in range(14):
    st = ''.join(str((int(st[i]) + int(st[i+1])) % 10) for i in range(len(st) - 1))

print(f"{st:0>2}")

# 제출 번호 : 84956755, 메모리 : 31120, 시간 : 40