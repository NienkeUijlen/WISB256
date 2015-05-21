def findRoot(f,a,b,epsilon):
    while True:
        m=(a+b)/2
        if abs(a-b)<=epsilon:
            return(m)
        elif (f(a)<0 and f(m)>0) or (f(a)>0 and f(m)<0):
            b=m
        elif (f(b)<0 and f(m)>0) or (f(b)>0 and f(m)<0):
            a=m
        elif m==0:
            return(m)
        elif a==0:
            return(a)
        elif b==0:
            return(b)


    
        