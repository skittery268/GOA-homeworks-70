# 1) მომხმარებელს შემოატანინეთ სიტყვა, თუ ამ სიტყვის სიგრძე არის 5-ზე მეტი, მაშინ გამოვიტანოთ ყველა ასო, პატარა შრიფტით, თუ არადა დიდით.

word = input("Please enter any word: ")

word_len = len(word)

if word_len > 5:
    print(word.lower())
else:
    print(word.upper())

