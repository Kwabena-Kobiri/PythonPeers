# Fahrenheit to Celsius
# Print out the purpose of this program
print("This is a program to help you convert temperatures in Fahrenheit to Degree Celsius")

#Take the Fahrenheit Temperature as input from the user 
fahrenheit = float(input("Please enter the fahrenheit temperature: ")) #stored as float to allow computations on it

#Calculate the Degree Celsius equivalent using the Fahrenheit to Celsius formula
celsius = (fahrenheit - 32) * (5/9)

#Round the value to two decimal places and store it in a different variable
newCelsius = round(celsius, 2)

#Print out the Celsius equivalent of the user input. String casting(str) is done to allow concatenation.
print("The temperature is: " + str(newCelsius) + " Degrees Celsius")
