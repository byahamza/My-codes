while True:
    try:
        number = int(input("Enter a positive integer greater than 1: "))
        if number <= 1:
            print("The number must be greater than 1. Please try again.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer greater than 1.")
        continue
def is_prime(number):
    for i in range(2, int(number ** 0.5)+1):
        if number % i == 0:
            return False
    return True
if is_prime(number):
    print(f"The number {number} is a prime number.")
else:
    print(f"The number {number} is not a prime number.")
