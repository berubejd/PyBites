#!/usr/bin/env python3.8

names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""

    for line_no, (name, country) in enumerate(zip(names, countries), 1):
        print(f'{line_no}. {name:11}{country}')

enumerate_names_countries()