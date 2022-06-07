import random 
thislist=["McDonalds", "In N Out", "Burger King"]
print(thislist) 
menu1 = ["French Fries", "Big Mac", "Mc Nuggets"] 
menu2 = ["French Fries", "Double double", "Triple triple"] 
menu3 = ["French Fries", "Whopper", "Chicken fries"] 

y=random.randrange(0,3) 
x=input("Which restaurant? ")
if x=="McDonalds":
    print(menu1)
    print(menu1[y]) 
elif x=="In N Out":
    print(menu2)
    print(menu2[y])
elif x=="Burger King":
    print(menu3)
    print(menu3[y]) 
else: 
    print("You didn't choose a restaurant.")
    

    