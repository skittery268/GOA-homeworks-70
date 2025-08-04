# 2) შექმენით ფუნქცია რომელიც მიიღებს რიცხვების სიას და დაბრუნებს მხოლოდ ლუწების ჯამს.

numbers = [5, 3, 1, 2, 6, 8, 9]
print(numbers)

def even_sum(numbers):
    sum_variable = 0
    for number in numbers:
        if number % 2 == 0:
            sum_variable += number
    return sum_variable

print(even_sum(numbers))