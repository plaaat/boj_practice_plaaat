def is_start(stm, sts, nom, nos, edm, eds):
    if nom < stm or nom > edm:
        return False
    
    if nom == stm == edm:
        if nos < sts:
            return False
        elif nos > eds:
            return False
        else:
            return True
    
    if stm < nom < edm:
        return True
    if nom == stm:
        if nos >= sts:
            return True
        return False
    if nom == edm:
        if nos <= eds:
            return True
        else:
            return False
    return False

def solution(video_len, pos, op_start, op_end, commands):
    vm,vs = map(int,video_len.split(':'))
    pom,pos = map(int,pos.split(':'))
    ops_m,ops_s = map(int,op_start.split(':'))
    ope_m,ope_s = map(int,op_end.split(':'))

    for com in commands:
        if is_start(ops_m,ops_s,pom,pos,ope_m,ope_s):
            pom,pos = ope_m,ope_s
        if com == 'prev':
            if pos < 10:
                if pom == 0:
                    pom,pos = 0,0
                else:
                    pom -= 1
                    pos += 50
            else:
                pos -= 10
        else:
            if pos >= 50:
                pom += 1
                pos -= 60
            pos += 10
            if pom == vm:
                if pos > vs:
                    pom = vm
                    pos = vs
            elif pom > vm:
                pom = vm
                pos = vs
    if is_start(ops_m,ops_s,pom,pos,ope_m,ope_s):
        pom,pos = ope_m,ope_s
    answer = f"{pom:0>2}:{pos:0>2}"
    return answer

print(solution(

  	"07:22", "04:05", "00:15", "04:07", ["next"]))