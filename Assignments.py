# 1. Build a grading system, using grades A-F
# 0 - 39 is F
# 40 - 44 is E
# 45 - 49 is D
# 50 - 59 is C
# 60 - 69 is B
# 70 - 100 is A
# less than 0 and greater than 100 is invalid

# Solution
# Grades = int(input('What did you score?:'))
# if Grades >=70 and Grades <=100:
#   print('A')
# elif Grades >=60 and Grades <=69:
#   print ('B')
# elif Grades >=50 and Grades <=59:
#   print ('C')
# elif Grades >=45 and Grades <=49:
#   print ('D')
# elif Grades >=40 and Grades <=44:
#   print ('E')
# elif Grades >0 and Grades <=30:
#   print('F')
# else:
#   print('INVALID')

# Assignment: Do the exact plan for mtn and see the outcome follow it step by step 
# Solution to Assignment

# User = input('USSD code:')
# if User == '*312#':
#   print ('''Welcome to MTN
#   Press 1. Data Plans
#         2. Get 1.2GB for #500
#         3. Social Bundles
#         4. Business Plan
#         5. XtraValue
#         0. Back to Main Menu
#   ''')

#   User_Input = input('Enter your choice:')
#   if User_Input == '1':
#     print ('''
#     a. Daily
#     b. weekly
#     c. Monthly
#     d. 2-3 month
#     ''')

#   elif User_Input == '2':
#     print('''
#     Double your Data! Enjoy 600MB + Extra 600MB for #500 only
#     a. Activate
#     0. Back 
#     ''')

#   elif User_Input == '3':
#    print ('''Choose your bundle
#    a. Whatsapp
#    b. Facebook
#    c. Instagram
#    d. Tiktok
#    e. Ayoba
#    ''') 

#   elif User_Input == '#':
#     print('Return back to Main Menu')
# else:
#   print('Invalid Code')  


# ASSIGNENT 3


# bottles_of_beer_on_the_wall = 99
# while bottles_of_beer_on_the_wall >0:
#  bottles_of_beer_on_the_wall -=1
#  print(f'99 bottles of beer on the wall, 99 bottles of beer. Take one down and pass it around, {bottles_of_beer_on_the_wall} bottles of beer')
# else:
#  print('No bottles of beet left')

# ASSIGNMENT 4
#Build a bank application

# import random
# class Bank:
#    def __init__ (self):
#       self.Bank_name = 'GTBANK'
#       self.balance = 0
#       self.account_number = random.randint(1000000000,9999999999)

#    def landing_page(self):
#       print (f'Welcome to {self.Bank_name}, your account balance is {self.balance}')
#       print('''
#     1. Login
#     2. Signup
#     3. Buy_Airtime
#     4. Buy_Data
#     #. Exit
#       ''')

#       choice = input ('Enter your choice:')

#       if choice == '1':
#          print('Login')
#          self.Login()
      
#       elif choice == '2':
        
#          print('Signup')
#          self.Signup()

#       elif choice == '3': 
         
#          print('Buy_Airtime')
#          self.Buy_Airtime()

#       elif choice == '4':
         
#          print('Buy_Data')
#          self.Buy_Data()

#       elif choice == '#':
#          print('Thanks for your patronage')
#          return
#       else:
#          print('Invalid USSD')

#    def Login(self):
#     print(f'welcome to {self.Bank_name}, your account number is {self.account_number}')
#     self.landing_page()

#    def Signup(self):
#       print('please fill in your details') 
#       print('''
#         1. Full Name
#         2. Email Address
#         3. Password
#            ''')
      
#       Signup_choice = input('Enter your choice:')
#       if Signup_choice == '1':
#        name = input('Enter your name:')
#        print(f'{name} has been saved!')

#       elif Signup_choice == '2':
#        email = input('Enter your email:')
#        print(f'{email} has ben saved!')

#       elif Signup_choice == '3':
#        password = input('Enter your password:')
#        print(f'{password} has been saved!')

#       else:
#        print('Wrong Input, try again')
#        self.landing_page()
   
#    def Buy_Airtime(self):  
#       print('Enter your account number')
#       self.landing_page()

#    def Buy_Data(self):
#       print('How much data?')
#       self.landing_page()
   
bank = Bank()
bank.landing_page()
         

# ASSIGNMENT: Learn how to use and incorporate into the bank app
# 1. SELECT Query
# 2. UPDATE Query
# 3. DELETE Query
# 4. DROP Query
