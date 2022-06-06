##takes argument as Augmented Matrix-->
def GJ_Elimination(M):
    n=len(M)
    r_multiply=lambda r,s:[round((s*i),10) for i in r]    #row multiplication by a number 's'
    r_subtract=lambda r1,r2:[(r1[i]-r2[i]) for i in range(len(r1))]    #Subtraction of rows
    for k in range(n):    #interchanging row having diagonal element = 0
        if M[k][k]==0:
            m=k+1
            while m!=k:
                if m==n:
                    m=0
                if M[m][k]!=0:
                    M[k],M[m]=M[m],M[k]
                    break
                m+=1
    for j in range(n):
        for i in range(n):
            if i!=j:        # for making all elements '0' except for diagonal elements
                M[i]=r_subtract(M[i],r_multiply(M[j],(M[i][j]/M[j][j])))
            else:           # for making all diagonal elements '1'
                M[i]=r_multiply(M[i],(1/M[i][j]))
    return M
m=[[0,2,1,4],[1,1,2,6],[2,1,1,7]]
m1=GJ_Elimination(m)
for i in range(len(m1)+1):
    for j in range(len(m1)):
        m1[j][i]=str(m1[j][i])
for i in range(len(m1)):
    print('X{} = '.format(i+1),(m1[i])[-1])
for j in range(len(m1)):
    (m1[j])[-1]=':  ' + (m1[j])[-1]
    
for i in m1:
    print(i)

