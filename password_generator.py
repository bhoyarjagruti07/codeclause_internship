import random
import string

length = int(input("Enter Password length\n"))
# pwd should have atleast 1 number, 1 min_length, special characters
#data

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
special = string.punctuation

#Add all data
pwd = lower+upper+digits+special

#use random
new_char = random.sample(pwd,length)   # Genrate new character

password="".join(new_char)   

#Create password
print("Your Password is "+password)

       