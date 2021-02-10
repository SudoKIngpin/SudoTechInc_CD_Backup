
#QUESTION21
# store record of employee and display records...


import mysql.connector as ms 
mycon=ms.connect(host='localhost',user='root',passwd='admin',database='Emg')
cursor=mycon.cursor()
print('1. Store record')
print('2. Display records')
ch=int(input("Enter choice:"))
if ch==1:
    eno=int(input("Enter Employee no:"))
    ename=input("Enter Employee Name:")
    sal=input("Enter Salary:")
    q='insert into Employee values({},"{}",{})'.format(eno,ename,sal)
    mycon.commit()
    print("Record added successfully!")
    
else:
    q='Select * from Employee'
    cursor.execute(q)
    r=cursor.fetchall()
    for row in r:
        print(row)


        


