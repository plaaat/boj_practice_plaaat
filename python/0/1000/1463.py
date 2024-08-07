import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
mem = [0]*(n+1)
for i in range(2,n+1):
  mem[i] = mem[i-1]+1
  if i%3 ==0:
    mem[i] = min(mem[i],mem[i//3]+1)
  if i%2 == 0:
    mem[i] = min(mem[i],mem[i//2]+1)
print(mem[n])


#  제출 번호 : 79649907, 메모리 : 38932, 시간 : 544