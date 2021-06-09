# cook your dish here
te = int(input())
while(te != 0):
    n = int(input())
    l = list(map(int, input().strip().split()))
    l.sort()
    out = 1
    c = 0
    i = n-1
    while(i > 0):
        if(l[i] == l[i-1]):
            c += 1
            out *= l[i]
            i -= 1
        if(c == 2):
            break
        i -= 1
    if(c == 2):
        print(out)
    else:
        print("-1")
    te -= 1
