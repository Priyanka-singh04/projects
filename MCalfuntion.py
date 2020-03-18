import math
def addition(num1,num2):
    result=num1+num2
    print("{0}+{1}={2}".format(num1,num2,result))
def subtraction(num1,num2):
    result=num1+num2
    print("{0}-{1}={2}".format(num1,num2,result))
def multiplication(num1,num2):
    result=num1*num2
    print("{0}*{1}={2}".format(num1,num2,result))
def division(num1,num2):
    if num2==0.0:
        print("Can't Do Divide by Zero")
    else:
        result=num1/num2
        print("{0}/{1}={2}".format(num1,num2,result))
def modulo(num1,num2):
    result=num1%num2
    print("{0}%{1}={2}".format(num1,num2,result))

def sqrt(a):
    x=math.sqrt(a)
    return x
def sinrad(a):
    y=math.sin(a)
    return y
def cosrad(a):
    y=math.cos(a)
    return y
def tanrad(a):
    y=math.tan(a)
    return y
def cosecrad(a):
    y=1/(math.sin(a))
    return y
def secrad(a):
    y=1/(math.cos(a))
    return y
def cotrad(a):
    y=1/(math.tan(a))
    return y
def sindeg(a):
    y=math.sin(math.radians(a))
    return y
def cosdeg(a):
    y=math.cos(math.radians(a))
    return y
def tandeg(a):
    y=math.tan(math.radians(a))
    return y
def cosecdeg(a):
    y=1/(math.sin(math.radians(a)))
    return y
def secdeg(a):
    y=1/(math.cos(math.radians(a)))
    return y
def cotdeg(a):
    y=1/(math.tan(math.radians(a)))
    return y
def logten(a):
    y=math.log10(a)
    return y
def ln(a):
    y=math.log(a)
    return y
def powerof(a,raiseby):
    y=math.pow(a,raiseby)
    return y
#def pi():
  #  y=math.pi()
  #  return y
#def logbasex(a,x):
 #  y=math.log(a,x)
  #  return y
