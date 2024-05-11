def print_dotted_line(length=20):
    print("." * length)

def add(A,M):
    c=0
    for i in range(0,len(A)):
        A[i]=A[i]+M[i]+c
        if(A[i]>1):
            A[i]=(A[i]+1)%2
            c=1
        else:
            c=0
            
    return A


def two(M):
    M_compli=[0]*4
    for i in range(0,len(M)):
        M_compli[i]=(M[i]+1)%2
    
    X=[0,0,0,1]
    add(M_compli,X)
    return M_compli


def ASR(A, Q, Q_1):
    Q_1=Q[-1]  
    temp=A[-1]  
    for i in range(len(A) - 1, 0, -1):
        A[i] = A[i - 1]
        Q[i] = Q[i - 1]
    Q[0] = temp
    for i in range(0,len(A)):
        print(A[i],end="")
    print("\t",end="")
    for i in range(0,len(Q)):
        print(Q[i],end="")
    print("\t",end="")
    print(Q_1,"\t",end="")
    print("ASR")
    return A,Q,Q_1

def header(Q,Q_1):
    print("A \t",end="")
    print("Q \t",end="")
    print("Q_1 \t",end="")
    print("Operation")
    print("0000\t",end="")
    for i in range(0,len(Q)):
        print(Q[i],end="")
    print("\t",end="")
    print(Q_1,"\t",end="")
    print("Initialize")

def printer(A,Q,Q_1):
    for i in range(0,len(A)):
        print(A[i],end="")
    print("\t",end="")
    for i in range(0,len(Q)):
        print(Q[i],end="")
    print("\t",end="")
    print(Q_1,end="")
    print("\t",end="")
    if((Q[-1]==0) and (Q_1)==1):
        print("A=A+M")
    elif((Q[-1]==1) and (Q_1)==0):
        print("A=A-M")

def Algo(A,Q,M,Q_1):
    header(Q,Q_1)
    print_dotted_line(20)
    printer(A,Q,Q_1)
    print_dotted_line(20)
    counter=len(Q)
    while(counter!=-0):
        if((Q[-1]==0) and (Q_1)==1):
            A=add(A,M)
            printer(A,Q,Q_1)
            A,Q,Q_1=ASR(A,Q,Q_1)
        elif((Q[-1]==1) and (Q_1)==0):
            A=add(A,two(M))
            printer(A,Q,Q_1)
            A,Q,Q_1=ASR(A,Q,Q_1)
        elif((Q[-1]==0) and (Q_1)==0):
            A,Q,Q_1=ASR(A,Q,Q_1)
        elif((Q[-1]==1) and (Q_1)==1):
            A,Q,Q_1=ASR(A,Q,Q_1)
        counter = counter-1
        print_dotted_line(20)

    result=0
    for i in range(0,len(Q)):
        result=result+Q[i]*(2**i)
    
    print_dotted_line(30)
    print("Result in binary : ",end="")
    for i in range(0,len(Q)):
        print(Q[i],end="")
    print("\n")
    print("Result in decimal : ",result)
    print_dotted_line(30)
        


def main():
    A=[0,0,0,0]
    Q=[0,0,1,1]
    M=[0,0,1,1]
    Q_1=0
    Algo(A,Q,M,Q_1)

main()
