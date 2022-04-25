from symtable import Symbol
import operator

code = [
    ['START',200],
    ['MOVER','AREG','A'],
    ['ADD','AREG','=2'],
    ['A','DC',4],
    ['B','DS',2],
    ['ORIGN','A+10'],
    ['LTORG'],
    ['MOVER','BREG','=4'],
    ['ADD','AREG','BREG'],
    ['END']
]


Symbolt =[]
lt =[]
pt = []
cmds = ['START','MOVER','ADD','DC','DS','ORIGN','LTORG','END']
oprnd = ['A','B','C']
addr = 0
lti = 0
sti = 0
operators = {'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
for i in range(len(code)):
    if code[i][0] == "START":
        addr = code[i][1]
    elif code[i][0] == "END":
        addr+=1
        for i in range(len(lt)):
            if len(lt[i]) == 2:
                lt[i].append(addr)  

    elif (code[i][0] or code[i][1])!='LTORG' and code[i][0] !='ORIGN':
        
        if  "=" in str(code[i][2]):
            lt.append([lti,code[i][2]])
            lti+=1
        elif code[i][0] in oprnd:
            Symbolt.append([sti,code[i][0],addr,1])
            sti+=1
        if code[i][0]==  'DS' or code[i][1]==  'DS' :
            if code[i][1].isdigit():
                addr+=int(code[i][1])
            else:
                addr+=int(code[i][2])
        addr+=1
    elif code[i][0]=='ORIGN':
        for j in range(len(Symbolt)):
            if Symbolt[j][1] == code[i][1][0]:
                addr = operators[code[i][1][1]](Symbolt[j][2],int(code[i][1][2:])) 
                break
    elif code[i][0]=='LTORG':
        
        for i in range(len(lt)):
            if len(lt[i]) == 2:
                lt[i].append(addr)  

print("=====symbol table=======")
print("Rn name val len")
print(*Symbolt,sep='\n') 
print("=====Literal table=====")
print("Rn name adds")
print(*lt,sep='\n')
print("=====Pool table======")
for i in range(len(lt)):
    print(i,1)