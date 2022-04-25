import numpy as np
grammarL=['S','S','A','B']
grammarR=['aABC','AB','b','#']
first=[['a'],['b','d'],['#']]
follow=[['$'],['$'],['c']]
col=['a','b','c','#','$']
nt=['S','A','B']
row=nt

print('Row Col')
for x in range(0,len(grammarL)):
    a = grammarR[x]
    
    if a[0]=='#':
        t = nt.index(grammarL[x])
        temp = follow[t][0]
        if temp =='$':
            print (grammarL[x],' ','$','    ', grammarL[x],'=>',grammarR[x])
        else :
            print (grammarL[x],' ',temp,'    ', grammarL[x],'=>',grammarR[x])
    elif a[0].islower():
        print (grammarL[x],' ',a[0],'    ', grammarL[x],'=>',grammarR[x])
    else :
        temp=first[nt.index(a[0])]
        for y in temp:
            print (grammarL[x],' ',y,'    ', grammarL[x],'=>',grammarR[x])