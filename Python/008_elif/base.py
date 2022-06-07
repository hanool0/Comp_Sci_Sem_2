x=int(input("Please enter a number: "))
y=(input("Please enter a operation: "))
z=int(input("Please enter another number: "))

if y == "+": 
    print(x + z)
elif y == "-": 
    print(x - z)
elif y == "*":
    print(x * z)
elif y == "/":
    print(x / z)
else: 
    print("You did not enter an operation.")
    