"""
This file contains the various computations that our client would like to carry out.
A function would be created for each computation followed by a decision tree.
This file would then be imported in the main file(index.py)
"""
#MODULES TO IMPORT

#FUNCTIONS FOR THE VARIOUS COMPUTATIONS

#THE INTEGRAL FUNCTION
def Integral():
    print("\nHi! I am here to help you find the definite integral of quadratic functions")
    lowerBound = float(input("\nPlease enter the lower bound of the integral\n"))
    upperBound = float(input("\nPlease enter the upper bound of the integral as a 'x\u00b3'\n"))

    print("\n**NOTE**\n A quadratic function is of the form (AX^2 + BX + C) where A, B and C are constants\n")
    
    A = float(input("Enter the value for 'A'\n"))
    B = float(input("\nEnter the value for 'B'\n"))
    C = float(input("\nEnter the value for 'C'\n"))

    #ESTABLISHING EQUATIONS TO CALCULATE THE DEFINITE INTEGRAL
    solutionUpper = float((A * (upperBound)**3)/3 + (B * (upperBound)**2)/2 + (C * upperBound))
    solutionLower = float((A * (lowerBound)**3)/3 + (B * (lowerBound)**2)/2 + (C * lowerBound))
    finalSolution = round((solutionUpper - solutionLower), 2)

    print("\nThe definite integral of the quadratic function is: ",finalSolution,"\n")

#THE GRADIENT FUNCTION
def Gradient():
    print("\nHi! I am here to help you find the gradient of the equation of a straight line ")
    print("\nThe equation of a line is of the form (Y = MX + C) Where: \n")
    print("\tY = value on the y-axis \n\tX = value on the x-axis\n\tM = gradient of the line \n\tC = a constant( y-intercept )\n")

    #TAKE THE VALUES OF THE VARIABLES
    Y = float(input("Enter the value for 'Y'\n"))
    X = float(input("\nEnter the value for 'X'\n"))
    C = float(input("\nEnter the value for 'C'\n"))

    #ESTABLISHING EQUATION TO CALCULATE GRADIENT
    M = round(float((Y - C)/X), 2)

    print("\nThe gradient of the straight line is ", M, "\n")

"""#THE LOGARITHM FUNCTION
def Logarithm():
    print("\nHi! I am here to help you find the logarithm of numbers\n")
    print("To compute logarithms, you need to identify the base of the logarithm\nLearn more about logarithms from ")

    #TAKE THE VALUES OF THE BASE AND THE NUMBER TO PERFORM THE ALGORITHMIC OPERATION ON
    base = float(input("\nEnter the base of the logarithm\n"))
    number = float(input("\nEnter the number to compute its logarithm\n"))

    #FINDING THE VALUE OF THE COMPUTATION
    print("COMPUTATION UNDER CONSTRUCTION")
"""