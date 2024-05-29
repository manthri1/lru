capacity=3
processlist=[3,4,5,6,7,1,2,0,1]
pagefault=0
s=[]
for i in processlist:
    if i not in s:
        if len(s)==capacity:
            s.remove(s[0])
            s.append(i)
        else:
            s.append(i)
        pagefault+=1
        #lru
    else:
        s.remove(i)
        s.append(i)


print(pagefault)
print(s)