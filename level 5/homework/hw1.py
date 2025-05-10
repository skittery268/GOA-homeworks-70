# 1)შემოატანინეთ მომხმარებელს რიცხვი  და თუ 10 ზე მეტი იქნება  გამოიტანინოს ("you are right ")
print("do this task: 7+4=?")
answer = int(input())

if answer > 10:
    print("You are right!")

if answer <= 10:
    print("You are wrong.")