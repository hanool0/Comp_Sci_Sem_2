import random
thislist=["McDonalds"]
thislist2=["In N Out"]
thislist3=["Burger King"]
x=input(print("Choose a restaurant!" + (thislist) + (thislist2) + (thislist3)))

mc = menu1 = ["French Fries", "Big Mac", "Mc Nuggets"] 
out = menu2 = ["French Fries", "Double double", "Triple triple"] 
king = menu3 = ["French Fries", "Whopper", "Chicken fries"] 

y=random.randrange(0,2) 

if x == thislist:
    print(mc(y)) 
elif x == thislist2:
    print(out(y))
elif x == thislist3:
    print(king(y))
else: 
    print("You didn't choose a restaurant")
    

    