#QUESTION23
#Update record of entered employee number..
import mysql.connector as ms 
mycon=ms.connect(host='localhost',user='root',passwd='admin',database='Emg')
cursor=mycon.cursor()
eno=int(input("Enter Employee no:"))
q='Select * from Employee where EmpNo={}'.format(eno)
cursor.execute(q)
r=cursor.fetchone()
if r!=None:
    eno=int(input("Enter  new Employee no:"))
    ename=input("Enter new Employee Name:")
    sal=input("Enter new Salary:")
    q='update Employee set Empno={},EmpName="{}",Sal={}'.format(eno,ename,sal)
    mycon.commit()
    print("Record updated successfully!")
    
else:
    print("Record does not exist !")


