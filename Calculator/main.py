
proceed = "y"
while proceed == "y":
    f_num = float(input("Enter the first number>>"))
    oper = input("Enter operation>>")
    s_num = float(input("Enter the second number>>"))
    if oper == "+":
        print(f_num + s_num)
    elif oper == "-":
        print(f_num - s_num)
    elif oper == "*":
        print(f_num * s_num)
    elif oper == "/":
        print(f_num % s_num)
    else:
        print("Error")
    proceed = input("Enter 'y' to continue and other key to finish>>")
