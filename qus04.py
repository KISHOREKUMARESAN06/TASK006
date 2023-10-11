def sum_of_first_and_last_digit(number):
    num_str = str(number)
        if num_str.isdigit():
        first_digit = int(num_str[0])
        last_digit = int(num_str[-1])
        
        return first_digit + last_digit
    else:
        return "Invalid input. Please enter a valid integer."

try:
    num = int(input("Enter an integer: "))
    result = sum_of_first_and_last_digit(num)
    print("Sum of the first and last digit:", result)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
