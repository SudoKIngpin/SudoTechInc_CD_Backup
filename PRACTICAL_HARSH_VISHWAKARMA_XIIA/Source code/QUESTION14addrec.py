#QUESTIION 14
#add record to binary file 'student ' 

import pickle 
def addrecord(list1):
    with open('student.dat','wb') as fo:
        pickle.dump(list1,fo)
list1=[]
stu_no=int(input("Enter Student Number:"))
stu_name=input("Enter Student Name:")
stu_marks=int(input("Enter Student Marks:"))
list1.extend([stu_no,stu_name,stu_marks])
addrecord(list1)
print("Record added Successfully!")


    

