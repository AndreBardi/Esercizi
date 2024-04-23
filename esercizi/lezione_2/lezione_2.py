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

"""
2-5. Famous Quote: Find a quote from a famous person you admire. 
Print the quote and the name of its author. Your output should look something like the following, including the quotation marks:
Albert Einstein once said, “A person who never made a mistake never tried anything new.”

"""

#Questa variabile mostra una citazione

quote: str = "Faccio sempre ciò che non so fare, per imparare come va fatto."
name: str = "Vincent Van Gogh"
message: str = f"{name} una vota disse:\"{quote}\""

print(message)

"""
2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person. 
Then compose your message and represent it with a new variable called message. Print your message. 
"""
#Questa variabile ha cambiato nome ma non funzione

famous_name: str = name
print(message)

"""
2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). 
Assign the value 'python_notes.txt' to a variable called filename. 
Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.
"""

#Questa variabile rimuove un suffisso

filename: str = 'python_notes.txt'

newfilename = filename.removesuffix('.txt')
print(newfilename)

"""
3-1. Names: Store the names of a few of your friends in a list called names. 
Print each person’s name by accessing each element in the list, one at a time.
"""

friends_name: list = ["Mario", "Giovanni", "Sara"]

print(friends_name[0], friends_name[1], friends_name[2])

"""
3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. 
The text of each message should be the same, but each message should be personalized with the person’s name.
"""

message_1: str = f"Ciao {friends_name[0]}, fammi sapere per la cena di domani!"
message_2: str = f"Ciao {friends_name[1]}, fammi sapere per la cena di domani"
message_3: str = f"Ciao {friends_name[2]}, fammi sapere per la cena di domani"

print(message_1)
print(message_2)
print(message_3)

"""
3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. 
Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”
"""