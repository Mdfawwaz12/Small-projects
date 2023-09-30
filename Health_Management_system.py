def date():
    import datetime
    return datetime.datetime.now()
 
print("*******welcome to Health Management System*******")

while(True):
    print("press\n\t1.name for diet and exercise\n\t2.name for diet and exercise\n\t3.name for diet and exercise\n\t4.retrive the client detail\n\t5.New Client to register\n\t")
    a = int(input())

    if a ==1:
        print("welcome name")
        x = int(input("1.diet log\n2.exercise\n"))
        if x==1:
            f = open("name_diet.txt","w")
            a =[date()]
            b = input("what diet food to log: ")
            f.write(str(a))
            f.write(b)
        else:
            f = open("name_exercise.txt", "w")
            a = [date()]
            b = input("enter exercise to log: ")
            f.write(str(a))
            f.write(b)

    if a ==2:
        print("welcome name")
        x = int(input("1.diet log\n2.exercise\n"))
        if x==1:
            f = open("name_diet.txt","w")
            a =[date()]
            b = input("what diet food to log: ")
            f.write(str(a))
            f.write(b)
        else:
            f = open("name_exercise.txt", "w")
            a = [date()]
            b = input("enter exercise to log: ")
            f.write(str(a))
            f.write(b)

    if a ==3:
        print("welcome name")
        x = int(input("1.diet log\n2.exercise\n"))
        if x==1:
            f = open("name_diet.txt","w")
            a =[date()]
            b = input("what diet food to log: ")
            f.write(str(a))
            f.write(b)
        else:
            f = open("name_exercise.txt", "w")
            a = [date()]
            b = input("enter exercise to log: ")
            f.write(str(a))
            f.write(b)
    print("file has been created")

    if a ==4:
        b = input("enter client name: ")
        x = int(input("1.diet\n2.exercise\n"))  
        if x==1:
         f = open(b + "_" +"diet" + ".txt")
         content = f.read()
         print(content)
        else:
          f = open(b + "_" +"exercise" + ".txt")
          content = f.read()
          print(content)
    
    if a ==5:
        user_inp = input("Enter your name: ")
        print("you have been registered\n")
        x = int(input("enter\n\t1.diet\n\t2.exercise\n\t"))  
        if x==1:
         f = open(user_inp + "_" +"diet" + ".txt","w")
         a = [str(date())]
         b = input("Enter diet food to log: ")
         f.write(str(a))
         f.write(b)
        else:
          user_inp = input("Enter your name: ")
          print("you have been registered\n")
          x = int(input("enter\n\t1.diet\n\t2.exercise\n\t"))  
          f = open(user_inp + "_" +"exercise" + ".txt","w")
          a = [str(date())]
          b = input("Enter exercise food to log: ")
          f.write(str(a))
          f.write(b)
  
    inp = input("you do want to continue, yes to continue and no to press 6: ")
    if inp == 'yes':
        continue

    if inp=='6':
        print("*****thank you*****")
        exit()
