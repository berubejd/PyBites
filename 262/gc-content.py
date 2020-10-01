#!/usr/bin/env python3.8

from collections import Counter


def calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    ACCEPTED = "AGCT"

    counter = Counter(sequence.upper())

    for k in list(counter):
        if not k in ACCEPTED:
            del counter[k]

    gc_content = counter["G"] + counter["C"]
    total_content = sum(counter.values())

    return round(gc_content / total_content * 100, 2)
