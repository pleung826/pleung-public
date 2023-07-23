import re

def word_length(input_str: str):
    """
    Word Length Calculator
    """
    split_string = re.split(r"[ /.]", input_str)

    return {string.lower(): len(string) for string in split_string if string}

input_1 = "This is a test string"

input_2 = "We're going to test all corner/edge scenarios."

input_3 = "This is another the test string/case. The difference here is that we have two sentences"

print(word_length(input_1))