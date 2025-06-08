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




# ASSIGNMENT 
# Build a bank application

import mysql.connector as sql
mycon = sql.connect(
  host = '127.0.0.1',
  user = 'root',
  password = 'Aramide001',
  database = 'Bank_App'
  )

mycursor= mycon.cursor()
mycon.autocommit = True   #This is to store information into the database without needing for a reocurrence of the .commit

# mycursor.execute('CREATE DATABASE Bank_App')

# mycursor.execute('SHOW DATABASES')
# for db in mycursor:      #db is database
#     print(db)


# mycursor.execute('CREATE TABLE customer_info(id INT(4) PRIMARY KEY AUTO_INCREMENT, fullname VARCHAR(30), email VARCHAR(30) UNIQUE, password VARCHAR(10), acct_no VARCHAR(10)UNIQUE, acct_bal FLOAT(10), date_time DATETIME DEFAULT CURRENT_TIMESTAMP )')


# mycursor.execute('SHOW TABLES')
# for table in mycursor:
#     print('TABLE')   



import random
class Bank:
   def __init__ (self):
      self.Bank_name = 'GTBANK'
      self.balance = 0
      self.account_number = random.randint(1000000000,9999999999)
      self.user_details = {}

   def landing_page(self):
      print (f'Welcome to {self.Bank_name}, your account balance is {self.balance}')
      print('''
    1. Login
    2. Signup
    3. Buy_Airtime
     4. Buy_Data
     #. Exit
       ''')

   #    choice = input ('Enter your choice:')

   #    if choice == '1':
   #       print('Login')
   #       self.Login()
      
   #    elif choice == '2':
        
   #       print('Signup')
   #       self.Signup()

   #    elif choice == '3': 
         
   #       print('Buy_Airtime')
   #       self.Buy_Airtime()

   #    elif choice == '4':
         
   #       print('Buy_Data')
   #       self.Buy_Data()

   #    elif choice == '#':
   #       print('Thanks for your patronage')
   #       return
   #    else:
   #       print('Invalid USSD')

   # def Login(self):
   #  print(f'welcome to {self.Bank_name}, your account number is {self.account_number}')
   #  self.landing_page()

   # def Signup(self):
   #    print('please fill in your details') 
   #    fullname = input('Enter your Full name:')
   #    email = input('Enter your email:')
   #    password = input('Enter your password:')
   #    confirm_password = input('Enter your password:')
   #    if confirm_password == password:
   #     print('Correct Password')
   #    else:
   #      print('Wrong Input, try again')

   #    acct_no = random.randint (2100000000, 2199999999)
   #    acct_bal = 0
   
   #    self.account_number = acct_no
   #    self.balance = acct_bal

      # query = 'INSERT into customer_info (fullname, email, password, acct_no, acct_bal) VALUE (%s, %s, %s, %s, %s)'
      # values= (fullname, email, password, acct_no,  acct_bal)

      # mycursor.execute(query, values)
      
      # print('Account Created Succesfully') 
   
   
#    def Buy_Airtime(self):  
#       print('Enter your account number')
#       self.landing_page()

#    def Buy_Data(self):
#       print('How much data?')
#       self.landing_page()
   
# bank = Bank()
# bank.landing_page()
         

def login():
   # print('login')
   email = input('Enter your email:')
   password = input ('Enter your password:') 

   query = 'SELECT * FROM customer_info WHERE email = %s and password = %s'
   values = (email, password)
   mycursor.execute(query, values)
   details = mycursor.fetchone()
   # print(details)
   if details == None:
      print ('details')
   else:
      print('login sucessfully')
      return details
# login()

def deposit():
  print('deposit')
  proceed_to_login = login()
#   print (proceed_to_login)
  current_balance = proceed_to_login[5]
  password = proceed_to_login[3]
#   print(current_balance, password)
  amount = float(input('Amount:'))
  new_bal = current_balance + amount
#   print(new_bal)
  password_inp = input('password:')

  if password_inp == password:
    query = 'UPDATE customer_info SET acct_bal = %s WHERE password = %s'
    values = (new_bal, password) 
    mycursor.execute(query, values)
    print(f'Your new account balance is {new_bal}')
  else:
    print('Invalid password')

deposit()