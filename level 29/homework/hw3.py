# 3) შექმენით ფუნქცია, რომელიც იღებს წინადადებას, სადაც ყოველი სიტყვის შორის ერთზე მეტი დაშორებაა(space). თქვენი დავალებაა ჩამოაშოროთ გადმოცემულ წინადადებას ზედმეტი space-ები(სიტყვებს შორის მხოლოდ ერთი უნდა იყოს). საბოლოოდ დააბრუნეთ ეს წინადადება

proposal = input("Enter sentensive: ")
proposal += " "

def formating_space(prop):
    new_list = []
    new_proposal = ""
    for letter in prop:
        if letter != " ":
            new_proposal += letter
        else:
            new_list.append(new_proposal)
            new_proposal = ""

    new_prop = ""

    for word in new_list:
        if len(word) > 0:
            new_prop += word + " "
    return new_prop

print(formating_space(proposal))

