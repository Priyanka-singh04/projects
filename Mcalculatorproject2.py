from MCalfuntion import*
from math import *
while True:
    print("\t------CALCULATOR-------")
    print("What do u want to do?")
    print("1 Addition")
    print("2 Substraction")
    print("3 Multiplication")
    print("4 Division")
    print("5 Modulo")
    print("6 Square root")
    print("7 Sine in radian")
    print("8 sine in degree")
    print("9 cos in radian")
    print("10 cos in degree")
    print("11 tan in radian")
    print("12 tan in degree")
    print("13 cosec in radian")
    print("14 cosec in degree")
    print("15 sec in radian")
    print("16 sec in degree")
    print("17 cot in radian")
    print("18 cot in degree")
    print("19 log10")
    print("20 ln")
    print("21 powerof")
    #print("22 pie")
    #print("23 logbasex")
    print("Enter Q or q to Exit")

    choice=input("Enter your Choice:")

    if choice =='Q' or choice =='q':
        break
    if choice=='1':
        print("enter two number:")
        num1=float(input("enter Number 1:"))
        num2=float(input("enter Number2:"))
        addition(num1,num2)

    elif choice=='2':
        print("enter two number:")
        num1 = float(input("enter Number 1:"))
        num2 = float(input("enter Number2:"))
        subtraction(num1,num2)
    elif choice=='3':
        print("enter two number:")
        num1 = float(input("enter Number 1:"))
        num2 = float(input("enter Number2:"))
        multiplication(num1,num2)
    elif choice=='4':
        print("enter two number:")
        num1 = float(input("enter Number 1:"))
        num2 = float(input("enter Number2:"))
        division(num1,num2)
    elif choice=='5':
        print("enter two number:")
        num1 = float(input("enter Number 1:"))
        num2 = float(input("enter Number2:"))
        modulo(num1,num2)
    elif choice=='6':
        print("enter the number:")
        num1 = float(input("enter Number 1:"))
        #num2 = float(input("enter Number2:"))
        r=sqrt(num1)
        print("\n the square root is:%s"%r)
    elif choice=='7':
        #print("enter the number:")
        num1=int(input("enter the number:"))
        x=sin(num1)
        print("\n the sine value in radian is:%f"%x)
    elif choice=='8':
        num1 = int(input("enter the number:"))
        x = sin(math.radians(num1))
        print("\n the sine value in degree is:%f" % x)
    elif choice=='9':
        num1 = int(input("enter the number:"))
        x = cos(num1)
        print("\n the cos value in radian is:%f" % x)
    elif choice=='10':
        num1 = int(input("enter the number:"))
        x = cos(math.radians(num1))
        print("\n the log value in degree is:%f" % x)
    elif choice=='11':
        num1=int(input("enter the number"))
        x=tan(num1)
        print("\n the tan value in radian is:%f" % x)
    elif choice=='12':
        num1 = int(input("enter the number"))
        x = tan(math.radians(num1))
        print("\n the tan value in degree is:%f" % x)
    elif choice=='13':
        num1 = int(input("enter the number"))
        x = 1/(sin(num1))
        print("\n the cosec value in radian is:%f" % x)
    elif choice=='14':
        num1=int(input("enter the number"))
        x=1/(sin(math.radians(num1)))
        print("\n the cosec value in degree is:%f" % x)
    elif choice=='15':
        num1 = int(input("enter the number"))
        x = 1/(cos(num1))
        print("\n the sec value in radian is:%f" % x)
    elif choice=='16':
        num1 = int(input("enter the number"))
        x = 1 /(cos(math.radians(num1)))
        print("\n the sec value in degree is:%f" % x)
    elif choice=='17':
        num1 = int(input("enter the number"))
        x = 1 /(tan(num1))
        print("\n the cot value in radian is:%f" % x)
    elif choice=='18':
        num1 = int(input("enter the number"))
        x = 1 /(tan(math.radians(num1)))
        print("\n the cot value in degree is:%f" % x)
    elif choice=='19':
        num1 = int(input("enter the number"))
        x = log10(num1)
        print("\n the log10 value is:%f" % x)
    elif choice=='20':
        num1 = int(input("enter the number"))
        x = log(num1)
        print("\n the log natural(ln) value is:%f" % x)
    elif choice=='21':
        num1 = int(input("enter the number"))
        num2=float(input("enter its power:"))
        x = powerof(num1,num2)
        print("\n the powerof value is:%f" % x)
    #elif choice=='22':
      # num1=int(input("enter the number"))
        #x=pi()
        #print("\n the pie value is:" %x)
    #elif choice=='23':
     #   num1=float(int(input("enter the number")))
      #  num2=float(int(input("enter the logbasex")))
       # x=log(num1,num2)
        #print("\n the logbasex is:%f %f",num1,num2)
    else:
        print("Invalid choice")
    print("\n")

