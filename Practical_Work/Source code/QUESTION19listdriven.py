##QUESTION 19
#mENU DRIVEN PROGRAM TO implement various insertion and deletion method 

T='y'
while T=='y' or T=='Y':
    def menu():
        print("*Menu Driven Insertion and Deletion in LIST*")
        print('1. Using insert() ')
        print('2. Using append() ')
        print('3. Using extend() ')
        print('4. Using pop() ')
        print('5. Using remove() ')
        print('6. Using delete  command ')
        print('7. Type 0 to exit')
    menu()
    l=eval(input('Enter your list here:'))
    ch=int(input('Enter your choice:'))
    if ch==0:
        exit()
    elif ch==1:
        ele=eval(input('Enter element to be inserted:'))
        idx=int(input('Enter position to insert element :'))
        l.insert(idx-1,ele)
        print('Element Inserted !',l)
    elif ch==2:
        el=eval(input('Enter element to be inserted:'))
        l.append(el)
        print('Element appended!',l)
    elif ch==3:
        l1=eval(input("Enter list to be inserted:"))
        l.extend(l1)
        print('List inserted!',l)
        
    elif ch==4:
        print('Pop will by default remove element at last!')
        chi=input('Do you want to change if yes, type "y", otherwise hit enter :')
        if chi=='y':
            idx=int(input('Enter new position : '))
            del l[idx-1]
            print('Element from your given position has been removed!!',l)
            
        else:
            l.pop()
            print('Element popped successfully!',l)
    elif ch==5:
        el=eval(input('Enter element to be removed:'))
        l.remove(el)
        print('Element removed Successfully!!',l)
    else :
        id=int(input('Enter position of element to be removed:'))
        del l[id-1]
        print('Deleted successfully from given position',l)
    T=input("Want to continue type 'Y' /  'y'  :" )





    
