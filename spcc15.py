th_cod_gen = ['t1=a-b' , 't2=a-c' , 't3=t1+u','t4=t3+t2']
# th_cod_gen = ['t1=a*b' , 't2=d*c' ,'t3=t1-t2']
# th_cod_gen = ['t1=c*d','t2=t1+b']
out =[]
opval = {'+':'ADD' , '-':'SUB' , '*':'MUL' , '/':'DIV'}
op = ['*' , '+' , '-' , '/']
j=1
temp = []
for i in range(len(th_cod_gen)):
    if len(th_cod_gen[i]) >= 6:
        if th_cod_gen[i][2:].count('t') >= 1:
            cnt = th_cod_gen[i][2:].count('t')
            if cnt == 1:
                opr = th_cod_gen[i][5]
                tval = th_cod_gen[i][4]
                out.append(f"{opval[opr]} {temp[int(tval) - 1]} , {th_cod_gen[i][6]}")
                temp.append(f"R{int(tval)}")
            else:
                opr = th_cod_gen[i][5]
                tval = th_cod_gen[i][4]
                t2val = th_cod_gen[i][7]
                out.append(f"{opval[opr]} {temp[int(tval) - 1]} , {temp[int(t2val) - 1]}")
            
        else:
            out.append(f"MOV {th_cod_gen[i][3]} , R{j}")
            out.append(f"{opval[th_cod_gen[i][4]]} R{j} , {th_cod_gen[i][5]}")
            temp.append(f"R{j}")
            j+=1

print(*out,sep='\n')