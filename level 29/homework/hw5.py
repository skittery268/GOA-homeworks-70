# 5) შექმენით ფუნქცია, რომელსაც გადაეცემა წინადადება. თქვენი დავალებაა ამ წინადადების სიტყვები შეაბრუნოთ და დააბრუნოთ (სიტყვების სიმბოლოები არ უნდა იყოს შებრუნებული) 

proposal = "Hello world, my name is Saba "
print(proposal)
print()

def reverse_sentensive(prop):
    words = []
    sentensive = ""
    for letter in prop:
        if letter != " ":
            sentensive += letter
        else:
            words.append(sentensive)
            sentensive = ""
    
    new_proposal = ""
    new_list = words[::-1]

    for proposal in new_list:
        new_proposal += proposal + " "
    return new_proposal

print(reverse_sentensive(proposal))

