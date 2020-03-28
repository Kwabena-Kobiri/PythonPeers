#Covid-19 Interactive Screen
"""
This is a program to support Nurses in attending to patients whilst observing the 
rules of social distancing in order to prevent the transmission of Covid-19.
"""
#Give patient instruction to enter personal details
print("PLEASE ENTER YOUR HEALTH DETAILS FOR THE NURSES TO ATTEND TO YOU SHORTLY")
firstName = input("First Name: ")
lastName = input("Last Name: ")
age = input("Age: ")
residence = input("Place of residence: ")

#Give patient instruction to enter symptoms
print("PLEASE ENTER THE HEALTH SYMPTOMS THAT BROUGHT YOU TO THE HOSPITAL")
symptoms = input("List your symptoms seperated with a comma(e.g cold, headache): ")

print("THANK YOU, WE WILL ATTEND TO YOU SHORTLY")

#Print the following details on the Nurse's screen
print("PATIENT DETAILS")
print("Name: " + firstName + " " + lastName)
print("Age: " + age)
print("Residence: " + residence)
print("Symptoms: " + symptoms)
