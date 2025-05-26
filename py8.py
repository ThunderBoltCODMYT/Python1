#Write a program to check how many times a character is repeated in a word?
while True:
    w=input("Enter your word: ")
    ch=input("Enter your character: ")
    c=0
    for x in w:
        if x==ch:
            c+=1
    print("The character", ch, "is repeated", c, " number of times in the word", w)
    choice=input("Do you want to continue? (yes/no): ")
    if choice not in ('y','Y'):
        break
