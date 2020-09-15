#!/usr/bin/env python3.8


def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    approved_value_types = [int, float]
    approved_formats = ["cm", "in"]

    if not type(value) in approved_value_types:
        raise TypeError("Incorrect value.  Must be int or float.")

    if not fmt.lower() in approved_formats:
        raise ValueError("Not the correct format.  Must be 'in' or 'cm'.")

    if fmt.lower() == "cm":
        value *= 2.54
    else:
        value /= 2.54

    return round(float(value), 4)


print(convert(1, "cm"))
