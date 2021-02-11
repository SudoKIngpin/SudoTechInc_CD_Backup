#QUESTION 11
#Menu driven program for string manipulation
#
T='y'
while T=='y' or T=='Y':
  def menu():
      print('**MENU DRIVEN PROGRAM FOR STRING MANIPULATION**')
      print('1. For capitalize() ')
      print('2. For lower() ')
      print('3. For upper()')
      print('4. For swapcase() ')
      print('5. For title() ')
      print('6. For count()')
      print('7. For find() ')
      print('0 To exit ....')

  menu()
  temp=input("Enter your string:")
  choice=int(input("Enter your choice: "))

  if choice==0:
    exit()
    
  elif choice==1:
    res1=temp.capitalize()
    print(res1)

  elif choice==2:
    res2=temp.lower()
    print(res2)
    
  elif choice==3:
    res3=temp.upper()
    print(res3)

  elif choice==4:
    res4=temp.swapcase()
    print(res4)

  elif choice==5:
    res5=temp.title()
    print(res5)

  elif choice==6:
    ele=input('Element to count:')
    res6=temp.count(ele)
    print(res6)
    
  else:
    ele=input('Enter element to found:')
    res7=temp.find(ele)
    print('Element found at position', res7+1)   

  T=input("Press y to continue, n to exit : ")

    
    
