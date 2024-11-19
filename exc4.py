# def is_palindrome(word):
#     return word == word[::-1]
#
# # Ζητάμε από τον χρήστη να εισάγει μια λέξη
# user_input = input("Παρακαλώ εισάγετε μια λέξη: ")
#
# # Έλεγχος αν είναι παλίνδρομο
# if is_palindrome(user_uinpt):
#     print(f'Η λέξη "{user_input}" είναι παλίνδρομη.')
# else:
#     print(f'Η λέξη "{user_input}" δεν είναι παλίνδρομη.')



def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

user_input = input("Enter a number to find its Fibonacci value: ")

n = int(user_input)

fib_value = fibonacci(n)

print(f"The Fibonacci value of {n} is {fib_value}.")