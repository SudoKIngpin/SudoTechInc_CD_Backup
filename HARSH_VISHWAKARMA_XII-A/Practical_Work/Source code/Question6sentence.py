##QUESTION6
##Input sentence and print stats
##number of words
##number of characters (including whitespace and punctuation)
##Percentage of characters that are alphanumeric.

ct_alnum=0
sen=input("Type sentence : ")
print(sen)
no_of_char=len(sen)
l1=sen.split()
word_ct=0
for i in l1:
    word_ct+=1 #no of words
for j in l1:
    if j.isalnum():
        ct_alnum+=1
r_alnum=(ct_alnum)/(no_of_char)
print("Number of words :",word_ct)
print("Number of characters :",no_of_char)
print("% of alphanumeric characters:",(r_alnum*100))

