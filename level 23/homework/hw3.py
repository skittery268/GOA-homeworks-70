# დავალება 3: დაითვალე, რამდენჯერ სცადა სწორი სიტყვის შეყვანა

user_input = input("გთხოვთ შეიყვანოთ რაიმე სიტყვა რომელიც იწყება და მთავრდება თანხმოვანზე: ")

wrong_word_count = 0

x = "აეიოუ"

while True:
    if user_input[0] in x or user_input[-1] in x:
        user_input = input("არასწორია, გთხოვთ შეიყვანოთ სიტყვა თავიდან: ")
        wrong_word_count += 1
    else:
        print(f"{user_input} სწორია, გმადლობთ.")
        print(f"არასწორად შეყვანილი სიტყვების რაოდენობა: {wrong_word_count}")
        break

