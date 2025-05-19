#Write a program  to check whether the student can take the exam or not Students will be allowed in only two conditions: If they have a medical cause ("Y" for yes and "N" for no.) If yes then they will be allowed If no then check attendance if above 75 they can take the exam otherwise not
M=input("Any Medical cause? (Yes/No): ")
if M.lower() == 'yes' :
    C=input("Do you have a medifical sertificate ? (Yes/No): ")
    if C.lower() == 'yes' :
        print("You can take the exam")
    else :
        print("You cannot take the exam")
else :
    A=int(input("Enter Students Attendance Percentage: "))
    if A>75:
        print("You can take the exam")
    else:
        print("You cannot take the exam")