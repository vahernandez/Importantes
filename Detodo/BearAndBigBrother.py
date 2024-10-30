pesos = [int(a) for a in input().split(" ")]
yearsA = (pesos[0] * 3 ) 
yearsB = (pesos[1] * 2 )

TotalYears = 1

while yearsA <= yearsB:
    yearsA = yearsA * 3
    yearsB = yearsB * 2
    TotalYears +=1
    
print(TotalYears)


a, b=map(int, input().split())
M=0
while a<=b:
 a=a*3
 b=b*2
 M=M+1
print(M)


a,b=map(int,input().split());c=0
while a<=b:a*=3;b*=2;c+=1
print(c)

