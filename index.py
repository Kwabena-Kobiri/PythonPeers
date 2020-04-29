"""
This is the main file that encapsulates everything about the PERSONAL ASSISTANCE
program. In this file, we ask what the user wants to do and then make function
calls from other files that have to created to solve the problem. This means
that each part of the problem would be solved on a seperate file and then imported
as a module into the main file which is this one.
"""
#LIST OF MODULES TO IMPORT
import TemperatureConverter
import Computations


#LET'S GET STARTED ALREADY
print("\n\t\t******PERSONAL ASSISTANCE******\n\n")
name = input("What is your name please? \n")    #Taking the name of the user to personalize the application for them

print("\nHello **", name, "** I am your Personal Assistance...")
print("What would you want to do today?\n")
print("    PLEASE ENTER ANY OF THE NUMBERS BELOW TO MAKE A CHOICE")
print("\n 1. SCHEDULE TIMETABLE \n 2. SUMMARY NOTES \n 3. TEMPERATURE CONVERTER \n 4. MATHEMATICAL COMPUTATIONS \n 5. GAMES AND FUN\n")
choice = input()

# Decision statements to resolve the various choices

if choice == '1':
    print("\n   PAGE UNDER CONSTRUCTION PLEASE. KINDLY TRY OTHER OPTIONS")
elif choice == '2':
    print("\n   PAGE UNDER CONSTRUCTION PLEASE. KINDLY TRY OTHER OPTIONS")
elif choice == '3':
    TemperatureConverter.TemperatureConverter() #Calling the temperature conversion function
elif choice == '4':
    print("\n***The Computation types available are: ***")
    print("\n1. FINDING THE DEFINITE INTEGRAL OF A QUADRATIC FUNCTION.\n2. FINDING THE GRADIENT OF A STRAIGHT LINE \n3. COMPUTING THE LOGARITHM OF A NUMBER")
    computationType = input("\n\t   WHAT TYPE OF COMPUTATION WOULD YOU LIKE TO PRACTISE?\n")
    if computationType == '1':
        Computations.Integral()    #Calling the integral function
    elif computationType == '2':
        Computations.Gradient()    #Calling the  Gradient function
    elif computationType == '3':
        print("I am good")
        # Computations.Logarithm()
    else:
        print("Please enter any of the digits '1', '2', or '3'")
elif choice == '5':
    print("\n   PAGE UNDER CONSTRUCTION PLEASE. KINDLY TRY OTHER OPTIONS")
else:
    print("\n   Please enter only a digit amongst the provided options")

