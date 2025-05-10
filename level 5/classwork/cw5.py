# 5) მომხმარებელს შემოატანინეთ ორი სტრინგი და თუ ეს სტრინგები ერთმანეთს ემთხვევა გამოიტანეთ True ხოლო თუ არ ემთხვევა გამოიტანეთ False
print("please enter word:")
word_1 = input()
print("Please enter word number 2:")
word_2 = input()

one = "False"
two = "True"

if word_1 == word_2:
    print(two)

if word_1 > word_2:
    print(one)