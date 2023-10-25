import random
u=0
c=0
while True:
   choices = ["rock", "paper", "scissor"]
   comp = random.choice(choices)
   print("Rock, Paper, Scissor!")
   user_choice = input("Type your choice:")
   user = user_choice.lower()
  
   print("Your choice:", user)
   print("Computer's choice:", comp)
   if user==comp:
       print("It's a tie")
   elif comp == "rock":
       if user == "paper":
           print("You Win!")
           u+=1
       else:
           print("You lose!")
           c+=1
   elif comp == "paper":
       if user == "scissor":
           print("You Win!")
           u+=1
       else:
           print("You lose!")
           c+=1
   elif comp == "scissor":
       if user == "rock":
           print("You Win!")
           u+=1
       else:
           print("You lose!")
           c+=1 
   k = input("Want to play again?(yes/no):")
   l=k.lower()
   if l=="no":
      break
print("Your total score: ",u,"\t")
print("Computer's total score: ",c)
if u>c:
    print("CONGRATS! You've won the game!")
elif u<c:
    print("Oopsies... You've lost the game!")
else:
    print("It's a tie")

    

