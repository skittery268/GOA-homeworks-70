# 4) შექმენით ფუნქცია, რომელიც იღებს წინადადებას, და მასში space-ების მაგივრად სიტყვებს შორის ჩასვამს ტირეს("-"). საბოლოოდ კი აბრუნებს მას

proposal = "Hello my name is Saba "
print(proposal)

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
        new_proposal += word + "-"
    return new_proposal

print(words(proposal))

