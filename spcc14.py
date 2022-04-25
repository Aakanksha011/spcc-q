exp = str(input("Expression :"))
 
post=[]
preced ={'+':1,'-':1,"*":2,'/':2}
s=[]
for x in exp :
    if x.isalpha():
        post.append(x)
    elif not s or preced[x]>preced[s[-1]]:
        s.append(x)
    else :
        y = s.pop()
        post.append(y)
        s.append(x)
rs= s[::-1]
post.extend(rs)

es=[]
i=1
for z  in post :
    if  z.isalpha():
        es.append(z)
    else:
        r=es.pop()
        l=es.pop()
        print('t',i,'=',l,z,r)
        es.append('t'+str(i))
        i+=1
print('x = t',i-1)