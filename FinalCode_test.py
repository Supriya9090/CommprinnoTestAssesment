T=int(input())                             #User Input
for i in range(T):           
    s=input()
    p=set(s)
    f=[]
    print(f)
    for i in p:                             #printing a number
        f.append(s.count(i))
    f.sort()
    print(f)
    print(p)
    if len(f)>=4 and f[3]!=f[1]+f[2]:       # check if distinct string is greater than 3 or not
        f[0],f[1]=f[1],f[0]
    condition=True
    if len(f)>=3:
        for i in range(2,len(f)):           #  check if distinct string is less than 3 or not
            if f[i]!=f[i-1]+f[i-2]:
                condition=False
    if condition:                           #check condition.if i<3 then string is always print dynamic else print Not
        print("Dynamic")
    else:
        print("Not")