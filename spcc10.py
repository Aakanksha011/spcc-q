inp=[['MACRO'],
['&LAB', 'ADDM', '&ARG1', '&ARG2', '&ARG3'], 
['&LAB', 'A', '1', '&ARG1'],
['','A', '2', '&ARG2'],
['','A', '3', '&ARG3'],
['MEND']]

mdt = []
sy = ['A']
mdtc = 1
ala = ['&LAB','&ARG1','&ARG2','&ARG3']
for i in range(len(inp)):
    if inp[i][0]=='MACRO':
        continue
    elif  inp[i][0]=='MEND' or inp[i][1] not in sy  :
        print(mdtc,inp[i])
        mdtc+=1
    elif inp[i][1] in sy:
        print(mdtc,end=" ")
        ls = []
        for j in range(len(inp[i])):
            if inp[i][j] not in ala:
                ls.append(inp[i][j])
            else:
                ls.append(f'#{ala.index(inp[i][j])}')
        print(ls)
        mdtc+=1