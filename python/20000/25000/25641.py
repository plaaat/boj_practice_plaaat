n = int(input())
w = input()
s,t = 0,0
x = 0
for i in w:
    if i == 's':
        s += 1
    else:
        t += 1

while s != t:
    if w[x] == 's':
        s -= 1
    else:
        t -= 1
    x += 1
print(w[x:n])
     

# 제출 번호 : 97620990, 메모리 : 32544, 시간 : 36