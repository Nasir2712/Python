from random import randrange
print (" INTEGER DIVISION ")
while(True):
    a= randrange(20)
    b= randrange(10)
    try:
        answer = a/b
    except:
        answer = -1
    print ("",a,"/",b,"=",)
    number = input("")
    try:
        if int(answer) == int(number):
            print ("You are absolutely right !!!")
            break
        else:
            print("This answer is incorrect")
            print("Please keep trying")
    except ValueError:
        print("Please Enter Integers Only !!!")
