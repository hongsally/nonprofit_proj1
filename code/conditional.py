age = 10
if age >= 18:
    print("you are are to watch r rated movies")
elif age >= 13:
    print("You can watch PG13 movies")
elif age >= 10:
    print('You can wach PG movies')
elif age >= 7:
    print("you can watch G rated movies")
else:
    print("You are too tpung to come to our movie theather")

secret_message = "missionbit"
name = input("Enter your name: ")
last_name = input("Enter your last name: ")

if name == "Sally" and last_name == "Hong":
    print("The secret message is", secret_message)

else:
    print("You are not allowed to see the secret message.")