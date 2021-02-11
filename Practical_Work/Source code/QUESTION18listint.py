##Question 18
##Program that accepts a list of x and sets all -ve to left and +ve to right of the list.
l=[]
n=int(input('Enter no of elements in list:'))
for i in range(n):
    a=int(input('Enter integer:'))
    l.append(a)
    l.sort()
print('Your list is' , l)

