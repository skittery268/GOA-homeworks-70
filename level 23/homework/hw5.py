# დავალება 5: სიტყვის ანალიზი — დაითვალე ხმოვნები და თანხმოვნები, სანამ სწორი არ იქნება

user_input = input("გთხოვთ შეიყვანოთ რაიმე სიტყვა რომელიც იწყება და მთავრდება თანხმოვანზე: ")

number_of_vowels = 0
number_of_consonants = 0

x = "აეიოუ"

while True:
    if user_input[0] in x or user_input[-1] in x:
        user_input = input("არასწორია, გთხოვთ შეიყვანოთ სიტყვა თავიდან: ")
    else:
        print(f"{user_input} სწორია, გმადლობთ.")
        for i in user_input:
            if i in x:
                number_of_vowels += 1
            else:
                number_of_consonants += 1
        print()
        print(f"ხმოვანი ასოების რაოდენობა: {number_of_vowels}")
        print(f"თანხმოვანი ასოების რაოდენობა: {number_of_consonants}")
        print()
        break


