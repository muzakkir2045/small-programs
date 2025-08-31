

def add(a:int, b:int):
    return a + b

def sub(a:int, b:int):
    return a - b

def mul(a:int, b:int):
    return a * b

def div(a:int, b:int):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

op = ["Add","Subtract","Multiply","Divide","Exit"]

while True:
    print("\n=== Simple CLI Calculator ===")
    print("Choose operation:")
    for ind,val in enumerate(op,start = 1):
        print(ind,".",val)
    
    choice = int(input("Enter choice 1-5 : "))

    if choice == 5:
        print("Exiting calculator")
        break

    if choice not in [1, 2, 3, 4]:
        print("Invalid choice. Please select a valid option.")
        continue

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number. Please enter numeric values.")
        continue

    if choice == 1:
        print(f"The sum of two numbers is {add(a,b)}")
    elif choice == 2:
        print(f"The difference of two numbers is {sub(a,b)}")
    elif choice == 3:
        print(f"The multiplication of two numbers is {mul(a,b)}")
    elif choice == 4:
        print(f"The division of two numbers is {div(a,b)}")
    else:
        print("Invalid choice, Please select a valid option.")
