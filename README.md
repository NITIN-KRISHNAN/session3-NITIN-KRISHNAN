# Numeric types

This assignment mainly contains code to 

- encode a decimal number to any base with the supplied digit map
- equality test for float number
- truncation with out using math library functions or int constructor
- rounding with out using round functions

## encoded_from_base10

This function returns a string encoding in the "base" for the the "number" using the "digit_map"

Conditions that this function must satisfy:

- 2 <= base <= 36 else raise ValueError
- invalid base ValueError must have relevant information
- digit_map must have sufficient length to represent the base, else throw error
- must return proper encoding for all base ranges between 2 to 36 (including)
- must return proper encoding for all negative "numbers" (hint: this is equal to encoding for +ve number, but with - sign added)
- the digit_map must not have any repeated character, else ValueError
- the repeating character ValueError message must be relevant
- you cannot use any in-built functions in the MATH module

## math.isclose()

Whether or not two values are considered close is determined according to given absolute and relative tolerances. This function is used for floating point equality.

This is the formula for calculation of tolerance
tot = max(rel_tol * max(abs(a), abs(b)), abs_tol)

If the difference of the numbers is less than or equal to the tolerance, then the two floating number are considered as equals.

Whether or not two values are considered close is determined according to given absolute and relative tolerances.

rel_tol is the relative tolerance – it is the maximum allowed difference between a and b, relative to the larger absolute value of a or b. For example, to set a tolerance of 5%, pass rel_tol=0.05. The default tolerance is 1e-09, which assures that the two values are the same within about 9 decimal digits. rel_tol must be greater than zero.

abs_tol is the minimum absolute tolerance – useful for comparisons near zero. abs_tol must be at least zero.

If no errors occur, the result will be: abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol).

The IEEE 754 special values of NaN, inf, and -inf will be handled according to IEEE rules. Specifically, NaN is not considered close to any other value, including NaN. inf and -inf are only considered close to themselves.

## math.trunc(*x*)

Performs truncation operation to return the Real value *x* truncated to an Integral (usually an integer).

## bin()

Convert an integer number to a binary string prefixed with “0b”. The result is a valid Python expression. If x is not a Python int object, it has to define an \__index__() method that returns an integer. Some examples:

bin(3)

'0b11'

bin(-10)

'-0b1010'

## hex()

Convert an integer number to a lowercase hexadecimal string prefixed with “0x”. If x is not a Python int object, it has to define an \__index__() method that returns an integer.

## round

Return number rounded to ndigits precision after the decimal point. If ndigits is omitted or is None, it returns the nearest integer to its input.

### Round half to even (Banker's Rounding)

A tie-breaking rule without positive/negative bias and without bias toward/away from zero is round half to even.

### Round half away from zero

The other tie-breaking method commonly taught and used is the round half away from zero (or round half towards infinity), namely: If the fraction of x is exactly 0.5, then y = x + 0.5 if x is positive, and y = x - 0.5 if x is negative.
