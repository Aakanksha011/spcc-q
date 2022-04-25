inp=[['MACRO'],
['&LAB', 'ADDM', '&ARG1', '&ARG2', '&ARG3'], 
['&LAB', 'A', '1', '&ARG1'],
['','A', '2', '&ARG2'],
['','A', '3', '&ARG3'],
['MEND']]

ala = []
isMacro = False

for i in range(len(inp)):
    if inp[i][0]=='MACRO':
        isMacro = True
        continue
    elif isMacro:
        k=0
        for j in range(len(inp[i])):
            if j!=1:
                print(f'#{k} {inp[i][j]}')
                k+=1
        break
    