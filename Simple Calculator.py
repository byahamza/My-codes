def calc():
    def add(a , b):
        return a + b
    
    def sub(a , b):
        return a - b
    
    def mul(a , b):
        return a * b
    
    def div(a , b):
        if b == 0 and a > 0:
            return "+inf"
        elif b == 0 and a < 0:
            return "-inf" 
        elif b == 0 and a == 0:
            return "undefined"
        else:
            return a / b
    
    def get_num(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
    a = get_num("Enter first number: ")
    b = get_num("Enter second number: ")
    op = input("Enter operation (+ , - , * , /):")
    while op not in ("+" , "-" , "*" , "/"):
        print("Invalid input . Please enter one of + , - , * , /")
        op = input("Enter operation (+ , - , * , /):")
    if op == "+":
        result = add(a , b)
    elif op == "-":
        result = sub(a , b)
    elif op == "*":
        result = mul(a , b)
    elif op == "/":
        result = div(a , b)
    
    print(f"The result of {a} {op} {b} = {result} ")

attempts = 0
while True:
    attempts += 1
    print(f"\n--- Calculator: Attempt#{attempts} ---")
    calc()
    cont = input("Do you want to perform another calculation? (y/n): ").strip().lower()
    while cont not in ("y" , "n"):
        print("Invalid input. Please enter 'y' or 'n'.")
        cont = input("Do you want to perform another calculation? (y/n): ").strip().lower()
    if cont == "n":
        print("Goodbye!")
        exit()
    else:
        print("Let's do another calculation!")
        continue
