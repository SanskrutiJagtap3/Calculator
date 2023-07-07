n1=int(input("Enter First Number: "))
n2=int(input("Enter Second Number: "))
print(" 1)Addition\n 2)Subtraction\n 3)Multiplication \n 4)Division")
o1=int(input("Ente mode of calculation: "))
if (o1 == 1): 
    print("Addition is: ",n1+n2)
elif o1==2:
    print("Subtraction is: ",n1-n2)
elif o1==3:
    print("Multiplication is: ",n1*n2)
elif o1==4: 
    print("Division is: ",n1/n2)
