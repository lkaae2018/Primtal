def primes(n):
    m=n+1
    #print (type(m))
    s=range(0,m)
    s[1]=0
    bottom=2
    top=n//bottom
    while (bottom*bottom<=n):
            while (bottom<=top):
                    if s[top]:
                            s[top*bottom]=0
                    top-=1
            bottom+=1
            top=n//bottom
    return [x for x in s if x]

Primtal=primes(1311)
print (Primtal)
