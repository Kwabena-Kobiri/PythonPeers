"""
This is the file that contains the function for converting the temperatures from
Degree celsius to Fahrenheit as the client requested. It will be exported into 
the main file(index.py)
"""
def TemperatureConverter():
    # Celsius to Fahrenheit
    # Print out the purpose of this program
    print("\n******Hi! I am here to help you convert temperatures in Degree Celsius to Fahrenheit******")

    #Take the Celsius Temperature as input from the user 
    celsius = float(input("\nPlease enter the Celsius temperature: ")) #stored as float to allow computations on it

    #Calculate the Fahrenheit equivalent using the Celsius to Fahrenheit formula
    fahrenheit = (celsius * 9/5) + 32

    #Round the value to two decimal places and store it in a different variable
    newFahrenheit = round(fahrenheit, 2)

    #Print out the Celsius equivalent of the user input. String casting(str) is done to allow concatenation.
    print("\nThe temperature is: " + str(newFahrenheit) + " Fahrenheit\n")
