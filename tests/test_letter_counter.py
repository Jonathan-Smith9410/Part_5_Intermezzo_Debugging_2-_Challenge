from lib.letter_counter import *

def test_example_given():
    counter = LetterCounter("Digital Punk")
    assert counter.calculate_most_common() == [2, "i"]