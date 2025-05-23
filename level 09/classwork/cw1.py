# მომხმარებელს შემოატანინეთ სამი რიცხვი, start/end/step და ჩასვით for loop-ში სათანადო ადგილას.

number = int(input("Please enter any number: "))
number2 = int(input("Please enter any number 2: "))
number3 = int(input("Please enter any number 3: "))

for i in range(number, number2, number3):
    print(i)