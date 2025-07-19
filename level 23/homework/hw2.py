# დავალება 2: 5 სიტყვის შეყვანა, და შენახვა მხოლოდ სწორების

x = "აეიოუ"

correct_word_list = []

for i in range(5):
    user_input = input("გთხოვთ შეიყვანოთ რაიმე სიტყვა რომელიც იწყება და მთავრდება თანხმოვანზე: ")
    print()
    if user_input[0] in x or user_input[-1] in x:
        print("არასწორია, სცადეთ თავიდან")
        print()
    else:
        print("გმადლობთ, სწორია, თქვენი სიტყავ იყო დამატებული სიაში.")
        correct_word_list.append(user_input)
        print()

print(f"თქვენს მიერ შეყვანილი სწორი სიტყვების სია: {correct_word_list}")

