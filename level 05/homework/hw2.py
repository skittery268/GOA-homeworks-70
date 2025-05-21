# 2)მომხმარებელს შემოატანინეთ ორი რიცხვი გააკეთეთ მათზე მათემატიკური ოპერაციები  ("+, -, *, /, %, <, >, <=, >=, ==, !=. **) 
print("Please enter number 1.")
number_1 = int(input())
print("Please enter number 2.")
number_2 = int(input())

one = number_1 + number_2 
two = number_1 - number_2
three = number_1 * number_2
four = number_1 / number_2
five = number_1 % number_2
six = number_1 < number_2
seven = number_1 > number_2
eight = number_1 <= number_2
nine = number_1 >= number_2
ten = number_1 == number_2
eleven = number_1 != number_2
twelve = number_1 ** number_2

print(f"{number_1} + {number_2} = {one}")
print(f"{number_1} - {number_2} = {two}")
print(f"{number_1} * {number_2} = {three}")
print(f"{number_1} / {number_2} = {four}")
print(f"{number_1} % {number_2} = {five}")
print(f"{number_1} < {number_2} = {six}")
print(f"{number_1} > {number_2} = {seven}")
print(f"{number_1} <= {number_2} = {eight}")
print(f"{number_1} >= {number_2} = {nine}")
print(f"{number_1} == {number_2} = {ten}")
print(f"{number_1} != {number_2} = {eleven}")
print(f"{number_1} ** {number_2} = {twelve}")