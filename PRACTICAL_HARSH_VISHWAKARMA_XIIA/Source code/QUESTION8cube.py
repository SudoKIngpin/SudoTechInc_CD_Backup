#QUESTION8
##write function
##cube that calculates cube for passed number (default arguement is 2)
##function that takes two char arguement and return True if both arguements are equal,otherwise
##true

def cube(a=2):
    return a**3

def check(char1,char2):
    if char1==char2:
        return True
    else:
        return False
res=cube()
print("If no arguement provided : ",res)
n=int(input("Enter number "))
print('Cube of given number is',cube(n))
c1=input('Enter 1st character: ')
c2=input('Enter 2nd character: ')
resp=check(c1,c2)
print(resp)
