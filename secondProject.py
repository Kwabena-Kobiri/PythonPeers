#Covid-19 Interactive Screen
"""
This is a program to support Nurses in attending to patients whilst observing the 
rules of social distancing in order to prevent the transmission of Covid-19.
"""
#Give patient instruction to enter personal details
print("\n\tPLEASE ENTER YOUR HEALTH DETAILS FOR THE NURSES TO ATTEND TO YOU SHORTLY")
firstName = input("\nFirst Name: ")
lastName = input("\nLast Name: ")
age = input("\nAge: ")
residence = input("\nPlace of residence: ")

#Give patient instruction to enter symptoms
print("\n\tPLEASE ENTER THE HEALTH SYMPTOMS THAT BROUGHT YOU TO THE HOSPITAL")
symptoms = input("\nList your symptoms seperated with a comma(e.g cold, headache): \n")

print("\n*****THANK YOU, WE WILL ATTEND TO YOU SHORTLY*****\n")

#Print the following details on the Nurse's screen
print("\t\tPATIENT DETAILS\n")
print("Name: " + firstName + " " + lastName)
print("Age: " + age)
print("Residence: " + residence)
print("Symptoms: " + symptoms)
