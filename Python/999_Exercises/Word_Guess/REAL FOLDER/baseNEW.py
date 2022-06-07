import random 
word_list = []
with open('allow_words.txt') as f:
    for line in f:
        l = line.strip()
        word_list.append(l)

num=random.randrange(0,12972)
answer=word_list[num]

a=0
for i in range(0,6):
    guess=input("Guess a word! ")
    if guess == answer: 
        print("You won!!!")
        a=1
        break
    else: 
        print("Guess again!") 

if a==0: 
    print("You lose! The answer was" + answer)


f.close()


a=int(input("Please enter a size: "))
b=int(input("Please enter a minimum value: "))
c=int(input("Please enter a maximum value: ")) 
x=random.randint(b,c,a)
print(x) 
g=x.min()
h=x.max()
total = 0
for i in x:
   total = total + i
total = total / len(x)
print("Maximum:")
print(g)
print("Minimum:")
print(h)
print("Average:")
print(total)
      
