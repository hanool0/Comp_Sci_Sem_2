mynumbers=[6,9,32,28,15,22,3,18] 
mini = mynumbers[0]
for  i in mynumbers:
    if mini > i:
        mini = i 
maxi= mynumbers[0] 
for i in mynumbers:
    if maxi < i:
        maxi = i
total = 0
for i in mynumbers:
   total = total + i
total = total / len(mynumbers)

print(mini)
print(maxi)
print(total)
