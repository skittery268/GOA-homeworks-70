# 1)classwork: შექმენით ფუნქცა რომელიც იღებს წინადადებას და აბრუნებ რამდენი სიტყვაა მასში.

name = input("შეიყვანეთ სახელი: ")

def len_word(word):
    len_name = len(word)
    return f"თქვენ სიტყვაში {len_name} ასოა"

print(len_word(name))