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














