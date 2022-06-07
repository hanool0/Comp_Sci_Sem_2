import random 
thislist = [1,2,3,4,5,6,7,8,9,10] 

x=int(input("Enter the amount of random numbers you want:")) 
print("your random numbers are: ")
for i in range(1, x + 1): 
    print(thislist[random.randrange(10)], end=" ") 