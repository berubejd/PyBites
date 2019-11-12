#!/usr/bin/env python3.8

shakespeare_unformatted = """
                          To be, or not to be, that is the question:
                          Whether 'tis nobler in the mind to suffer

                          The slings and arrows of outrageous fortune,
                          Or to take Arms against a Sea of troubles,
                          """

remember_unformatted = """
                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand
                      """

INDENTS = 4

def print_hanging_indents(poem):
    first_line = True

    for line in poem.splitlines():
        line = line.strip()

        if line == '':
            first_line = True
            continue

        if first_line:
            print(line)
            first_line = False
        else:
            print(f'{" " * INDENTS}{line}')

print_hanging_indents(shakespeare_unformatted)
print()
print_hanging_indents(remember_unformatted)
