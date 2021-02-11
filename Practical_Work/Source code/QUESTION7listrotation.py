#Question 7
# LIST  rotation program that rotates elements of list so that element at first index moves to second index ,
#element in second index moves to 3rd and element in last moves to first index.

lis=eval(input('Enter list : '))
last=lis[-1]
for i in range(len(lis)-1,0,-1):
    lis[i]=lis[i-1]
lis[0]=last
print(lis)
