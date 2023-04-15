# Write a Python Script that will accept a string as encrypted text and then
# the program will decrypt it using the following character substitute:
# 'a' = *, 'e' = & , 'i' = # , 'o' = + 'u' = !

# take in string input from user
str_input = input("Enter encrypted string: ")

# create class for decryption


class Decrypt:
    def __init__(self, user_str):
        self.user_str = user_str

# replace each character with respective letter substitute:
# '*' for 'a'
# '&' for 'e'
# '#' for 'i'
# '+' for 'o'
# '!' for 'u'
# print decrypted string
