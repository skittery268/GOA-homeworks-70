# 7) მომხმარებელს შემოატანინეთ წელი და შეამოწმეთ, თუ ის არის ნაკიანი დაბეჭდეთ "This is leap year".(ნაკიანი წელიწადი იყოფა 4-ზე და არ იყოფა 100-ზე ან იყოფა 400-ზე)

year = int(input("Please enter year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("This is leap year")