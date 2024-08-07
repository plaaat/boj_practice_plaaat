import sys
input = sys.stdin.readline

while True:
    line = input()
    if line[0] == ".":
        break
    line.strip()
    li = []
    tf = True
    for i in line:
        if i == '(' or i == '[':
            li.append(i)
        elif i == ')' or i == ']':
            if not li:
                tf = False
                break
            a = li.pop()
            if (i == ')' and a != '(') or (i == ']' and a != '['):
                tf = False
                break
    if tf and len(li) == 0:
        print("yes")
    else:
        print("no")


#  제출 번호 : 79653967, 메모리 : 31120, 시간 : 84