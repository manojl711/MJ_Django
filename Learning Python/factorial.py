# Recursion example

def fact(number):
    if number == 1:
        return 1
    return number * fact(number - 1)


n = int(input('Enter a number less than 10 : '))
factorial = fact(n)
print('Factorial of ', str(n), ' = ', str(factorial))
