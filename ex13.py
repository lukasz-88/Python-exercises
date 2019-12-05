"""
Exercise 13: Fibonacci
Write a program that asks the user how many Fibonnaci numbers
to generate and then generates them. Take this opportunity to
think about how you can use functions. Make sure to ask the user to
enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the
 next number in the sequence is the sum of the previous two
 numbers in the sequence. The sequence looks like this:
 1, 1, 2, 3, 5, 8, 13, …)
"""

def Fibonacci(number: int):
    if number == 1:
        print("Fibonacci sequence for your number ({}) is: {}".format(number, [1]))
    else:
        num1, num2 = 0, 1
        Fib_seq = [num2]
        i = 1
        while i < number:
            Fib_seq.append(num1 + num2)
            i += 1
            num3 = num1 + num2
            num1 = num2
            num2 = num3
        print("Fibonacci sequence for your number ({}) is: {}".format(number, Fib_seq))

Fibonacci(8)
