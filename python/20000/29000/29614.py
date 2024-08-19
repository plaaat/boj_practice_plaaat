from collections import deque
import decimal as dc
dc.getcontext().rounding = dc.ROUND_HALF_UP

scores = {'A+' : 4.5, 'A' : 4.0, 'B+' : 3.5, 'B' : 3.0,
          'C+' : 2.5, 'C' : 2.0, 'D+' : 1.5, 'D' : 1.0, 'F' : 0.0}
score_list = []

S = deque(list(input()))
temp = S.popleft() #temp에 가장 왼쪽 값 담기
while S:
    try:
        if temp!='+' and temp!='F': #A+와 A 등을 구별하기 위해 추가해줌
                if S[0]=='+':
                    temp = temp+S.popleft()
        score_list.append(scores[temp])
        temp = S.popleft()
    except IndexError:
        pass
if temp:
    score_list.append(scores[temp])

ans = dc.Decimal(sum(score_list))/dc.Decimal(len(score_list))
print(dc.Decimal(str(ans)).quantize(dc.Decimal('1.00000')))