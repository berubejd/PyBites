#!/usr/bin/env python3.8

import pytest

from workouts import print_workout_days

testdata = [
    ("lower", "Tue, Fri"),
    ("LOWER", "Tue, Fri"),
    ("loWer", "Tue, Fri"),
    ("upper", "Mon, Thu"),
    ("cardio", "Wed"),
    ("something", "No matching workout"),
    ("wed", "No matching workout"),
    ("lower upper", "No matching workout"),
]


@pytest.mark.parametrize("workout,expected", testdata)
def test_print_workout_days(workout, expected, capsys):
    print_workout_days(workout)

    captured = capsys.readouterr()
    assert captured.out.strip() == expected


"""
Bite 246. Test print / standard output ☆
In this Bite you test a function that prints to stdout. Check out pytest's Capturing of the stdout/stderr output how to test this. You probably want to use the capsys / capfd fixture in your test code.

Have fun and keep calm and code in Python!
"""
