# --------------------------------------------------
# Challenge 5 - All Operations
# --------------------------------------------------

# Create a function named lots_of_math(). This function should have four parameters named a, b, c, and d. The function should print 3 lines and return 1 value.

# First, print the sum of a and b.

# Second, print d subtracted from c.

# Third, print the first number printed, multiplied by the second number printed.

# Finally, return the third number printed mod a.

# Write your lots_of_math function here:

# Uncomment these function calls to test your lots_of_math function:
#print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
#print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0

def lots_of_math(a,b,c,d):
    x = a + b
    print(x)
    y = d - c
    print(y)
    n = x * y
    print(n)
    return n % a
    

def main():
    print(lots_of_math(1, 1, 1, 1))
main()