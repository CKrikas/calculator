def user_input():
    number_list = input().split(" ")
    number_list = [float(x) for x in number_list]
    return number_list

def continue_program():
    ye_or_nah = input("Do you want to do another calculation sir? y/n")
    while ye_or_nah != "y" and ye_or_nah != "n":
        ye_or_nah = input("Please type y to make another calculation or n to stop")
    return ye_or_nah

def addition():
    print("Give the numbers that you want added:")
    Nlist = user_input()
    result = 0
    for x in Nlist:
        result += x
    print("The result is: ", result)
    return continue_program()

def subtraction():
    print("Give the numbers that you want to subtract")
    Nlist = user_input()
    result = 0
    for x in Nlist:
        result -= x
    print("The result is: ", result)
    return continue_program()

def multiplication():
    print("Give the numbers that you want to multiply")
    Nlist = user_input()
    result = 1
    for x in Nlist:
        result *= x
    print("The result is: ", result)
    return continue_program()

def division():
    while False:
        print("Give the divident and then, give the divisor")
        Nlist = user_input()
        if len(Nlist) == 2 and Nlist[1] != 0:
            print("The result is: ", Nlist[0] / Nlist[1])
            return
        else:
            print("try again bucko")
    return continue_program()

def root():
    while False:
        print("Give me the power of the root and then, the number whose root you want to find")
        Nlist = user_input()
        if len(Nlist) == 2 and Nlist[0] != 0:
            print("The result is: ", Nlist[1] ** (1 / Nlist[0]))
            return
        else:
            print("wrong input")
    return continue_program()

def percent():
    print("Enter P and X numbers to find P% of X")
    Nlist = user_input()
    if len(Nlist) == 2:
        print("The result is", (Nlist[0]/100) * Nlist[1])
        return
    else:
        print("You gave too many numbers, r*tard")
    return continue_program()

program_running = "y"
while program_running == "y":
    print("Welcome, what would you like to calculate today?\nSelect one by inputing a number to procede\n1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n5. Root\n6. Percent\n0. Exit")
    while True:
        choice = input()
        if choice == "1":
            program_running = addition()
        elif choice == "2":
            program_running = subtraction()
        elif choice == "3":
            program_running = multiplication()
        elif choice == "4":    
            program_running = division()
        elif choice == "5":
            program_running = root()
        elif choice == "6":
            program_running = percent()
        elif choice == "0":
            program_running = "n"
            break
        else:
            print("Wrong input, please try again")
        break
