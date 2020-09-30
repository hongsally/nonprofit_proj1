def displayIntro():
    print("Welcome. This are a list of non profit you can donate to!")
  #put an Introduction message to the users


def displayNonProfits():
    print(" 1. World Central Kitchen")
    print(" 2. Crisis Text Line")
    print("3. Heart to Heart International")
    wck = 0
    ctl = 0
    hth = 0
  #print all the non-profits to the screen numerically. For Example:
#    1. World Central Kitchen
#    2. Crisis Text Line
#    3. Heart to Heart International
 
def main():
	displayIntro()

	#steps: 
	#1. welcome the user using a unique Intro Message (use a function for this)
	#2. create a variable for each nonprofit/charity that keeps track of how much total money has been donated
	#3. display all the non-profits to the user and ask which one they would like to donate to 
	#4. then ask the user how much money they would like to donate to that specific charity chosen in step 3
	#5. update the variable created in step 2 with whatever amount the user wanted to donated
			#for example: missionbit = 0 -> user wants to donate 100 so you would add 100 to missionbit. missionbit is now 100
	#6. now display all the nonprofits with their new total amounts donated
	#7. repeat this process until the user wants to stop donating (only do this if you cover while loops)
	#push to github after every single step
main()