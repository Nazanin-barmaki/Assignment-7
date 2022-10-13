list=[]
p=''.join(list)
n_r=int(input("enter the number of row: "))
m_c=int(input("enter the number of column: "))
one=1
tow=1
for i in range(n_r):
    for i in range(m_c):
        c=one*tow
        tow+=1
        list.append(c)
        
    one+=1
    tow=1

for i in range(n_r):
        l=list[:m_c]
        if len(list)>0:
            del list[0:m_c]
            print(l)
        else:
            break        