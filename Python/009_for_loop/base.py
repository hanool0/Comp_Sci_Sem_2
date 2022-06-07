x=int(input("Please enter line length: "))
y=str(input("Do you want a horizontal or vertical line? ")) 

a = "*"

if y == "vertical": 
    for a in range(0,x):
        print("*")

elif y == "horizontal":
    for a in range(0,x): 
        print("*", end =" ") 

else:
    print("You have not entered a line command.") 
    