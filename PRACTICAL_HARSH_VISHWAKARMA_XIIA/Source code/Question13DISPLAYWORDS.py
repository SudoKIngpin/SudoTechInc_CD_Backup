##Question 13

##read words from text file less than 4 characters

def DISPLAYWORDS(filename):
    ct=0
    file=open(filename)
    line=file.read()
    list_word=line.split()
    for word in list_word:
        if len(word)<4:
            print(word)
    file.close()
DISPLAYWORDS('Story.txt')
