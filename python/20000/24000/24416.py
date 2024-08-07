import sys
input = lambda:sys.stdin.readline().strip()

fn = 0
sn = 0
t = int(input())
def fib1(n):
    global fn
    if n == 1 or n == 2:
        fn+=1
    else:
        fib1(n-1)
        fib1(n-2)
dp = [0]*(t+1)
dp[0] = 1
dp[1] = 1
def fib2(n):
    global sn
    for i in range(2,n):
        dp[i] = dp[i-1]+dp[i-2]
        sn+=1
fib1(t)
fib2(t)
print(fn,sn)


#  제출 번호 : 81519158, 메모리 : 123056, 시간 : 1924