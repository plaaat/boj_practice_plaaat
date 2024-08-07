n = int(input())
sit = set()
num = 0
li = list(map(int,input().split()))
for i in li:
  if i in sit:
    num+=1
  else:
    sit.add(i)
print(num)


#  제출 번호 : 79800698, 메모리 : 31252, 시간 : 44