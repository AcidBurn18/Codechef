t=int(input())
while(t>0):
    t-=1
    n=[int(n) for n in input().split()]
    c=0
    d=[0]
    f=[0]
    
    for i in range(1,n[1]+1):
        p=[int(p) for p in input().split()]
        d.append(p[1])
        f.append(p[0])
        c=c+abs(d[i]-f[i])+abs(d[i-1]-f[i])
    print(c)
        
