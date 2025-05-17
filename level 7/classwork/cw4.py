# 4) მომხმარებელს შემოაყვანინეთ რიცხვი, სანამ ეს რიცხვი არ იქნება 100-ზე მეტი მაქამდე თავიდან მოთხოვთ რიცხვის შემოტანა

user_number = int(input("Please enter a number greater than 100: "))

while user_number < 100:
    print("Wrong")
    user_number = int(input("Please enter a number greater than 100: "))

print("Wright, thank you wery much.") 