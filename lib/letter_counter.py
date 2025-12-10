# File: lib/letter_counter.py

# Original bugged code:

# class LetterCounter:
#     def __init__(self, text):
#         self.text = text

#     def calculate_most_common(self):
#         counter = {}
#         most_common = None
#         most_common_count = 1
#         for char in self.text:
#             if not char.isalpha():
#                 continue
#             counter[char] = counter.get(char, 1) + 1
#             if counter[char] > most_common_count:
#                 most_common = char
#                 most_common_count += counter[char]
#         return [most_common_count, most_common]

class LetterCounter:
    def __init__(self, text):
        self.text = text

    def calculate_most_common(self):
        counter = {}
        most_common = None
        most_common_count = 0 # Changed from 1 to 0 as would always be 1 ahead of actual value due to loop incrementing value by 1. Not actually necesary to change - see line 36 annotation.
        for char in self.text:
            if not char.isalpha():
                continue
            counter[char] = counter.get(char, 0) + 1 # Changed (char, 1) to (char 0) or it initiated every new char with 2 instead of 1
            if counter[char] > most_common_count: 
                most_common = char
                most_common_count = counter[char] # was originally += counter += car which just added on to original value. This gets the value from the dict.
        return [most_common_count, most_common]


counter = LetterCounter("Digital Punk")
print(counter.calculate_most_common())
# Intended output:
# [2, "i"]
