
# 1
# print('Welcome to Python 101!')
# print('Welcome to Python 1012!')
# print('Create Hammer')
# print('Create Nails')
# print('Use Hammer')
# print('Use Hammer and Nails')



# 2 -> Concatenation
# failed_subjects = "6"
# name = 'John'

# print('Dear Mrs Badger')
# print('Your son' + name + ' is failing ' + failed_subjects + ' subjects.')
# print(name  + ' will need to redo ' + failed_subjects +  ' courses.')
# name = 'Eric'
# print(name + ' is doing well in geography.')


# 3 -> Variables
# failed_subjects = 2.45 # Float
# name = 'John' # String
# is_going_to_party = True # Boolean
# a = "it's"
# b = 'it\'s'
# print('Dear Mrs Badger')
# print('Your son' + name + ' is failing ' + failed_subjects + ' subjects.')
# print(name  + ' will need to redo ' + failed_subjects +  ' courses.')
# name = 'Eric'
# print(name + ' is doing well in geography.')

# 4 -> Type
# print(type('hello'))
# print(type(1))
# print(type(1.64))
# print(type(True))

# 5 -> Typecasting
# a = int(1)        # a will be 1
# b = int(2.5)      # b will be 2
# c = int("3")      # c will be 3
# c1 = int(float("3.4"))   # c1 will be...
# d = float(1)      # d will be 1.0
# e = float(2.5)    # e will be 2.5
# f = float("3")    # f will be 3.0
# g = float("4.23") # g will be 4.23
# h = str("80s")    # h will be '80s'
# i = str(22)       # i will be '22'
# j = str(3.01)     # j will be '3.01'

# print([a,b,c,d,e,f,g,h,i,j]) 

# 6 -> Exercise

# item_name = "Hammer"
# item_price = 10.99
# item_quantity = 5
# total_price = item_price * item_quantity

# print("Item Name: " + item_name + "\nItem Price: " + str(item_price) + "\nItem Quantity: " + str(item_quantity) + "\nTotal Price: " +   str(total_price)) 

# 7 -> User Input

# print('User Input')
# name = input('What is your name : ')
# age = input('What is your age : ')
# print('Hello ' + name + '!' + ' You are ' + age + ' years old.') 

# num1 = input('Enter first number: ')
# num2 = input('Enter second number: ')
# answer = float(num1) + float(num2)
# print('The answer is: ' + str(answer))


# 8 -> Exercise -> User Input
# name_input = input('What is your name? : ')
# km_input = input('How many kilometers did you run? ')
# mil_input = float(km_input) * 0.621371
# print('Hello ' + name_input.capitalize())
# print('You ran ' + km_input + ' kilometers, which is equal to ' + str(mil_input) + ' miles.')

# 9 -> Basic Arithmetic Operations
# print('Basic Arithmetic Operations')

# a=6
# b=2
# print('Addition : ', a + b)
# print('Subtraction : ', a - b)
# print('Multiplication : ', a * b)
# print('Division (float) : ', a / b)
# print('Division (floor) : ', a // b)
# print('Modulus : ', a % b)
# print('Exponent : ', a ** b)

# 10 ->String-Basics / Slicing
# msg='welcome to Python 101: Strings'
# print(msg)
# print(msg.upper())
# print(msg.lower())
# print(msg.capitalize())
# print(msg.title())
# print(len(msg))
# print(msg.count('o'))

# Slicing
# msg='welcome to Python 101: Strings'
#     #012345678
# print(msg)
# Slicing
# print(msg[:7])
# print(msg[7:14])
# print(msg[14:])
# print(msg[-4:])

# Exercise -> Slicing 
# msg='welcome to Python 101: Strings'
# msg1=msg[18]+' '+msg[:8]+msg[25:29]+msg[7:11]+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]  
# print(msg1.title())
# print(msg1[::-1].title())


# Find / Replace / String Formatting
# msg = 'Welcome to Python 101: Strings'
# print('Python' not in msg)

# name='TERRY'
# color = 'RED'
# msg = '[' + name + '] loves the color ' + color + '!'
# msg1 = f'[{name}] loves the color {color.lower()}!'
# print(msg)


