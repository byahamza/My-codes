import time
def get_num():
    while True:
        try:
            num = int(input("Enter a number: "))
            return num
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
num = get_num()
time.sleep(1)
print(f"Your number is {num}")
parity = num % 2
time.sleep(1)
print(f"Calculating if {num} is even or odd...")
time.sleep(3)
if parity == 0:
    result = "even"
else:
    result = "odd"
print(f"By my calculations, your number wich is {num} is {result}.")
time.sleep(2)
print("Thank you for using my program.")
