
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


def pit_stop_optimizer():
    print("🏁 Welcome to the Pit Stop Timing Optimizer! 🔧\n")
    
    # Get race information from user
    total_race_time = float(input("Enter the total race time in seconds: "))
    num_pit_stops = int(input("How many pit stops were made? "))
    avg_pit_duration = float(input("Enter the average pit stop duration in seconds: "))
    
    # Calculate total pit stop time
    total_pit_time = num_pit_stops * avg_pit_duration
    
    # Calculate percentage of race spent in pits
    pit_percentage = (total_pit_time / total_race_time) * 100
    pit_percentage = round(pit_percentage, 2)
    
    # Display results
    print(f"\n📊 Pit Stop Analysis Results:")
    print(f"Total pit stop time: {total_pit_time} seconds")
    print(f"Percentage of race time spent in pits: {pit_percentage}%")
    
    # Check if pit time is too high
    if pit_percentage > 5:
        print("You need a new pit crew. 🛠️")

if __name__ == "__main__":
    pit_stop_optimizer()