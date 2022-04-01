import datetime
import random
import array
 
def password():
 
   print("Input length of password: ")
   pass_len = int(input())
 
   print("Input reason for password: ")
   reason = input()
 
   # check length
   UCASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                       'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                       'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                       'Z']
 
   LCASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                       'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                       'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                       'z']
 
   DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
 
   SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']
 
   # number of different characters
   ucase_amount = random.randint(1, pass_len-3)
   lcase_amount = random.randint(1, pass_len-2-ucase_amount)
   digit_amount = random.randint(1, pass_len-1-ucase_amount-lcase_amount)
   symbols_amount = pass_len - ucase_amount-lcase_amount-digit_amount
 
   temp = ""
   for i in range(ucase_amount):
       temp = temp + random.choice(UCASE)
       temp_list = array.array('u', temp)
       random.shuffle(temp_list)
 
   for i in range(lcase_amount):
       temp = temp + random.choice(LCASE)
       temp_list = array.array('u', temp)
       random.shuffle(temp_list)
 
   for i in range(digit_amount):
       temp = temp + random.choice(DIGITS)
       temp_list = array.array('u', temp)
       random.shuffle(temp_list)
 
   for i in range(symbols_amount):
       temp = temp + random.choice(SYMBOLS)
       temp_list = array.array('u', temp)
       random.shuffle(temp_list)
 
   password = ""
   for x in temp_list:
       password = password + x
      
   date = datetime.datetime.now()
   f= open("secrets.txt","a+")
   f.write(reason +" "+str(date)+" "+password)
   f.close()
 
password()
