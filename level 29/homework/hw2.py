# 2) შექმენით ფუნქცია, რომელიც მიიღებს წინადადებას და დაბეჭდავს მის თითოეულ სიტყვაში სიმბოლოების რაოდენობას(ცალ-ცალკე)

proposal = "Hello my name is Saba "
print(proposal)
print()

def prop_len(prop):
    my_list = []
    new_prop = ""
    for letter in prop:
        if letter != " ":
            new_prop += letter
        else:
            my_list.append(new_prop)
            new_prop = ""
    
    for word in my_list:
        word_len = len(word)
        print(f"{word} ამ სიტყვაში {word_len} ასოა")

print(prop_len(proposal))

