"""
This is a program that computes the Collatz Sequence on any given 
positive integer.
"""
#Define the function to compute the collatz sequence
def collatz(number):
        if number % 2 == 0:
            return number // 2
        elif number % 2 == 1:
            return 3 * number + 1
        else:
            print("Please enter a positive integer value")

#Take input from the user
print("\n\t****** THE COLLATZ SEQUENCE ******")
value = int(input("\nPlease enter an integer value: "))

#Output the Sequence
print("\nThe Collatz Sequence for ", value, " is:")

#Condition to loop through the sequence and output all of its figures
while value != 1:
    newvalue = collatz(value)
    print(int(collatz(value)))
    value = newvalue

