def happy_numbers(number):
    squared_sum = 0
    count = 0
    orginal_number = number
    while number > 0:
        for digit in str(number):
            digit_squared = pow(int(digit), 2)
            if count < len(str(number))-1:
                 squared_sum += digit_squared
                 count += 1
            elif count == len(str(number))-1:
                 if squared_sum == 1:
                     print(f"{orginal_number} is a happy number")
                     number = 0
                 elif squared_sum == 4:
                     print(f"{orginal_number} is a sad number")
                     number = 0
                 else:
                     number = squared_sum + digit_squared
                     squared_sum = 0
                     count = 0

happy_numbers(int(input("Enter a number to see if it is happy. ")))

def prime_numbers(number):
    if number % 2 != 0 and number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        print(f"{number} is prime.")
    else:
        print(f"{number} is not prime.")

prime_numbers(int(input("Enter a number to see if it is prime. ")))

def fibonacci(starting_position, ending_position):
    list = []
    for position in range(starting_position, ending_position, 1):
        value = (pow((1 + pow(5, .5)) / 2, position) - pow((1 - pow(5, .5)) / 2, position)) / pow(5, .5)
        value = int(value)
        list.append(value)
    print(list)
 
fibonacci(int(input("Enter the n starting position of where to start the Fibonacci sequence. ")), int(input("Enter the n ending position of where to start the Fibonacci sequence. ")))