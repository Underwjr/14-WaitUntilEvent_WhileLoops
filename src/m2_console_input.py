"""
This module demonstrates lets you practice INPUT from the CONSOLE.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Jairyq Underwood.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.
import math

def main():
    """ TESTs the functions in this module (by calling them). """
    double_a_float()
    print_an_integer_many_times()
    print_an_integer_many_times_on_one_row()
    input_it_all()


def double_a_float():
    """
    What comes in: Nothing.
    What goes out: Nothing (i.e. None)
    Side effects:
       a. Prompts the user for and inputs a floating point number.
       b. Prints the input number, doubled (i.e., multiplied by 2).
    No input validation is required.  Nothing else should be printed.

    Example:
    Here is a sample run, where the user input is to the right
    of the colon:
         Enter a number: -3.14
         -6.28
    """
    number = float(input('Input number here:'))
    print(str(number) + ' is an interesting number!')
    print('Your number doubled is ' + str(number * 2))

    # -------------------------------------------------------------------------
    # Done 2. Implement and test this function.
    #   The testing code is already written for you (above).
    # -------------------------------------------------------------------------


def print_an_integer_many_times():
    """
    What comes in: Nothing.
    What goes out: Nothing (i.e. None)
    Side effects:
       a. Prompts the user for and inputs a positive integer.
       b. Prints the input integer, doubled (i.e., multiplied by 2),
          the input number of times.  (See the example.)
    No input validation is required.  Nothing else should be printed.

    Example:
    Here are two sample runs, where the user input is to the right
    of the colon:
         Enter an integer: 3
         6
         6
         6

         Enter an integer: 5
         10
         10
         10
         10
         10
    """
    print('')
    print('------------')
    print('Many_times function')
    print('------------')
    number = int(input('Enter an Integer:'))
    for k in range(number):
        print(str(number * 2))
    # -------------------------------------------------------------------------
    # Done 3. Implement and test this function.
    #   The testing code is already written for you (above).
    # -------------------------------------------------------------------------


def print_an_integer_many_times_on_one_row():
    """
    Same as the previous problem, but print the numbers
    on a single line with no spaces in between them.

    Here are two sample runs, where the user input is to the right
    of the colon:
         Enter an integer: 3
         666

         Enter an integer: 5
         1010101010
    """
    print('')
    print('-----------------------------')
    print('Many_times function_one_rows')
    print('-----------------------------')
    number = int(input('Enter an Integer:'))
    print(str(number * 2) * number)
    # -------------------------------------------------------------------------
    # Done: 4. Implement and test this function.
    #   The testing code is already written for you (above).
    #
    # HINT: One way to print on a SINGLE line is to build up a string
    #       and then print that (single) string.
    # -------------------------------------------------------------------------


def input_it_all():
    """
    What comes in: Nothing.
    What goes out: Nothing (i.e. None)
    Side effects:
      Prompts the user for and inputs:
        -- A positive floating point number
        -- A positive integer
        -- A string
      in that order (via three separate INPUT statements).
      Then prints, in this order, all on separate lines:
        a. The square root of the floating point number,
           repeated the input integer number of times.
        b. The string, repeated the input integer number of times.
      No input validation is required.  Nothing else should be printed.

    Example:
    Here is a sample run, where the user input is to the right
    of the colons:
         Enter a positive floating point number: 1.44
         Enter a positive integer: 4
         Enter a string: Peace & Love.
         1.2
         1.2
         1.2
         1.2
         Peace & Love.
         Peace & Love.
         Peace & Love.
         Peace & Love.
    """
    float_number = float(input('Enter a floating point number:'))
    integer_number = int(input('Enter in a Positive Integers:'))
    string_name = str(input('Enter in a cool string:'))
    for k in range(integer_number):
        print(str(math.sqrt(float_number)))
    for k in range(integer_number):
        print(str(string_name))
    # -------------------------------------------------------------------------
    # Done: 5. Implement and test this function.
    #   The testing code is already written for you (above).
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
