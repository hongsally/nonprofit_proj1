import random
runprogram = True
while(runprogram):
   user = input("Trash Compost or Recycle: ")
   game = ["trash", "compost", "recylce"]
   ran = random.choice(game)
   print(ran)
   if user == ran:
       print("It is a tie")
    elif user == "trash" and ran == ""
   again = input("Would you like to play again? ")
   if again == "no":
       runprogram = False   