for x in range(int(input())):
    n=int(input())
    s=list(input())
    count=0
    a=[]
    for i in range(1,n//2+1):
        a.append(str(i))
        a.append(' ')
    for i in range(n//2+1,0,-1):
        a.append(str(i))
        if i>1:
            a.append(' ')
    if a==s:
        print('yes')
    else:
        print('no')