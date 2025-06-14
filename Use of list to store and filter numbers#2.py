import time
numbers = []
for i in range(6):
    while True:
        try:
            num = int(input(f"Enter number {i + 1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
print(f"The list of numbers is: {numbers}")
time.sleep(1)
even_numbers = [n for n in numbers if n % 2 == 0]
print(f"The even numbers are: {even_numbers}")