# 11 -> Exercise -> Pit Stop Optimizer - Exercise
# def pit_stop_optimizer():
#     print("🏁 Welcome to the Pit Stop Timing Optimizer! 🔧\n")
    
#     # Get race information from user
#     total_race_time = float(input("Enter the total race time in seconds: "))
#     num_pit_stops = int(input("How many pit stops were made? "))
#     avg_pit_duration = float(input("Enter the average pit stop duration in seconds: "))
    
#     # Calculate total pit stop time
#     total_pit_time = num_pit_stops * avg_pit_duration
    
#     # Calculate percentage of race spent in pits
#     pit_percentage = (total_pit_time / total_race_time) * 100
#     pit_percentage = round(pit_percentage, 2)
    
#     # Display results
#     print(f"\n📊 Pit Stop Analysis Results:")
#     print(f"Total pit stop time: {total_pit_time} seconds")
#     print(f"Percentage of race time spent in pits: {pit_percentage}%")
    
#     # Check if pit time is too high
#     if pit_percentage > 5:
#         print("You need a new pit crew. 🛠️")

# if __name__ == "__main__":
#     pit_stop_optimizer()

# Lists
# friends = ['John', 'Eric', 'Terry', 'Graham', 'Michael']
# print(friends[1])
# cars = [911,1300, 1350, 1400, 1450]
# friends.sort()
# print(friends)
# friends.sort(reverse=True)
# print(friends)
# print(friends)

# print(min(cars))
# print(max(cars))
# print(sum(cars))

# friends.append('TerryG')
# friends.insert(2, 'TerryG')
# print(friends)
# friends.pop(2)
# friends.remove('TerryG')
# friends.clear()
# print(friends)

# del friends[2]

# Coppy List
# new_friends = friends[:]
# print(new_friends)
# print(friends)


# List -> Exercise
# week1 = [15, 22, 18, 25, 20, 12, 17]
# week2 = [13, 19, 24, 16, 21]

# new_day = float(input("Enter the number of lemonades sold on the additional day: "))
# week2.append(new_day)

# sales = week1 + week2

# profits = [day * 1.5 for day in sales]

# best_day = max(profits)
# worst_day = min(profits)
# total_profit = sum(profits)

# print(f"You earned ${best_day:.2f} on your best day.")
# print(f"You earned ${worst_day:.2f} on your worst day.")
# print(f"Your total earnings over two weeks were ${total_profit:.2f}.")

# Split And Join
# msg ='Welcome to Python 101: Split and Join'
# csv = 'Eric,John,Michael,Terry,Graham'
# friends_list = ['Eric','John','Michael','Terry','Graham']
# print(msg.split())
# print(msg.split(','),type(msg.split(' ')))
# print(csv.split(','))

# print(str(friends_list))
# print('-'.join(friends_list))
# print(''.join(friends_list))
# print(''.join(msg.split()))

# Exercise -> Split And Join

# friends_string = "Ali, Ayşe, Mehmet, Zeynep, Can"
# friends_list = []

# split_names = friends_string.split(",")  

# for name in split_names:
#     clean_name = name.strip()  
#     friends_list.append(clean_name)
#     print(f"Eklenen: {clean_name}")

# print("Sonuç listesi:", friends_list)

#Tuples - faster Lists you can't change
# friends = ['John','Michael','Terry','Eric','Graham']
# friends_tuple = ('John','Michael','Terry','Eric','Graham')
# friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
# my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}

# print(friends[2:4])
# print(friends_tuple[2:4])

# print(friends_tuple)
# print(friends)
# print(friends_set)
# print(friends_set.intersection(my_friends_set))
# print(friends_set.difference(my_friends_set))
# print(friends_set.union(my_friends_set))


#Sets - blazingly fast unordered Lists 
# Empty Lists
# empty_list = []
# empyt_list = list()

#Empty Tuple
# empty_tuple = ()
# empty_tuple = tuple()

#Empty Set
# empty_set = {} # this is wrong, this is a dictionary
# empty_set = set()

# friends = {'John','Michael','Terry','Eric','Graham'}
# my_friends = {'Reg','Loretta','Colin','John','Graham'}
# cars =['900','420','V70','911','996','V90','911','911','S','328','900']

