#QUESTION12

#Count A in text file

def CountA(filename):
    ct=0
    with open(filename) as f:
        con=f.readlines()
        for i in con:
            if i[0]=="A":
                ct+=1
    return ct
res=CountA("story.txt")
print('Total lines starting with A is: ',res)
