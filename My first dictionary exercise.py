numbers_str = input("Enter 5 integers separated by spaces: ")
numbers = numbers_str.split()
numbers = [int(n) for n in numbers]
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
print("Frequency of each number:")
for num, freq in frequency.items():
    if freq > 1:
        print(f"The number {num} appears {freq} times.")
    else:
        print(f"The number {num} appears once.")
