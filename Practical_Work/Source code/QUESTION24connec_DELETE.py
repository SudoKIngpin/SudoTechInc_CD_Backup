# QUESTION 24
#Deleting records of entered employee number.
import mysql.connector as ms 
mycon=ms.connect(host='localhost',user='root',passwd='admin',database='Emg')
cursor=mycon.cursor()
eno=int(input("Enter Employee no:"))
q='Select * from Employee where EmpNo={}'.format(eno)
cursor.execute(q)
res=cursor.fetchone()
if res!=None:
    q='delete from Employee where EmpNo={}'.format(eno)
    mycon.commit()
    print('Record deleted successfully!')
    
else:
    print("Invalid Emp Number!")


