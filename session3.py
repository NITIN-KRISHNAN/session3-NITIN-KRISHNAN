from fractions import Fraction
def encoded_from_base10(number, base, digit_map):
    '''
    This function returns a string encoding in the "base" for the the "number" using the "digit_map"
    Conditions that this function must satisfy:
    - 2 <= base <= 36 else raise ValueError
    - invalid base ValueError must have relevant information
    - digit_map must have sufficient length to represent the base
    - must return proper encoding for all base ranges between 2 to 36 (including)
    - must return proper encoding for all negative "numbers" (hint: this is equal to encoding for +ve number, but with - sign added)
    - the digit_map must not have any repeated character, else ValueError
    - the repeating character ValueError message must be relevant
    - you cannot use any in-built functions in the MATH module

    '''
    if(not isinstance(base, int) or not isinstance(number, int) ):
        raise ValueError("Non integer input is not yet supported ")

    if(not(2 <= base or base >= 36)):
        raise ValueError("Invalid base ")

    digit_map_len = len(digit_map)
    if(base != digit_map_len):
        raise ValueError("Lenght of digmit map should match with base ")

    if (len(frozenset(digit_map)) != digit_map_len):
        raise ValueError(" base contains repeating characters")

    encoded_string = ''
    is_negative_number = False
    if(number < 0):
        number = number * -1;
        is_negative_number = True
    elif(number == 0):
        return 0

    while number != 0:
        rem = number % base
        encoded_char = digit_map[rem]
        encoded_string = encoded_char + encoded_string
        number = number // base

    if (is_negative_number):
        encoded_string = '-' + encoded_string
    return encoded_string


def float_equality_testing(a, b):
    '''
        This function emulates the ISCLOSE method from the MATH module, but you can't use this function
        We are going to assume:
        - rel_tol = 1e-12
        - abs_tol = 1e-05
    '''
    rel_tol = 1e-12
    abs_tol = 1e-05
    tol = max(rel_tol * max(abs(a), abs(b)), abs_tol)
    return (abs(a - b) <= tol)


def manual_truncation_function(f_num):
    '''
    This function emulates python's MATH.TRUNC method. It ignores everything after the decimal point. 
    It must check whether f_num is of correct type before proceed. You can't use inbuilt constructors like int, float, etc
    '''
    if(not isinstance(f_num, float)):
        raise ValueError("Not correct type ")

    result = f_num
    if (f_num < 0):
        result = (f_num // -1) * -1
    else:
        result = f_num // 1
    return result

def manual_rounding_function(f_num):
    '''
    This function emulates python's inbuild ROUND function. You are not allowed to use ROUND function, but
    expected to write your one manually.
    '''
    is_negative_number = False
    if (f_num < 0):
        is_negative_number = True

    abs_num = abs(f_num)
    int_num = manual_truncation_function(abs_num)
    if (abs_num - int_num >= 0.5):
        int_num += 1

    if (is_negative_number):
        int_num = int_num * -1
    return int_num;

def rounding_away_from_zero(f_num):
    '''
    This function implements rounding away from zero as covered in the class
    Desperately need to use INT constructor? Well you can't. 
    Hint: use FRACTIONS and extract numerator. 
    '''
    return 3.0