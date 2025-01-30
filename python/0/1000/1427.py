import sys
input = lambda: sys.stdin.readline().rstrip()

li = list(map(int,input()))
li.sort(reverse=True)

print(*li,sep='')


#  제출 번호 : 82482459, 메모리 : 31120, 시간 : 36