a=[[1,2,3],[4,5,6],[1,4,7]]
b=[[1,4,3],[6,7,8],[3,4,5]]
c=[[0,0,0],[0,0,0,],[0,0,0]]
ads=0
mul=0
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            c[i][j]=c[i][j]+(a[i][k]*b[k][j])
            ads=ads+1
            mul=mul+1
        ads=ads-1
print("Number of scalar addition : ",ads)
print("Total numner of multiplication : ",mul)