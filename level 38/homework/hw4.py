# 4)https://www.codewars.com/kata/55f1b763dd670651620000ce

# დავალება:

# Define a method named countCharOccurrences or count_char_occurrences that accepts a string and a char as inputs and returns the number of times the char occurs in the string as an int.

# შესრულებული დავალება:

def count_char_occurrences(strng, char):
    sum = 0
    for i in strng:
        if i == char:
            sum += 1
    
    return sum