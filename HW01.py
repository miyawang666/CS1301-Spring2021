"""
Georgia Institute of Technology - CS1301
HW01 - Functions and Expressions
Name:Zhiqing Wang
GTID:903541413
"""

#########################################

"""
Function Name: bake()
Parameters: N/A
Returns: None
"""
def bake():
    cakes = int(input("How many cakes do you want?"))
    cupcake = int(input("How many cupcakes do you want?"))
    cookies = int(input("How many cookies do you want?"))
    hour = (100 * cakes +70 * cupcake +45 * cookies) // 60
    mins = (100 * cakes +70 * cupcake +45 * cookies) % 60
    print("It will take {} hours and {} minutes to make {} cakes, {} cupcakes, and {} cookies.".format(hour, mins,cakes,cupcake,cookies))
#########################################

"""
Function Name: cakeVolume()
Parameters: N/A
Returns: None
"""

def cakeVolume():
    r=float(input("What is the radius of the cake? "))
    h=float(input("What is the height of the cake? "))
    pi = float(3.14)
    v=((r)**2)*3.14*h
    v=round(v,2)
    print("The volume of the cake is {}.".format(v))   

#########################################

"""
Function Name: celebrate()
Parameters: N/A
Returns: None
"""
def celebrate():
    pizza = input("How many pizzas do you want? ")
    pasta = input("How many orders of pasta do you want? ")
    burger = input("How many burgers do you want? ")
    tip_percent = input("What percent would you like to tip? ")

    total = int(pizza)*14 + int(pasta)*10 + int(burger)*7
    tip = int(tip_percent)*0.01 *total
    tip = round(tip,2)
    total = total + tip
    total= round(total,2)
    print("You paid ${} and tipped ${}.".format(total,tip))
    

#########################################

"""
Function Name: bookstore()
Parameters: N/A
Returns: None
"""
def bookstore():
    day = input("How many days have you had this book for? ")
    day = int(day)
    total = (day - 14) * 0.25
    print("Your total amount due is ${}.".format(total))

#########################################

"""
Function Name: monthlyAllowance()
Parameters: N/A
Returns: None
"""
def monthlyAllowance():
    allowance = input("How much is your allowance this month? ")
    percent = float(input("What percentage do you want to save? "))
    left = float(allowance) * (100-percent)* 0.01 - 5.50 - 3.99
    print("You have ${} left after savings and fees.".format(left))



