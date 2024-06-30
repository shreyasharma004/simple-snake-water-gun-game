import random

def check(comp, user):
  if comp == user:
    return 0
    
  if comp == 0 and user == 1:
    return -1
    
  if comp == 1 and user == 2:
    return -1
    
  if comp == 2 and user == 0:
    return -1

  return 1
    
  
comp = random.randint(0, 2)
user = int(input("Enter your choice: 0 for Snake, 1 for Water, and 2 for Gun:\n"))

score = check(comp, user)

print("Your choice: ", user)
print("Computer's choice: ", comp)

if score == 0:
  print("It's a tie")
elif score == -1:
  print("Sorry, you lose")
else:
  print("Congratulations, you have won!")
  