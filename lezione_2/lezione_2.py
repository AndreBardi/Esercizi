# Andrea Bardi
# 18/04/2024 a 
# 2-3. Personal Message: Use a variable to represent a person's name,
# and print a message to that person.
# Your message should be simple, such as,
# "Hello Eric, would you like to learn some Python today?"


name: str = "Mario"
message: str = f"Ciao {name}, ti va di imparare un pò di Python insieme?"
print(message)

"""
2-4. Name Cases: Use a variable to represent a person’s name, 
and then print that person’s name in lowercase, uppercase, and title case.
"""

#Questa è una variabile che contiene il nome di una persona
name: str = "Mario"

#Questa variabile contiene il nome minuscolo
name_lower: str = name.lower()

#Questa variabile contiene il nome minuscolo
name_upper: str = name.upper()

print(f"{name}, {name.upper()}, {name.lower()}")