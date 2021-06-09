t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(str,input().split()))
    if(a[-1]=='cookie'):
        print('NO')
    else:
        for j in range(n-1):
            if(a[j]=='cookie' and a[j+1]=='cookie'):
                print('NO')
                break
        else:
            print('YES')