# print('Eric' in friends and 'John' in friends)
# print(friends.union(my_friends)) 
# print(friends & my_friends)  # Intersection -> Scrimba Solution
# print(friends.intersection(my_friends,friends))
# print(friends.difference(my_friends)) 
# print(friends - my_friends)  # Difference -> Scrimba Solution
# print(my_friends.symmetric_difference(friends))
# print(my_friends ^ friends) # Symmetric Difference -> Scrimba Solution

# new_cars = set(cars)
# print(new_cars)


# Comments
# print('This is a comment')  
# This is a comment
# more comments
# Multi-line comment
# '''
# # This is a multi-line comment
# # You can write multiple lines here.  
# # This is useful for documentation or explanations.
# # '''

# name = "Default"
# name = input('Enter your silly name: ')
# print("Thank you " + name + "!")
# print("for applying to")
# print("the Minstry of Silly Walks") 

# Functions
# def greeting(param):
#     print("Hello, " + param +  " welcome to Python 101!")

# greeting("Berk")

# def add_numbers(num1, num2):
#     return num1 + num2

# result = add_numbers(5, 10)
# print("The result of the addition is: " + str(result))


#! Function - Exercise
# 1. Add new print statement - on a new line
#    which says 'We hear you like the color xxx! xxx is a string with color 
# 2. extend the function with another  input parameter 'color', that defaults to 'red'
# 3. Capture the color via an input box as variable:color 
# 4. Change the 'You are xx!' text to say 'you will be xx+1 years old next birthday 
#  adding 1 to the age
# 5. Capitalize first letter of the 'name', and rest are small caps 
# 6. Favorite color should be in lowercase 

# def greeting(name, age=24, color = 'red'):
#     print('Hello '  +  name.capitalize() + ', you will be ' + str(age+1) +' next birthday!')
#     print(f'Hello {name.capitalize()}, you will be {age+1} next birthday!')
#     print(f'We hear you like the color {color.lower()}!')

# name = input('Enter your name: ')
# age = input('Enter your age: ')
# color = input('Enter favorite color: ')
# greeting(name, int(age), color)


#1. Comment your code...and explain what it does
# print("Functions - Named Notation")

# def greeting(name, age=28, color="red"):
# Greets user with “name” from “input box” and “age”, if unavailable, default age is used   
   
#    print(f"Hello {name.capitalize()}, you will be {age+1} next birthday!")
#    print(f"We hear you like the color {color.lower()}!")

# greeting(age=27, name="brian",color="Blue")
# Profile(yob=1995,weight=83.5,height=192,eye_color = "blue")

# Return Statements
# def value_added_tax(amount):
#     tax = amount * 0.25
#     total_amount = amount * 1.25
#     return amount, tax, total_amount

# print(value_added_tax(125)) # 31.25

# 🪐 Mars Mission Planner — Challenge Steps
#
# 1. Write a function to calculate how long it takes
#    to reach Mars at a given speed.
#    - Mars' average distance is 225,000,000 km.
#    - Use the formula: time = distance ÷ speed
#    - Round the result to the nearest hour.
#
# 2. Write another function to figure out the total fuel cost
#    for a mission.
#    - Formula: total cost = distance × fuel usage × price per liter
#
# 3. Test your functions with the provided mission data:
#    - Pathfinder: 40,000 km/h
#    - Perseverance: 75,000 km/h
#    - Starship: 120,000 km/h
#    - Each mission travels 225 million km,
#      burns 0.3 liters/km, and fuel costs $1.80/L.
#
# 4. For each mission, print a report showing:
#    - Mission name
#    - Travel time (hours)
#    - Total fuel cost

# distance = 225000000  # km

# fuel_per_km = 0.3     # liters per km
# fuel_price = 1.8      # dollars per liter

# print("🪐 MARS MISSION REPORTS 🪐\n")

# Mission 1: Pathfinder
# speed1 = 40000
# time1 = distance / speed1
# cost1 = distance * fuel_per_km * fuel_price

# print("🚀 Pathfinder:")
# print(f"   Time: {round(time1)} hours")
# print(f"   Cost: ${cost1:,.0f}")
# print()

# Mission 2: Perseverance  
# speed2 = 75000
# time2 = distance / speed2
# cost2 = distance * fuel_per_km * fuel_price

