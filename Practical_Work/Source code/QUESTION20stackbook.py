#Question 20
#Menu driven program using function push(),pop(),display() to implement stack.'
##Program will store name of books.

def isEmpty(stk):
    if stk==[]:
        return True
    else:
        return False
def Push(stk,item):
    stk.append(item)
    top=len(stk)-1
def Pop(stk):
    if isEmpty(stk):
        return "Underflow"
    else:
        item=stk.pop()
        if len(stk)==0:
            top=None
        else:
            top=len(stk)-1
        return item
def Display(stk):
    if isEmpty(stk):
        print('Stack Empty')
    else:
        top=len(stk)-1
        i=len(stk)-1
        while i>=0:
            print(stk[i])
            i-=1
stk=[]
top=None
while True:
    print('1. Push') 
    print('2. Pop')
    print('3. DIsplay')
    print('4. Exit')
    ch=int(input("Enter your choice(1-3):"))
    if ch==1:
        item=(input("Enter item :"))
        Push(stk,item)
    elif ch==2:
        item=Pop(stk)
        if item=="Underflow":
            print("Underflow stack is Empty")
        else:
            print("Popped item is :",item)
         
    elif ch==3:
        Display(stk)
    else:
        exit()
    
