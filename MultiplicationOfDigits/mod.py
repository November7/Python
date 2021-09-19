def mul(n,iter):
    if(len(str(n))==1):
        print('Total steps: ',iter)
        return
    
    digits=[int(i) for i in str(n)]

    m=1
    iter+=1
    for j in digits:
        m *= j
    print('Step: ',iter,' -> ',m)
    

    mul(m,iter)


mul(998888887777772,0)