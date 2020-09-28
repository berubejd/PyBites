#!/usr/bin/env python3.8

PYBITES = "pybites"


def convert_pybites_chars(text):
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    # new_text = []

    # for letter in text:
    #     if letter.lower() in PYBITES:
    #         if letter == letter.lower():
    #             letter = letter.upper()
    #         else:
    #             letter = letter.lower()

    #     new_text.append(letter)

    # return "".join(new_text)

    return "".join(
        letter.swapcase() if letter.lower() in PYBITES else letter for letter in text
    )


print(
    convert_pybites_chars("Today we added TWO NEW Bites to our Platform, exciting!")
)  # 'todaY wE addEd tWO NeW bITES To our plaTform, ExcITIng!'
