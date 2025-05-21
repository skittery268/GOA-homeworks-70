# 3) შემოატანინეთ მომხმარებელს სტრინგი და თუ მომხმარებლის შემოტანილი სტრინგი არის 'yes', მაშინ შემოატანინეთ სახელი და გამოიტანეთ ის. ყველა ვარიანტში საბოლლოდ დაემშვიდობეთ მომხმარებლლს მესიჯი 'goodbye' - თი
print("Answer the question: Do you want your future to be succesful?")
answer = input()

if answer == "yes":
    print("Thank you for answer, whar's your name?")
    input()
    print("Thank you, goodbye!")

if answer == "no":
    print("Thank you for answer, goodbye!")