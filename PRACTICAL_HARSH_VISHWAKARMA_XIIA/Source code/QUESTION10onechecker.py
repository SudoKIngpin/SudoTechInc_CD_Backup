##Question10
##Function that takes two nos and return that which has minimum one's digit 
def one_checker(n1,n2):
    first_n=n1%10
    sec_n=n2%10
    if first_n<sec_n:
        return n1
    elif first_n>sec_n:
        return n2
    else:
        return "Ones digit of both numbers are same"
n1=int(input("Enter 1st no: "))
n2=int(input("Enter 2nd no: "))
res=one_checker(n1,n2)
print(res,"has minimum one's value ")
