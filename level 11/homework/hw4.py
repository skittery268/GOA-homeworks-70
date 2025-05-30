# 4) მომხმარებელი შეიყვანს ორ რიცხვს და ოპერაციას (+, -, *, /)
# დაბეჭდე შედეგი შესაბამისი მოქმედებით.
# თუ ოპერაცია არასწორია (მაგ 0-ს გაყოფა ან ტექსტი ან უცხო სიმბოლო) → "არასწორი ოპერაცია!"

num1 = int(input("Please enter any number: "))
math_operation = input("Please enter mathematical operation (+, -, *, /): ")
num2 = int(input("Please enter any number: "))

if math_operation == "+":
    sum = num1 + num2
    print(f"{num1} + {num2} = {sum}")
elif math_operation == "-":
    difference = num1 - num2
    print(f"{num1} - {num2} = {difference}")
elif math_operation == "*":
    multiplied = num1 * num2
    print(f"{num1} * {num2} = {multiplied}")
elif num1 == 0 or num2 == 0:
    print("არასწორი ოპერაცია!")
elif math_operation == "/":
    division = num1 / num2
    print(f"{num1} / {num2} = {division}")
else:
    print("არასწორი ოპერაცია!")