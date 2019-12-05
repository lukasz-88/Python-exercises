'''
Exercise 16: Password Generator
Write a password generator in Python. Be creative with how you generate
passwords - strong passwords have a mix of lowercase letters, uppercase
letters, numbers, and symbols. The passwords should be random,
generating a new password every time the user asks for a new password.
Include your run-time code in a main method.

Extra:
Ask the user how strong they want their password to be.
For weak passwords, pick a word or two from a list.
'''

import random

def password_generator():
    letters_lower = ['a','b', 'c', 'd', 'e', 'f','g','h','i','j','k','l','m','n', \
                  'o','p','q','r','s','t','u','v','w','x','y','z']
    letters_upper = ['A','B', 'C', 'D', 'E', 'F','G','H','I','J','K', \
                  'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    specials = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '/', '_', \
                '.', ',']

    password_len = random.randint(10,20)

    #we would like characters from each group, thus we divide length by 4
    password = random.sample(specials, password_len//4) \
               + random.sample(numbers, password_len//4) \
               + random.sample(letters_upper, password_len//4) \
               + random.sample(letters_lower, password_len - 3 * (password_len//4))

    random.shuffle(password)
    print("Your new password: {}\t(Length: {})".format(''.join(password), password_len))


password_generator()
