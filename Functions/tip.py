# --------------------------------------------------
# Challenge 2 - Tip
# --------------------------------------------------

# Create a function called tip() that has two parameters named total and percentage.

# This function should return the amount you should tip given a total and the percentage you want to tip.

# Write your tip function here:
  
# Uncomment these function calls to test your tip function:
#print(tip(10, 25))
# should print 2.5
#print(tip(0, 100))
# should print 0.0

def tip(total,percentage):
  tip = (total * percentage) / 100
  return tip
  

def main():
    print(tip(10,25))
    print(tip(100,10))

main()
