n = 0
dic = {}
for _ in range(10):
    t = int(input())
    if t in dic:
        dic[t]+=1
    else:dic[t] = 1
    n+=t
print(n//10)
print(max(dic.items(),key=lambda x:x[1])[0])#  제출 번호 : 80808423, 메모리 : 31120, 시간 : 32