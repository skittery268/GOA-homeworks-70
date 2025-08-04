# 1) შექმენით ფუნქცია, რომელიც მიიღებს წინადადებას, ფუნქციამ ამ წინადადების თითოეული სიტყვა უნდა შეინახოს სიაში, როგორც ცალკე ელემენტი. საბოლოოდ გადააქციეთ სია ისევ წინადადებად, სადაც სიტყვებს შორის არის მძიმე და ერთი დაშორება(", ")

proposal = "Hello my name is Saba "
print(proposal)
print()

def words(prop):
    my_list = []
    list_word = ""
    for letter in prop:
        if letter != " ":
            list_word += letter
        else:
            my_list.append(list_word)
            list_word = ""
    
    new_proposal = ""
    
    for word in my_list:
        new_proposal += word + ", "
    return new_proposal

print(words(proposal))

