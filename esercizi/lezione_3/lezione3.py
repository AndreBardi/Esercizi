"""
4-1. Pizzas: Think of at least three kinds of your favorite pizza. 
Store these pizza names in a list, and then use a for loop to print the name of each pizza.
• Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. 
For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
• Add a line at the end of your program, outside the for loop, that states how much you like pizza. 
The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!
"""
pizzas: list = ["Margherita", "Pepperoni", "Vegetarian"]

for i in pizzas:
    print(i)
print("---------------------------------------")
for i in pizzas:
    print(f"My favourite pizza is the {pizzas[0]}")
    print(f"I like the {pizzas[1]} pizza")
    print(f"I never tried the {pizzas[2]} pizza")
    break
print("---------------------------------------")
print("I really love pizza!!")
print("---------------------------------------")

"""
4-2. Animals: Think of at least three different animals that have a common characteristic. 
Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
• Modify your program to print a statement about each animal, such as A dog would make a great pet.
• Add a line at the end of your program, stating what these animals have in common. You could print a sentence, 
 such as Any of these animals would make a great pet!
"""
animals: list = ["Cat", "Panther", "Lion", "Tiger"]
print("---------------------------------------")
for i in animals:
    print(i)
print("---------------------------------------")
for i in animals:
    print(f"The {animals[0]} it's a small feline")
    print(f"The {animals[1]} it's a midnight coloured feline")
    print(f"The {animals[2]} it's the King of the felines ")
    print(f"The {animals[3]} it's a sneaky feline")
    break
print("---------------------------------------")
print("I would really like to pet any of these animals!!")
print("---------------------------------------")

"""
4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
"""
for i in range(1, 21):
    print(i)
print("---------------------------------------")    

"""
4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. 
(If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)
"""

#for i in range(1, 10000001):
#    print(i)
print("---------------------------------------")
"""
4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() 
to make sure your list actually starts at one and ends at one million. 
Also, use the sum() function to see how quickly Python can add a million numbers.
"""
one_mil_list: list = [1, 10000001]
x = min(1, 10000001)
y = max(1, 10000001)
z = sum(one_mil_list)
print(x)
print(y)
print(z)
print("---------------------------------------")

"""
4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. 
Use a for loop to print each number.
"""
odd_nums = list(range(1, 21, 2))

for nums in odd_nums:
    print(nums)
print("---------------------------------------")

"""
4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.
"""

num_list: list = list(range(3, 31, 3))
for nums in num_list:
    print(nums)
print("---------------------------------------")

"""
4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. 
Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.
"""
cubes = []

for i in range(1, 11):
    cube = i ** 3
    cubes.append(cube)

for cube in cubes:
    print(cube)
print("---------------------------------------")

"""
4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
"""
count_cubes = [i**3 for i in range(1, 11)]
print(count_cubes)

"""
4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
• Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
• Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.
"""
x = slice(3)
y = slice(3, 6, 1)
z = slice(6, 10, 1)
print("The first three itmes are:", count_cubes[x])
print("The three items from the middle of the list are:", count_cubes[y])
print("The last three items in the list are:", count_cubes[z])
print("---------------------------------------")
"""
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. 
Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. 
Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. 
Make sure each new pizza is stored in the appropriate list.
"""
friends_pizzas = pizzas[:]
pizzas.append("Salami")
friends_pizzas.append("Four Cheeses")
print("My favourite pizzas are", pizzas)
print(f"My friend's favourite pizzas are {friends_pizzas}")
print("---------------------------------------")
"""
4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing, to save space. 
Choose a version of foods.py, and write two for loops to print each list of foods.
"""
print("My pizzas:")
for pizza in pizzas:
    print(pizza)

print("\nFriend's pizzas:")
for pizza in friends_pizzas:
    print(pizza)
print("---------------------------------------")

"""
5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Look closely at your results, and make sure you understand why each line
evaluates to True or False.
• Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False.
"""

city = 'rome'
print("Is city == 'rome'? I predict True.")
print(city == 'rome')
print("\nIs city == 'naples'? I predict False.")
print(city == 'naples')

animal = 'dog'
print("\nIs animal == 'dog'? I predict True.")
print(animal == 'dog')
print("\nIs animal == 'cat'? I predict False.")
print(animal == 'cat')

internet = 'google'
print("\nIs internet == 'google'? I predict True.")
print(internet == 'google')
print("\nIs internet == 'youtube'? I predict False.")
print(internet == 'youtube')

anime = 'one piece'
print("\nIs anime == 'one piece'? I predict True.")
print(anime == 'one piece')
print("\nIs anime == 'HunterxHunter'? I predict False.")
print(anime == 'HunterxHunter')

