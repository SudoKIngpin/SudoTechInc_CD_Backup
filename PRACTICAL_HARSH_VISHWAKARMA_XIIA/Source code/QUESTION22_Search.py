#Question 22
#Search if not found display appropriate msg.
import mysql.connector as ms 
mycon=ms.connect(host='localhost',user='root',passwd='admin',database='Emg')
cursor=mycon.cursor()

eno=int(input("Enter Employee no :"))
chk_q='Select * from Employee where EmpNo={}'.format(eno)
cursor.execute(chk_q)
res=cursor.fetchone()
if res!=None:
    print("Record found, details are")
    print(res)
     
else:
    print("Employee details not found !")


