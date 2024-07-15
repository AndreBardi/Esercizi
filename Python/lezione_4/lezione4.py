"""
8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. 
Call the function, and make sure the message displays correctly.
"""
def display_message() -> str:

        print("In this chapter, we are learning about python")

display_message()
print("---------------------------------------")
"""
8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. 
The function should print a message, such as "One of my favorite books is Alice in Wonderland". 
Call the function, making sure to include a book title as an argument in the function call.
"""
def favorite_book() -> str:
        
        title = "Your Name"
        print(f"My favourite book is {title}")

favorite_book()
print("---------------------------------------")

"""
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
The function should print a sentence summarizing the size of the shirt and the message printed on it. 
Call the function once using positional arguments to make a shirt. 
Call the function a second time using keyword arguments.
"""
def make_shirt(size, message):
    print(f"A {size}-sized shirt will be printed with the message: '{message}'")

make_shirt("large", "HellFire Club")
make_shirt("medium", "Joyboy")
print("---------------------------------------")

"""
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
"""
def make_shirt(size="large", message="I love Python"):
    print(f"A {size}-sized shirt will be printed with the message: '{message}'")

make_shirt()
make_shirt("medium", "I love programming")
print("---------------------------------------")

"""
8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. 
The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. 
Call your function for three different cities, at least one of which is not in the default country.
"""
def describe_city(city="Amsterdam", country="Italy"):
      print(f"Rome is located in {country}")
      print(f"Bologna is located in {country}")
      print(f"{city} is located in Netherlands")

describe_city()
print("---------------------------------------")

"""
8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. 
The function should return a string formatted like this: "Santiago, Chile". 
Call your function with at least three city-country pairs, and print the values that are returned.
"""
def city_country(city, country):
    return f"{city}, {country}"

print(city_country("Rome", "Italy"))
print(city_country("Amsterdam", "Netherlands"))
print(city_country("Helsinki", "Finland"))

print("---------------------------------------")
"""
8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. 
The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. 
Use the function to make three dictionaries representing different albums. 
Print each return value to show that the  dictionaries are storing the album information correctly. 
Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. 
If the calling line includes a value for the number of songs, add that value to the album’s dictionary. 
Make at least one new function call that includes the number of songs on an album.
"""
def make_album(artist_name, album_title, number_of_songs=None):
    album = {
        'artist': artist_name,
        'title': album_title
}
    if number_of_songs:
        album['number_of_songs'] = number_of_songs
    return album
album1 = make_album("TheWeeknd", "After Hours")
album2 = make_album("Aurora", "Sky: Concert in the Light", 18)
album3 = make_album("Rihanna", "ANTI", 16)

print(album1)
print(album2)
print(album3)

{'artist': 'TheWeeknd', 'title': 'After Hours'}
{'artist': 'Aurora', 'title': 'ky: Concert in the Light', 'number_of_songs': 18}
{'artist': 'Rihanna', 'title': 'ANTI', 'number_of_songs': 16}
print("---------------------------------------")

"""
8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. 
Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. 
Be sure to include a quit value in the while loop.
"""

"""def make_album(artist_name, album_title, number_of_songs=None):
    album = {
        'artist': artist_name,
        'title': album_title
    }
    if number_of_songs:
        album['number_of_songs'] = number_of_songs
    return album

while True:
    artist = input("Enter the artist's name (or 'quit' to exit): ")
    if artist == 'quit':
        break

    title = input("Enter the album's title (or 'quit' to exit): ")
    if title == 'quit':
        break

    album = make_album(artist, title)
    print(album)"""
print("---------------------------------------")

"""
8-9. Messages: Make a list containing a series of short text messages. 
Pass the list to a function called show_messages(), which prints each text message.
"""
def show_messages(messages):
    for message in messages:
        print(message)

messages = [
     
        "Hello!"
        "\nHow are you?"
        "\nAre you coming to dinner tonight?"
]

show_messages(messages)
print("---------------------------------------")
"""
8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. 
Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. 
After calling the function, print both of your lists to make sure the messages were moved correctly.
"""
messages = ["Hello!", "How are you?", "Are you coming to dinner tonight?"]
sent_messages = []


def send_messages(messages, sent_messages):
 
  while messages:
    message = messages.pop(0)
    print(message)
    sent_messages.append(message)


send_messages(messages.copy(), sent_messages)

print(messages)
print(sent_messages)
print("---------------------------------------")
"""
8-11. Archived Messages: Start with your work from Exercise 8-10. 
Call the function send_messages() with a copy of the list of messages. 
After calling the function, print both of your lists to show that the original list has retained its messages.
"""

messages_copy = messages[:]

sent_messages = []

show_messages(messages)

send_messages(messages_copy, sent_messages)

print("Original messages:", messages)
print("Sent messages:", sent_messages)
print("---------------------------------------")

"""
8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. 
The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered. 
Call the function three times, using a different number of arguments each time.
"""

def make_sandwich(*ingredients):
    
    print("\nMaking a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print("- " + ingredient)

make_sandwich("Ham", "Ketchup", "Lettuce")
make_sandwich("Cheese", "Tomato")
make_sandwich("Peanut Butter", "Jelly")
print("---------------------------------------")
"""
8-13. User Profile:  Build a profile of yourself by calling build_profile(), using your first and last names and 
three other key-value pairs that describe you. 
All the values must be passed to the function as parameters. 
The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"
"""
def build_profile(first_name, last_name, age, hair_color, weight):
    profile = f"{first_name} {last_name}, age {age}, hair {hair_color}, weight {weight}"
    return profile


my_profile = build_profile("Andrea", "Bardi", 20, "brown", 74)

print(my_profile)
print("---------------------------------------")
"""
8-14. Cars: Write a function that stores information about a car in a dictionary. 
The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. 
Call the function with the required information and two other name-value pairs, such as a color or an optional feature. 
Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True) 
Print the dictionary that’s returned to make sure all the information was stored correctly. 
"""
def make_car(producer, model, **car_info):
 
    car = {
        'producer': producer, 
        'model': model
 }
    
    car.update(car_info)
    return car

car = make_car('Toyota', 'Yaris', color='Black', insurance=True)
print(car)
print("---------------------------------------")

"""
8-15. Printing Models: Put the functions for the example printing_models.py in a separate file called printing_functions.py. 
Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.
"""
from lezione4 import city_country

print(city_country("Rome", "Italy"))
print(city_country("Amsterdam", "Netherlands"))
print(city_country("Helsinki", "Finland"))
print("---------------------------------------")

"""
8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. 
Import the function into your main program file, and call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
"""
import mynewfun
print(mynewfun.hello('Giulia'))

from mynewfun import hello
print(hello('Carlos'))

from mynewfun import hello as hello_fn
print(hello_fn('Damian'))

import mynewfun as myfun_fn
print(myfun_fn.hello('Micheal'))

from mynewfun import *
print(hello(f'Jean'))

"""
8-17. Styling Functions: Choose any three programs you wrote for this chapter, 
and make sure they follow the styling guidelines described in this section.
"""

