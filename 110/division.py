#!/usr/bin/env python3.8

def divide_numbers(numerator, denominator):
    """For this exercise you can assume numerator and denominator are of type
       int/str/float.
       Try to convert numerator and denominator to int types, if that raises a
       ValueError reraise it. Following do the division and return the result.
       However if denominator is 0 catch the corresponding exception Python
       throws (cannot divide by 0), and return 0"""

    try:

        numerator = int(numerator)
        denominator = int(denominator)

        result = numerator / denominator

    except ZeroDivisionError:

        result = 0 

    except ValueError:

        raise ValueError('Unable to convert to int!')

    return result


print(divide_numbers(1,2))
print(divide_numbers(1,11))
print(divide_numbers(1,0))
print(divide_numbers(1,'zzap'))
