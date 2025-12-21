""" My attempt at pw generator
Looking to create pw of user definded length with user defined class of characters
using lists of keyboard characters. """

# Where do we go now?
# import necessary packages; random, etc.
import secrets
import string

ALPHA_LIST = list(string.ascii_letters)
NUM_LIST = list(string.digits)
SPEC_LIST = ['!', '@', '#', '$', '%', '^', '&', '*', '<', '>', '?', '/']
#    pw.append(secrets.choice(string.digits))
#    pw.append(secrets.choice(string.punctuation))
# establish pw
pw = []
# seek user input fopw parameters
password_length = input('How many characters (8 - 16)?:')
if password_length.isdigit():
    password_length = int(password_length)
else:
    print('Invalid input. Please enter a number.')
char_set_num = input('Use numeric characters (0 - 9)? Y or N:')
char_set_spec = input('Use special characters (!, @, #, $, etc.)? Y or N:')
if char_set_spec == 'y' and char_set_num == 'y':
    char_set = ALPHA_LIST + NUM_LIST + SPEC_LIST
    pw.append(secrets.choice(string.digits))
    pw.append(secrets.choice(string.punctuation))
    password_length = password_length - 2
elif char_set_spec == 'y' and char_set_num == 'n':
    char_set = ALPHA_LIST + SPEC_LIST
    pw.append(secrets.choice(string.punctuation))
    password_length = password_length - 1
elif char_set_spec == 'n' and char_set_num == 'y':
    char_set = ALPHA_LIST + NUM_LIST
    pw.append(secrets.choice(string.digits))
    password_length = password_length - 1
else:
    char_set = ALPHA_LIST

# Create loop to create pw of user desired length
for i in range(password_length):
    char = secrets.choice(char_set)
    pw.append(char)
print("Your password is: " + ''.join(pw) + ", the length is " + str(len(pw)) + " characters.")
# EOF
