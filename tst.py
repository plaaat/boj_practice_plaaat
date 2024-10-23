import time
starttimertimer = time.perf_counter_ns()
import sys
input = lambda: sys.stdin.readline().rstrip()

l,r = int(input()),int(input())
n = 0
br = 1
while True:
    l *= (r/100)
    l = int(l)
    if l <= 5:
        print(n)
        break
    br *= 2
    n += l * br

# 제출 번호 : 85532493, 메모리 : 31120, 시간 : 36

print(f"Time : {(time.perf_counter_ns()-starttimertimer)*1e-05}ms")