# print("🚀 Perseverance:")
# print(f"   Time: {round(time2)} hours") 
# print(f"   Cost: ${cost2:,.0f}")
# print()

# Mission 3: Starship
# speed3 = 120000
# time3 = distance / speed3
# cost3 = distance * fuel_per_km * fuel_price

# print("🚀 Starship:")
# print(f"   Time: {round(time3)} hours")
# print(f"   Cost: ${cost3:,.0f}")

# Comparisons and Booleans
# a = 7
# b = 3 
# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)
# print('o in John is ','o' in 'John') #membership
# print('o in John is ','o' not in 'John') #non membership
# print('John is John ','John' is 'John') #identity

# Boolean Operators
# print(a == 7 and b == 3)  # True
# print(a == 7 or b == 3)   # True
# print(not a == 7)         # False

# Boolean Expressions
# is_raining = False
# is_sunny = True
# is_weekend = True

# print(bool('Parrot')) # True
# print(bool(1)) # True
# print(bool(0)) # False
# print(bool([])) # False
# print(bool([1, 2, 3])) # True

# print(42 + True) # 43
# print(42 + False) # 42

# Conditional Statements -> If, Elif, Else

# is_raining = False
# is_cold = True
# print("Good Morning!")
# if is_raining or is_cold:
#     print("Don't forget your umbrella or jacket or both!")
# elif is_raining and not is_cold:
#     print("Don't forget your umbrella!")
# else:
#     print("Umbrella optional!")

# amount = 51
# if amount <= 50:
#     print("You can buy a small item.")
# else:
#     print("Please enter your PIN")


#! If/ELIF/ELSE - Exercise 
# mode = input("Enter math mode (+,-,*,/): ")
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# if mode == '+':
#     print(num1 + num2)
# elif mode == '-':
#     print(num1 - num2)
# elif mode == '*':
#     print(num1 * num2)
# elif mode == '/':
#     if num2 != 0:
#         print(num1 / num2)
#     else:
#         print("Division by zero is not allowed.")
# else:
#     print("Invalid math mode.")

# Scrimba Solution
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f
# mode = input('Enter math operation(+,-,*,/) or f for Celsius to Fahrenheit conversion: ')
# num1 = float(input('Enter first number: '))
# if mode.lower() == 'f':
#     print(f'{num1} Celsius is equivalent to {(num1*9/5)+32 } fahrenheit')
# else:
#     num2 = float(input('Enter second number: '))

#     if mode == '+':
#         print(f'Answer is: {num1 + num2}')
#     elif mode == '-':
#         print(f'Answer is: {num1 - num2}')
#     elif mode == '*':
#         print(f'Answer is: {num1 * num2}')
#     elif mode == '/':
#         print(f'Answer is: {num1 / num2}')
#     else:
#         print('Input error!')


# def num_days(month):

#     if month == 'jan':
#         print('number of days in',month,'is',31)
#     elif month == 'feb':
#         print('number of days in',month,'is',28)
#     elif month == 'mar':
#         print('number of days in',month,'is',31)
#     elif month == 'apr':
#         print('number of days in',month,'is',30)
#     elif month == 'may':
#         print('number of days in',month,'is',31)
#     elif month == 'jun':
#         print('number of days in',month,'is',30)
#     elif month == 'jul':
#         print('number of days in',month,'is',31)
#     elif month == 'aug':
#         print('number of days in',month,'is',31)
#     elif month == 'sep':
#         print('number of days in',month,'is',30)
#     elif month == 'oct':
#         print('number of days in',month,'is',31)
#     elif month == 'nov':
#         print('number of days in',month,'is',30)
#     elif month == 'dec':
#         print('number of days in',month,'is',31)

#! optimize/shorten the code in the function
#! try to reduce the number of conditionals 
# def num_days(month):
#     if month == 'jan' or month == 'mar' or month == 'may' or month == 'jul' or month == 'aug' or month == 'oct' or month == 'dec':
#         print('number of days in',month,'is',31)
#     elif month == 'feb':
#         print('number of days in',month,'is',28)
#     else:
#         print('number of days in',month,'is',30)
        
# num_days('feb')


#! While Loops

