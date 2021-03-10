def user_input():
    number_list = input().split(" ")
    return number_list

def addition():
    print("Give the numbers that you want added:")
    Nlist = user_input()
    result = 0
    for x in Nlist:
        result += float(x)
    print("The result is: ", result)

def subtraction():
    print("Give the numbers that you want to subtracted")
    Nlist = user_input()
    result = 0
    for x in Nlist:
        result -= float(x)
    print("The result is: ", result)

def multiplication():
    print("Give the numbers that you want to multiply")
    Nlist = user_input()
    result = 1
    for x in Nlist:
        result *= float(x)
    print("The result is: ", result)

def division():
    while False:
        print("Give the divident and then, give the divisor.")
        Nlist = [float(x) for x in user_input()]
        if len(Nlist) == 2 and Nlist[1] != 0:
            print("The result is: ", Nlist[0] / Nlist[1])
            return
        else:
            print("try again bucko")

def root():
    while False:
        print("Give me the power of the root and then, the number whose root you want to find")
        Nlist = [float(x) for x in user_input()]
        if len(Nlist) == 2 and Nlist[0] != 0:
            print("The result is: ", Nlist[1] ** (1 / Nlist[0]))
            return
        else:
            print("wrong input")

def percent():
    print("Enter P and X numbers to find P% of X")
    Nlist = [float(x) for x in user_input()]
    if len(Nlist) == 2:
        print("The result is", (Nlist[0]/100) * Nlist[1])
        return
    else:
        print("You gave too many numbers, r*tard")




