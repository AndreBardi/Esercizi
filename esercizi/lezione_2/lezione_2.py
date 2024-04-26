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
car_list: list [str] = ("Toyota", "Jeep", "Nissan")

car1: str = f"I would like to own a {car_list[0]} one day"
car2: str = f"I would like to get on a {car_list[1]} at least once"
car3: str = f"In the future, i would like to drive a {car_list[2]}"

for i in range(len(car_list)):
    print(car1)
    print(car2)
    print(car3)
    break

"""
3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? 
Make a list that includes at least three people you’d like to invite to dinner. 
Then use your list to print a message to each person, inviting them to dinner.
"""

guest_list: str = ["Daniele", "Sandro", "Fernanda", "Alessandra"]
mess1: str = f"Dear {guest_list[0]}, you are invited to my place for a fancy dinner"
mess2: str = f"Dear {guest_list[1]}, you are invited to my place for a fancy dinner"
mess3: str = f"Dear {guest_list[2]}, you are invited to my place for a fancy dinner"
mess4: str = f"Dear {guest_list[3]}, you are invited to my place for a fancy dinner"

for i in range(len(guest_list)):
    print(mess1)
    print(mess2)
    print(mess3)
    print(mess4)
    break

"""
3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. 
  You’ll have to think of someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in your list.
"""

print(f"{guest_list[3]} won't make it to dinner")

guest_list.pop(3)
guest_list.append("Gianluca")

mess5: str = f"Dear {guest_list[3]}, you are invited to my place for a fancy dinner"
for i in range(len(guest_list)):
    print(mess1)
    print(mess2)
    print(mess3)
    print(mess5)
    break

"""
3-6. More Guests: You just found a bigger dinner table, so now more space is available. 
  Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, 
  informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
"""
guest_list.append("Simone")
guest_list.append("Alessandro")
guest_list.append("Annalisa")

discovery: str = f"Dear {guest_list}, for our dinner, i just found a bigger table"
print(discovery)

guest_list.insert(0, "Margherita")
guest_list.insert(4, "Angelo")
guest_list.append("Giovanni")

mess6: str = f"Dear {guest_list[0]}, you are invited to my place for a fancy dinner"
mess7: str = f"Dear {guest_list[4]}, you are invited to my place for a fancy dinner"

for i in range(len(guest_list)):
    print(mess6)
    print(mess1)
    print(mess2)
    print(mess3)
    print(mess4)
    print(mess5)
    print(mess7)
    break

"""
3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. 
  Add a new line that prints a message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list. 
  Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty list. 
  Print your list to make sure you actually have an empty list at the end of your program.
"""
everyone: str = f"Dear {guest_list}, sadly i have to announce that i can only have two guests at my dinner. Sinceere apoogies."
print(everyone)

guest_list.pop(0)
guest_list.pop(2)
guest_list.pop(3)
guest_list.pop(4)
guest_list.pop(5)

print(guest_list)


"""
3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
• Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the actual list.
• Show that your list is still in its original order by printing it.
• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
• Show that your list is still in its original order by printing it again.
• Use reverse()  to change the order of your list. Print the list to show that its order has changed.
• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
• Use sort() to change your list so it’s stored in reverse-alphabetical order.
Print the list to show that its order has changed.
"""

dream_places: list = ["Japan", "Canada", "Finland", "Switzerland", "USA"]
print(dream_places)

sorted(dream_places[1: 5])
print(dream_places)

sorted(dream_places[5: -1])
print(dream_places)

dream_places.reverse()
print(dream_places)

dream_places.reverse()
print(dream_places)

dream_places.sort()
print(dream_places)

dream_places.sort(reverse=True)
print(dream_places)



"""
3-9. Dinner Guests: Working with one of the programs from Exercises 3, use len() 
to print a message indicating the number of people you’re inviting to dinner.
"""

x = len(guest_list)
print("The number of guests is", x)


"""
3-10. Every Function: Think of things you could store in a list. 
For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. 
Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.
"""

food_list = ["pizza", "burger", "sushi", "pasta", "salad", "taco", "sandwich", "steak"]

food1: str = f"What do you want for dinner? {food_list[0]} or {food_list[2]}?"
food2: str = f"I'd like some {food_list[1]}, but i'm craving for some {food_list[3]}!!"
food3: str = f"What should i bring for lunch at work, a {food_list[5]} or a {food_list[6]}?"
food4: str = f"For lunch, I'll cook some {food_list[7]} with a side dish of {food_list[4]}"

for i in range(len(food_list)):
    print(food1)
    print(food2)
    print(food3)
    print(food4)
    break


food_list.pop(4)
food_list.insert(4, "fries")
food5: str = f"For lunch, I'll cook some {food_list[7]} with a side dish of {food_list[4]}"

print(food_list)

for i in range(len(food_list)):
    print(food5)
    break


"""
6-1. Person: Use a dictionary to store information about a person you know. 
Store their first name, last name, age, and the city in which they live. 
You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.
"""

profile =	{
  "first_name": "Marco",
  "last_name": "De Stefano",
  "age": 19,
  "city": "Rome"

}

for x in profile:
    print(profile[x])


"""
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. 
  Think of five names, and use them as keys in your dictionary. 
  Think of a favorite number for each person, and store each as a value in your dictionary. 
  Print each person’s name and their favorite number. 
For even more fun, poll a few friends and get some actual data for your program.
"""


profile1 =	{
  "name": "Marco",
  "fav_number": 69
}

profile2 =	{
  "name": "Giovanni",
  "fav_number": 42
}

profile3 =	{
  "name": "Manuel",
  "fav_number": 33
}

profile4 =	{
  "name": "Emauele",
  "fav_number": 90
}

profile5 =	{
  "name": "Elia",
  "fav_number": 29
}



for x in profile1:
    print(profile1[x])

for x in profile2:
    print(profile2[x])

for x in profile3:
    print(profile3[x])

for x in profile4:
    print(profile4[x])
    
for x in profile5:
    print(profile5[x])


"""
6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
• Print each word and its meaning as neatly formatted output. 
You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. 
Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.
"""

glossary_dict: dict = {
    

}