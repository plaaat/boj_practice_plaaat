import math

t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    print(math.lcm(a,b),math.gcd(a,b))


#  제출 번호 : 81176345, 메모리 : 33240, 시간 : 84