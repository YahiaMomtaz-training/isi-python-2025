# create 4 functions
"""
1. add_numbers : which add 2 parameters and return result
2. multiply_numbers : which multiply 3 parameters and return result
3. divide_numbers : which divide 2 parameters and return result and check not to divide by Zero
4. abs_numbers : which take 1 parameter : if it is negative just return +ive of this number
"""
def add_numbers(first_number, second_number = 0):
    """
    This function is used to add 2 values and return the result
    :param first_number: It is the first number
    :param second_number: It is the second number
    :return: return int value the result of addition
    """
    return first_number + second_number

def multiply_numbers(first_number, second_number, third_number):
    return first_number * second_number * third_number
def abs_number(value):
    if value < 0:
        return value * (-1)
    else:
        return value
def divide_numbers(first_number, second_number):
    if second_number == 0:
        return 'Error - Cannot divide by Zero'
    else:
        return first_number / second_number

############################################
print('test')
add_result = add_numbers(7, 8)
multiply_result = multiply_numbers(9, 6, 3)
abs_result = abs_number(20)
divide_result = divide_numbers(8, 0)
# divide_result = divide_numbers(second_number=2, first_number=10) # 10/2
print(add_result, multiply_result, abs_result, divide_result)



res = add_numbers(6, 7)
print(res)

print('ahmed', 'omar', 'marwa', 'aly', 'mostafa')



