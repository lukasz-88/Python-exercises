"""
Exercise 11: Check Primality Functions
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that
has no divisors.). You can (and should!) use your answer to Exercise 4
to help you. Take this opportunity to practice using functions, described below.
"""


def prime_number(number):
    divisors_list = [counter for counter in range(1, (user_number/2) + 1)
                     if user_number % counter == 0]
    if len(divisors_list) == 2:
        print("Your number is prime")
    else:
        print("Your number is not prime.\nThe list of divisors: {}".format(divisors_list))


while True:
    try:
        user_number = int(input("Enter the number: "))
        prime_number(user_number)
    except ValueError:
        print("Incorrect value. Please enter the number.")
        continue
    else:
        break
