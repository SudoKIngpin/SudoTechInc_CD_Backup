#Question1
# PALINDROME CHECker

a=input("Enter your word:")
b=a[::-1] #Reversing a string
if a.lower()==b.lower():# Converting all to lowercase for matching
    print('Entered word is a palindrome')
else:
    print('Entered word is not a palindrome')
    
