n = int(input())
sit = set()
num = 0
li = list(map(int,input().split()))
for i in li:
  if i in sit:
    num+=1
  else:
    sit.add(i)
print(num)#  ���� ��ȣ : 79800698, �޸� : 31252, �ð� : 44