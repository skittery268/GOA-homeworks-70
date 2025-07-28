# 5) შექმენით ფუნქცია, რომელსაც გადაეცემა სახელების სია. შექმენით ახალის სია, სადაც ჩაამატებთ გადმოცემული სიიდან მხოლოდ იმ სახელებს, რომლებიც იწყება "N"-ზე`. საბოლოოდ დააბრუნეთ ეს სია

names = ["Nika", "Ana", "Saba", "Nana", "nunu", "Giorgi"]
print(names)

def name_list(names):
    new_names = []
    for name in names:
        if name[0] == "n" or name[0] == "N":
            new_names.append(name)
    return new_names

print(name_list(names))

