# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=0
    x=[int(w) for w in input().split()]
    for i in range(n):
        for j in range(n):
            if i!=j:
                for k in range(n):
                    if x[k]==x[i]*x[j]:
                        a+=1
    if n==a:
        print('yes')
    else:
        print('no')