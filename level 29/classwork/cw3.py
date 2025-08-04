# 3) შექმენით ფუნქცია რომელიც აბრუნებს სიაში უმაღლეს რიცხვს.

numbers = [1, 11, 3, 4, 1, 2, 3, 8, 0, 1, 2, 3, 4, 10]

def number(num_list):
    num_list.sort()
    return num_list[-1]

print(number(numbers))