fast_food = 'kfc'
print("\nIs fast_food == 'kfc'? I predict True.")
print(fast_food == 'kfc')
print("\nIs fast_food == 'McDonalds'? I predict False.")
print(fast_food == 'McDonalds')
print("---------------------------------------")
"""
5-2. More Conditional Tests: You don’t have to limit the number of tests you cre-
ate to 10. If you want to try more comparisons, write more tests and add them
to conditional_tests.py. Have at least one True and one False result for each of the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and less
than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list
"""
h = "apple"
print(h == "apple")
print(h != "orange")
print(h == "kiwi")
print("\n")

f = "Apple"
print(f.lower() == f.lower())
print(f.lower() != "orange".lower())

c = 5
d = 10
print("\n")
print(c == c)
print(c != d)
print(d == c)
print("\n")
print(c < d)
print(d > d)
print(c <= d)

print("\n")
print(5 > 3 and 10 < 20)
print(5 < 3 or 10 > 20)
print("\n")

fruits = ["\napple", "banana", "orange"]
print("banana" in fruits)
print("grape" not in fruits)
print("kiwi" in fruits)
print("---------------------------------------")

"""
5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
• Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
• Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)
"""

alien_color = 'green'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points.")

alien_color = 'red'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points.")
print("---------------------------------------")
"""
5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
• If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
• If the alien’s color isn’t green, print a statement that the player just earned 10 points.
• Write one version of this program that runs the if block and another that runs the else block.
"""

alien_color = 'green'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points for shooting the alien.")
else:
    print("Congratulations! You just earned 10 points.")


other_alien_color = 'red'

if other_alien_color == 'green':
    print("Congratulations! You just earned 5 points for shooting the alien.")
else:
    print("Congratulations! You just earned 10 points.")

print("---------------------------------------")
"""
5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.

• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed for the appropriate color alien.
"""

alien_color = 'green'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points.")
elif alien_color == 'yellow':
    print("Congratulations! You just earned 10 points.")
else:
    print("Congratulations! You just earned 15 points.")


alien_color = 'yellow'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points.")
elif alien_color == 'yellow':
    print("Congratulations! You just earned 10 points.")
else:
    print("Congratulations! You just earned 15 points.")


alien_color = 'red'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points.")
elif alien_color == 'yellow':
    print("Congratulations! You just earned 10 points.")
else:
    print("Congratulations! You just earned 15 points.")
print("---------------------------------------")

"""
5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
• If the person is less than 2 years old, print a message that the person is a baby.
• If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
• If the person is at least 4 years old but less than 13, print a message that the person is a kid.
• If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
• If the person is at least 20 years old but less than 65, print a message that the person is an adult.
• If the person is age 65 or older, print a message that the person is an elder.
"""

age = 25

if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")
print("---------------------------------------")

"""
5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
• Make a list of your three favorite fruits and call it favorite_fruits.
• Write five if statements. Each should check whether a certain kind of fruit is in your list. 
If the fruit is in your list, the if block should print a statement, such as You really like Apples!
"""

favorite_cars = ['Tesla', 'BMW', 'Ferrari']


if 'Tesla' in favorite_cars:
    print("You really like Teslas!")
if 'BMW' in favorite_cars:
    print("You really like BMWs!")
if 'Toyota' in favorite_cars:
    print("You really like Toyotas!")
if 'Ferrari' in favorite_cars:
    print("You really like Ferraris!")
if 'Honda' in favorite_cars:
    print("You really like Hondas!")
print("---------------------------------------")

"""
5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user.
• If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.
"""

users = ['admin', 'jaden', 'emma', 'alex', 'sophia', 'mike']


for user in users:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")
print("---------------------------------------")

"""
5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct message is printed.
"""

users = ['admin', 'jaden', 'emma', 'alex', 'sophia', 'mike']

if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")


users.clear()

if not users:
    print("We need to find some users!")
print("---------------------------------------")

"""
5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
• Make a list of five or more usernames called current_users.
• Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
• Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. 
If a username has not been used, print a message saying that the username is available.
• Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. 
(To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)
"""

current_users = ['joshua', 'emma', 'andrew', 'sophia', 'james']

new_users = ['Jaden', 'emma', 'Andre', 'sophie', 'james']


current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    
    user_lower = user.lower()
    
    if user_lower in current_users_lower:
        print(f"Sorry, the username '{user}' is already taken. Please enter a new username.")
    else:
        print(f"The username '{user}' is available.")
print("---------------------------------------")
"""
5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
• Store the numbers 1 through 9 in a list.
• Loop through the list.
• Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. 
Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.
"""

numbers = list(range(1, 10))


for number in numbers:
   
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
print("---------------------------------------")