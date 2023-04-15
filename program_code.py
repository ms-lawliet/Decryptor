# Write a Python Script that will accept a string as encrypted text and then
# the program will decrypt it using the following character substitute:
# 'a' = *, 'e' = & , 'i' = # , 'o' = + 'u' = !

# take in string input from user
str_input = input("Enter encrypted string: ")

# create class for decryption


class Decrypt:
    def __init__(self, user_str):
        self.user_str = user_str

    def decrypt_str(self):
        for letter in range(len(self.user_str)):    # replace each character with respective letter substitute:
            decrypt_a = self.user_str.replace('*', 'a')  # '*' for 'a'
            decrypt_e = decrypt_a.replace('&', 'e')  # '&' for 'e'
            decrypt_i = decrypt_e.replace('#', 'i')  # '#' for 'i'
            decrypt_o = decrypt_i.replace('+', 'o')  # '+' for 'o'
    # '!' for 'u'

    # print decrypted string
        print('Decrypted string:', decrypt_o)


# call function
user_input = Decrypt(str_input)
user_input.decrypt_str()
