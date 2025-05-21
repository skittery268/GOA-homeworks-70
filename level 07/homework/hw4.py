# 4)დაწერე პროგრამა, რომელიც სთხოვს მომხმარებელს პაროლის შეყვანას. სწორი პაროლია "python123". სანამ სწორად არ შეიყვანს, მოთხოვე თავიდან.

password = "python123"

user_password = input("Please enter your password: ")

if user_password == password:
    print("access granted.")

while user_password != password:
    user_password = input("Wrong! Please enter your password again: ")
    if user_password == password:
        print("access granted.")