#Design an application of taking admission process in UIT?
print("Welcome To UIT Online Admissions")
input("Please Press Enter to continue")
name= input("Enter Your Name:")
fname= input("Enter Your Father's Name:")
matric =eval(input("Enter Your Matric %"))
inter = eval(input("Enter Your Inter %"))
uit = eval(input("Enter Your Marks in UIT/NED Test"))
if uit<50:
    uittest="not clear"
else:
    uittest= 'clear'
if matric < 50:
    print("Dear Applicant,{}, You are not eligible for admission as your Matric Marks are below 50%".format(name.title()))
else:
    if inter < 60:
        print("Dear Applicant,{}, You are not eligible for admission as your Inter Marks are below 60%".format(name.title()))
    else:
        if uittest == 'clear' :
            print("Dear Applicant,{},Please wait while UIT Admission Department processes your data".format(name.title()))
            print("You will be called if your name makes into the merit list")
