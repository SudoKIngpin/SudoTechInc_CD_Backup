##Question9
##Function that recieves two numbers and generate random number from
#that range
##Main program should be able to print three nos randomly

import random 
def randgen(n1,n2):
    a=random.randint(n1,n2)
    return a
n1=int(input("Enter number :"))
n2=int(input("Enter number :"))
for i in range(3):
    ran_no=randgen(n1,n2)
    print(ran_no)