# print("1.*Loops are great*")
# print("2.**Loops are great**")
# print("3.***Loops are great***")
# print("4.****Loops are great****")
# print("5.*****Loops are great*****")

# while condition:
#     code
#     iterator

# i=0
# while i < 5:
#     print("Loops are awesome")
#     i=i+1


# i=0
# while i < 5:
#     print(f"{i}."+ "*"*i + "Loops are awesome" + "*"*i)
#     i=i+1 # i += 1 aynı ifade

# While Loop - Exercise

# num = 12
# guess = 0
# guess_limit = 3 
# guess_number = 0

# while guess < guess_limit:
#     guess_number = int(input("Guess the number: "))
#     if guess_number == num:
#         print("Congratulations! You guessed the number.")
#         break
#     else:
#         print("Wrong guess, try again!")
#         guess += 1 
# if guess == guess_limit:
#     print("Sorry, you've used all your guesses. The number was:", num)


# Coffee Shop Order System - Exercise
# total_price = 0.0
# drink_count = 0

# while True:
#     name = input("Customer name (type 'done' to finish): ")

#     if name.lower() == "done":
#         break

#     drink = input("What would you like to order (latte, americano, espresso)? ").lower()

#     if drink == "latte":
#         total_price += 3.50
#         drink_count += 1
#     elif drink == "americano":
#         total_price += 3.00
#         drink_count += 1
#     elif drink == "espresso":
#         total_price += 2.50
#         drink_count += 1
#     else:
#         print("⚠️ Sorry, we don't serve that drink.")
#         continue

# print(f"\nTotal drinks ordered: {drink_count}")
# print(f"Total price: ${total_price:.2f}")

# For Loops and Nesting
# for furgle in 'Norwegian blue':
#     print(furgle)

# for furgle in range(2,8):
#     print(furgle)

# for furgle in range(1,15,3):
#     print(furgle)

# for name in range ['John','Terry','Eric','Michael','George']:
#     print(name)

# friends = ['John','Terry','Eric','Michael','George']
# for friend in friends:
#     print(friend)
 
#! For - Exercise

# names = ['aySE','fAtMa','kUZEy']
# names1 = ['bERk', 'eMİR']

# extra_name1 = input("Enter first additional guest name: ").strip().capitalize()
# extra_name2 = input("Enter second additional guest name: ").strip().capitalize()

# all_names = names + names1 + [extra_name1, extra_name2]

# for name in all_names:
#     capitalized_name = name.capitalize()
#     print(f"{capitalized_name},You are invited to the party on Saturday.\n")


#! Phone Numbe Formatter - Exercise
# phone_input = input("Enter U.S phone number in any format: ").strip()

# for char in ['-','(',')','.']:
#     phone_input = phone_input.replace(char, ' ')

# digits = ''.join(phone_input.split())

# if len(digits) == 10 and digits.isdigit():
#     formatted_number = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
#     print(formatted_number)
# else:
#     print("Please enter exactly 10 digits.")

#! Scrimba Solution

# phone_input = input("Enter a U.S. phone number (any format): ")

# cleaned = phone_input.strip()

# for ch in ["-", "(", ")", "."]:
#     cleaned = cleaned.replace(ch, " ")
    
# parts = cleaned.split()
# digits_only = "".join(parts)

# if len(digits_only) == 10:
#     area = digits_only[0:3]
#     mid = digits_only[3:6]
#     end = digits_only[6:]
#     print(f"Formatted number: ({area}) {mid}-{end}")
# else:
#     print("Error: Please enter exactly 10 digits.")
    
# Enumerate

# print('python101 - Enumerate')
# friends = ['Brian', 'Judith', 'Reg', 'Loretta', 'Colin']
# efriends = [(51,'Brian'), (52,'Judith'), (53,'Reg'), (54,'Loretta'), (55,'Colin')]


# i = 1
# for friend in friends:
#     print(i,friend)
#     i = i + 1 # or i += 1

# for num,friend in enumerate(friends,51):
#     print(num,friend)

# print(type(enumerate(friends)))
# print(list(enumerate(friends)))

# Sort() and Sorted()
# my_list = [1,5,3,7,2]
# my_dict = {'car':4,'dog':2,'add':3,'bee':1}
# my_tuple = ('d','c','e','a','b')
# my_string = 'python'

