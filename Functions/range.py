
def in_range(num,lower,upper):
    if num >= lower and num <= upper:
        return True
    else:
        return False

def main():
    print(in_range(10,10,10))
main()