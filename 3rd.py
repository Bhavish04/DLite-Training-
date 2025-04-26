def is_disarium(num):
    """Check if a number is Disarium"""
    num_str = str(num)
    total = sum(int(digit) ** (idx + 1) for idx, digit in enumerate(num_str))
    return total == num

def first_a_disarium(a):
    """Print the first 'a' Disarium numbers"""
    print(f"First {a} Disarium numbers are:")
    count = 0
    num = 0
    while count < a:
        if is_disarium(num):
            print(num, end=" ")
            count += 1
        num += 1
    print("\n")  

def disarium_between(start, end):
    """Print Disarium numbers between two numbers"""
    print(f"Disarium numbers between {start} and {end} are:")
    found = False
    for num in range(start, end + 1):
        if is_disarium(num):
            print(num, end=" ")
            found = True
    if not found:
        print("None")
    print()  


print("1. Find first 'a' Disarium numbers")
print("2. Find Disarium numbers between two numbers")
choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    a = int(input("Enter how many Disarium numbers you want: "))
    first_a_disarium(a)
elif choice == 2:
    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))
    disarium_between(start, end)
else:
    print("Invalid choice. Please enter 1 or 2.")
def is_disarium(num):
    """Check if a number is Disarium"""
    num_str = str(num)
    total = sum(int(digit) ** (idx + 1) for idx, digit in enumerate(num_str))
    return total == num

def first_a_disarium(a):
    """Print the first 'a' Disarium numbers"""
    print(f"First {a} Disarium numbers are:")
    count = 0
    num = 0
    while count < a:
        if is_disarium(num):
            print(num, end=" ")
            count += 1
        num += 1
    print("\n")  

def disarium_between(start, end):
    """Print Disarium numbers between two numbers"""
    print(f"Disarium numbers between {start} and {end} are:")
    found = False
    for num in range(start, end + 1):
        if is_disarium(num):
            print(num, end=" ")
            found = True
    if not found:
        print("None")
    print()  
print("1. Find first 'a' Disarium numbers")
print("2. Find Disarium numbers between two numbers")
choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    a = int(input("Enter how many Disarium numbers you want: "))
    first_a_disarium(a)
elif choice == 2:
    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))
    disarium_between(start, end)
else:
    print("Invalid choice. Please enter 1 or 2.")