# print(my_list,'original')
# print(sorted(my_list))
# print(my_list,'new')
# my_list1 =sorted(my_list)
# print(my_list1)
# print(list(reversed(my_list)))
# print(my_list[::-1]) # Reverse the list

# Access Control Scanner 

# revoked_badges = {'R100', 'R200', 'R300', 'X404', 'X505'}

# approved = []
# denied = []

# while True:
#     name = input("\nEnter visitor's name (or 'done' to finish): ").strip()
    
#     if name.lower() == 'done':
#         break
    
#     badge = input(f"Enter {name}'s badge number: ").strip()
    
#     if badge in revoked_badges:
#         denied.append(name)
#         print(f"ACCESS DENIED for {name} (badge {badge})")
#     else:
#         approved.append(name)
#         print(f"ACCESS GRANTED for {name}")

# print("\n=== Access Summary ===")

# # Approved 
# print("\n✅ Approved Visitors:")
# approved_sorted = sorted(approved)
# for visitor in approved_sorted:
#     print(f"- {visitor}")
# print(f"Total: {len(approved_sorted)}")

# # Denied 
# print("\n⛔️ Denied Visitors:")
# denied_sorted = sorted(denied)
# for visitor in denied_sorted:
#     print(f"- {visitor}")
# print(f"Total: {len(denied_sorted)}")


# Loyalty Points Engine
# Purchase history (example data - can be modified)
# purchases = [15.99, 27.50, 8.75, 42.20, 225.95, 120.00]

# def earn_points(price):
#     return int(price) * 3  # 3 points per whole dollar

# def tier_label(points):
#     if points < 100:
#         return "Bronze"
#     elif 100 <= points < 500:
#         return "Silver"
#     else:
#         return "Gold"

# # Calculate total spending and points
# total_spent = sum(purchases)
# total_points = sum(earn_points(price) for price in purchases)
# final_tier = tier_label(total_points)

# # Print loyalty summary
# print("\n=== Loyalty Summary ===")
# print(f"• Total dollars spent: ${total_spent:.2f}")
# print(f"• Total points earned: {total_points}")
# print(f"• Final tier: {final_tier}")

# Dictionaries
# movie = {
#     'title': 'The Godfather',
#     'year': 1972,
#     'cast': ['Marlon Brando', 'Al Pacino', 'James Caan'],
# }
# movie.update({'director': 'Francis Ford Coppola', 'rating': 9.2})
# movie['title'] = 'The Godfather Part II'
# movie['budget'] = 6000000
# print(movie['title'])
# del movie['year']
# print(movie.get('year', 'Year not found'))

# Dict II

# python = {'John':35,'Eric':36,'Michael':35,'Terry':38,'Graham':37,'TerryG':34}
# holy_grail = {'Arthur':40,'Galahad':35,'Lancelot':39,'Knight of NI':40, 'Zoot':17}
# life_of_brian = {'Brian':33,'Reg':35,'Stan/Loretta':32,'Biccus Diccus':45}

# Membership Test

# people = {}
# people1 = {}
# people2 = {}

# people.update(python)
# people.update(holy_grail)
# people.update(life_of_brian)
# print(sorted(people))

# for groups in (python,holy_grail) : people1.update(groups)
# print(sorted(people1))

# people2 = {**python, **holy_grail, **life_of_brian}
# print(sorted(people2))

# Dog Bus Tracker - Exercise

# 1. Start with a bus dictionary holding current passengers.
#    - Each seat number (1, 2, 3, ...) is a key
#    - Each value is another dictionary with each pet's:
#        • name
#        • breed
#        • pickup time
#        • dropoff time
#
# 2. Print a starting roster showing each pet’s seat, name, and pickup time.

# 3. Add one new pet if there’s room on the bus.  
#    - Use MAX_SEATS to limit capacity.  
#    - Dynamically assign the next seat number.  
#    - Print the updated roster showing all pets after pickup.  

# 4. Ask which pet leaves early.  
#    - Remove that pet from the bus.  
#    - Print a message saying they’ve headed home.  

# 5. Print a final roster listing the remaining pets and their dropoff times.  


# Constants
# MAX_SEATS = 5

