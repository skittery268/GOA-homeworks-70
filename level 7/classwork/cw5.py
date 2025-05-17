# 5) მომხმარებელს შემოატანინეთ სხვადასხვა სახელები 5-ჯერ იტერაციის მეშვეობით, შექმენით ამ სახელებისთვის ცვლადი რომელშიც ყოველი სახელი დაემატება და ეს სახელები გამოიყოფა მძიმეებით, ანუ თქვენი ცვლადი 5 სახელის შეყვანის შემდეგ უნდა გამოიყურებოდეს ასე: "{სახელი პირველი}, {სახელი მეორე}, ... {სახელი მეხუთე}" 

count = 0

while count < 5:
    name = input("Please enter name: ") 
    name2 = input("Please enter name number 2: ")
    name3 = input("Please enter name number 3: ")
    name4 = input("Please enter name number 4: ")
    name5 = input("Please enter name number 5: ")
    count = count + 5
print(f"User names: {name}, {name2}, {name3}, {name4} and {name5}.")