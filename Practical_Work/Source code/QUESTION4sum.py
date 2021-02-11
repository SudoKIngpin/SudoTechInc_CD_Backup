#Question4
#if n is +ve sum from n to 2*n 
###if n is -ve sum from  2*n to n
##Inclusive values (end points are included)

N=int(input("Enter number :"))
sum1=sum2=0
if N>0:
    upper_limit=(2*N)+1
    for i in range(N,upper_limit):
        sum1+=i
    print("Sum is",sum1)
        
elif N<0:
    upper_lim=N+1
    for j in range(2*N,upper_lim):
        sum2+=j
    print("Sum is",sum2)

else:
    print("The number is zero")
