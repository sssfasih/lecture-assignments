'''
Design an application in which you can get all marks from your FSc Marks sheet;
 based on your marks decide either the person is passed in A+, A, B, C, D grades or got ”F” grade.
'''
header = "Usman Board of Education"
header_2 = "Annual Result card"
#Initial Valus rquired for making appropriate Sequences in program
info = 0
stud_1 = 0
stud_2 = 0
print(header)
print(header_2)
print("DATA ENTRY:")
students = []
stud_1 = input("Enter Name of student 1: ")
students.append(stud_1)
yn = input("another student? Y/N")
if yn == "y" or yn == "Y":
    stud_2 = input("Enter Name of student 2: ")
    students.append(stud_2)
    yn2 = input("another student? Y/N: ")
    if yn2== 'y' or yn2=='Y':
        print("Program is designed on Trial basis for Max 2 students")
        print("For full version Please Contant Syed Fasih Uddin")
        print("Roll No: 19B-029-SE")
        quit()
print("DATA ENTRY")
for name in students:
    print("STUDENT NAME:",name)
    eng = int(input("Enter Marks Obtained in English: "))
    urdu = int(input("Enter Marks Obtained in Urdu: "))
    maths = int(input("Enter Marks Obtained in Maths: "))
    physics = int(input("Enter Marks Obtained in Physics: "))
    pst = int(input("Enter Marks Obtained in PST: "))
    if info == 0:
        data1 = [eng,urdu,maths,physics,pst]
        info = info + 1
    if info == 1:
        data2 = [eng,urdu,maths,physics,pst]
print("Data collection completed")
yn3 = input("Print Marksheets? y/n :")
if yn3 == "y" or yn3 == "Y" :
    print("Printing Marksheets")
else :
    print("Why on earth you input data if you didn't want to print Marksheets")
    print("Ending Program")
    quit()
for name in students:
    print(header)
    print(header_2)
    if name == stud_1:
        print("Student Name:",name)
        print("Marks Obtained in English: ",data1[0])
        print("Marks Obtained in Urdu: ",data1[1])
        print("Marks Obtained in Maths: ",data1[2])
        print("Marks Obtained in Physics: ",data1[3])
        print("Marks Obtained in Pakistan Studies: ",data1[4])
        obt = data1[0] + data1[1] + data1[2] + data1[3] + data1[4]
        print("Total Marks Obtained: ",obt)
        print("Maximum Marks: ",500)
        print ("Percentage:",(obt/500)*100)
        input("\n \n Enter Anything to continue: ")
    if name == stud_2:
        print(" \n Student Name:", name)
        print("Marks Obtained in English: ", data2[0])
        print("Marks Obtained in Urdu: ", data2[1])
        print("Marks Obtained in Maths: ", data2[2])
        print("Marks Obtained in Physics: ", data2[3])
        print("Marks Obtained in Pakistan Studies: ", data2[4])
        obt = data2[0] + data2[1] + data2[2] + data2[3] + data2[4]
        print("Total Marks Obtained: ", obt)
        print("Maximum Marks: ", 500)
        print("Percentage:", (obt / 500) * 100)
# End of Program
#
