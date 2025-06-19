def add(n1, n2):
    return n1+n2

def sub(n1, n2):
    return n1-n2

def mul(n1, n2):
    return n1*n2

def div(n1, n2):
    return n1/n2

dict  = {
    '+' : add,
    '-' : sub,
    '*' : mul,
    '/' : div
}

def calculator():
    first_number = int(input("Enter first number: \n"))
    bool_ = True
    while(True):
        
        opr = input("enter the operation you want to perform: '+' '-' '*' '/' \n")
        if opr not in dict:
            print("Enter a valid operator")
        else:    
            second_number = int(input("Enter second number: \n"))

            result = dict[opr](first_number, second_number)
            print(f"The answer is: {result}")
            yes_or_no = input("Do you wanna continue the calculation with the result? Type 'yes' to continue and 'no' if you want to start a new calulation\n")
            if yes_or_no == 'yes':
                first_number = result
            else:
                yes_or_no = False
                calculator()   

calculator()        