# # Initial bus passengers
# bus = {
#     1: {"name": "Buddy", "breed": "Golden Retriever", "pickup": "8:00 AM", "dropoff": "4:30 PM"},
#     2: {"name": "Luna", "breed": "Labrador", "pickup": "8:15 AM", "dropoff": "4:45 PM"},
#     3: {"name": "Max", "breed": "Beagle", "pickup": "8:30 AM", "dropoff": "5:00 PM"}
# }

# def print_roster(bus_dict, title="Current Bus Roster"):
#     """Print current passengers in a formatted way"""
#     print(f"\n=== {title} ===")
#     for seat, pet in bus_dict.items():
#         print(f"Seat {seat}: {pet['name']} ({pet['breed']}) - Pickup: {pet['pickup']}")

# # 1. Print starting roster
# print_roster(bus, "Starting Bus Roster")

# # 2. Add new pet if there's room
# if len(bus) < MAX_SEATS:
#     next_seat = max(bus.keys()) + 1 if bus else 1
    
#     print("\nNew pet boarding...")
#     name = input("Enter pet's name: ").strip()
#     breed = input("Enter pet's breed: ").strip()
#     pickup = input("Enter pickup time (e.g., 9:00 AM): ").strip()
#     dropoff = input("Enter dropoff time (e.g., 5:30 PM): ").strip()
    
#     bus[next_seat] = {
#         "name": name,
#         "breed": breed,
#         "pickup": pickup,
#         "dropoff": dropoff
#     }
    
#     print_roster(bus, "Updated Bus Roster After Pickup")
# else:
#     print("\nBus is at full capacity - cannot accept more pets.")

# # 3. Remove a pet
# if bus:
#     print("\nEarly dropoff...")
#     print_roster(bus, "Current Passengers")
#     seat_to_remove = int(input("Enter seat number of pet leaving early: "))
    
#     if seat_to_remove in bus:
#         leaving_pet = bus.pop(seat_to_remove)
#         print(f"\n{leaving_pet['name']} has headed home early!")
#     else:
#         print("Invalid seat number - no pet removed.")

# # 4. Print final roster
# if bus:
#     print("\n=== Final Bus Roster ===")
#     for seat, pet in bus.items():
#         print(f"Seat {seat}: {pet['name']} - Dropoff: {pet['dropoff']}")
# else:
#     print("\nBus is now empty - all pets have been dropped off.")

# Scrimba Solution
# MAX_SEATS = 8

# bus = {
#   1: {"name": "Milo", "breed": "Labrador", "pickup": "8:00 AM", "dropoff": "4:00 PM"},
#   2: {"name": "Otis", "breed": "French Bulldog", "pickup": "8:15 AM", "dropoff": "4:15 PM"},
#   3: {"name": "Willow", "breed": "Border Collie", "pickup": "8:30 AM", "dropoff": "4:30 PM"},
# }

# print("-- Starting roster --")
# for seat, info in bus.items():
#   print(f"Seat {seat}: {info['name']} (pickup {info['pickup']})")

# if len(bus) < MAX_SEATS:
#   seat_num = len(bus) + 1
#   new_pet = {
#     "name": "Sir Barks-a-Lot",
#     "breed": "Corgi Knight",
#     "pickup": "8:45 AM",
#     "dropoff": "4:45 PM",
#   }
#   bus[seat_num] = new_pet
#   print(f"\n👋  {new_pet['name']} boards (seat {seat_num}).")
# else:
#   print("\n🚫  No free seats.")

# print("\n-- Roster after pickup --")
# for seat, info in bus.items():
#   print(f"Seat {seat}: {info['name']}")


# remove_name = input("\nWho goes home early? ").strip().lower()

# seat_to_remove = 0
# for seat, info in bus.items():
#   if info['name'].lower() == remove_name:
#     seat_to_remove = seat
#     break

# if seat_to_remove:
#   gone = bus.pop(seat_to_remove)
#   print(f"\n👋  {gone['name']} (seat {seat_to_remove}) heads home early.")
# else:
#   print(f"\n⚠️  No passenger name '{remove_name}' on the bus.")


# print("\n-- Final roster --")
# for seat, info in bus.items():
#   print(f"Seat {seat}: {info['name']} (drop-off {info['dropoff']})")
