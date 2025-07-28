# 1) შექმენით ფუნქცია, რომელსაც გადაეცემა სიმბოლოების სია. ფუნქციამ უნდა დააბრუნოს ეს სია პირველი და ბოლო ელემენტების გარეშე, გამოიყენეთ slicing-ი

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)
print()

def slicing_list(list):
    return list[1:-1]

print(slicing_list(numbers))

