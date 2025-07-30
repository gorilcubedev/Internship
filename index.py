
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

friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']

print('Eric' in friends and 'John' in friends)
print(friends.union(my_friends)) 
print(friends & my_friends)  # Intersection -> Scrimba Solution
print(friends.intersection(my_friends,friends))
print(friends.difference(my_friends)) 
print(friends - my_friends)  # Difference -> Scrimba Solution
print(my_friends.symmetric_difference(friends))
print(my_friends ^ friends) # Symmetric Difference -> Scrimba Solution

new_cars = set(cars)
print(new_cars)