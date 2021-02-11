#Question15
#To save dictionary records to students.csv
#1. Sno','Student','Subject'
#2. 1,'Shilpa','English
#3  2,"Sakshi",'Computer'
#4  3,"Sahil","Chemistry

import csv
with open('student.csv','w') as csvfile:
   mywriter=csv.writer(csvfile)
   mywriter.writerow(['Sno','Student','Subject'])
   mywriter.writerow([1,'Shilpa','English'])
   mywriter.writerow([2,"Sakshi",'Computer'])
   mywriter.writerow([3,"Sahil","Chemistry"])
   print("Records added Successfully !")
