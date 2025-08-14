while True:
    try:
        equation_type = int(input("Enter the type of equation 1:linear or 2:quadratic :"))
        if equation_type not in [1, 2]:
            print("Incorrect choice. Please enter 1 for linear or 2 for quadratic :")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a number :")
if equation_type == 1:
    while True:
        try:
            a = float(input("Enter the coefficient a (non-zero): "))
            if a == 0:
                print("Coefficient a cannot be zero for a linear equation.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number for coefficient a:")
    while True:
        try:
            b = float(input("Enter the coefficient b: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for coefficient b:")
    x = -b / a
    print(f"The solution to the linear equation {a}x + ({b}) = 0 is x = {x}")
else:
    while True:
        try:
            a = float(input("Enter the coefficient a (non-zero): "))
            if a == 0:
                print("Coefficient a cannot be zero for a quadratic equation.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number for coefficient a:")
    while True:
        try:
            b = float(input("Enter the coefficient b: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for coefficient b:")
    while True:
        try:
            c = float(input("Enter the coefficient c: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for coefficient c:")
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b + discriminant**0.5) / (2*a)
        x2 = (-b - discriminant**0.5) / (2*a)
        print(f"The quadratic equation {a}x^2 + ({b})x + ({c}) = 0 has two real solutions: x1 = {x1} and x2 = {x2}")
    elif discriminant == 0:
        x = -b / (2*a)
        print(f"The quadratic equation {a}x^2 + ({b})x + ({c}) = 0 has one real solution: x = {x}")
    else:
        print("The quadratic equation has complex solutions.")
        real_part = -b / (2*a)
        imaginary_part = (-discriminant**0.5) / (2*a)
        print(f"The quadratic equation {a}x^2 + ({b})x + ({c}) = 0 has two complex solutions: x1 = {real_part} + {imaginary_part}i and x2 = {real_part} - {imaginary_part}i")
