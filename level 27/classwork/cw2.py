# 2)შექმენით ფუნქცია რომელიც არგუმენტად იღებს სიტყვას/წინადადებას და ასოს, ის აბრუნებს პირველი სად შეხვდა ასო ამ სიტყვაში

user_word = input("Please enter any word: ")
user_letter = input("Please enter any letter: ")

def word_find(word, letter):
    for i in word:
        return word.find(letter)
    return -1

print(word_find(user_word, user_letter))