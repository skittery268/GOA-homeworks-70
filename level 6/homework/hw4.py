# 5) მომხმარებელს შემოატანინეთ რიცხვი და თუ ის არის ლუწი და არის 10-ზე მეტი, ან ტოლია 7-ის, დაბეჭდეთ True

number = int(input("Please enter number: "))


if number % 2 == 0 and number > 10 or number == 7:
    print(True)

