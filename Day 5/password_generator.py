import random

all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
all_numbers = ['0','1','2','3','4','5','6','7','8','9']
all_symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', 
 ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']


print ("Welcome to the Password Generator")
letters_inp = int(input("How many letters would you like in your password? "))
symbols_inp = int(input("How many symbols would you like in your password? "))
numbers_inp = int(input("How many numbers would you like in your password? "))

password = []
final_password = ""

# for chars in range (0,letters_inp):
#     password += random.choice(all_letters)

# for chars in range (0, numbers_inp):
#     password += random.choice(all_numbers)

# for chars in range (0, symbols_inp):
#     password += random.choice(all_symbols)

for char in range (0, letters_inp):
    password.append(random.choice(all_letters))

for char in range (0, symbols_inp):
    password.append(random.choice(all_symbols))

for char in range (0, numbers_inp):
    password.append(random.choice(all_numbers))

random.shuffle(password)

for char in password:
    final_password += char


print (f"Your password is: {final_password}")
