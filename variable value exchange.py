import time
def get_num():
    while True:
        try:
            get_num = int(input("Enter a number between 1 and 10: "))
            if get_num < 1 or get_num > 10:
                print("Invalid number. Please enter a number between 1 and 10.")
                continue
            return get_num
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
a = get_num()
print(f"Your number is {a}")
time.sleep(2)
b = get_num()
print(f"Your number is {b}")
time.sleep(2)

c = a
a = b
b = c
print(f"a is now {a} and b is now {b}")
