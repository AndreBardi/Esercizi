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

