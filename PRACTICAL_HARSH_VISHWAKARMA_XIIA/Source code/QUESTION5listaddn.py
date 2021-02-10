##QUESTION5
##Takes two list e.g.[3,1,4],[1,5,9]
##Then equal to [4,6,13]

l3=[] 
_sum_=0
l1=[1,5,8]
l2=[4,8,12]
len_list=len(l1)
for i in range(len_list):
    _sum_=l1[i]+l2[i]
    l3.append(_sum_)
    _sum_=0
print("L1 : ",l1)
print('L2: ',l2)
print('New list : ',l3)
    
    
