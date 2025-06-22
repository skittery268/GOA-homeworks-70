# 4) შეიყვანე ტექსტი და დაბეჭდე ბოლო სიმბოლო ინდექსის მეშვეობით (არა სლაისინგით და არა უარყოფითი ინდექსით).
# მაგ: "hello" → `o` (მოძებნე `len(text) - 1` ინდექსით)

string = "Hello world"

last_letter = len(string) - 1

print(f"the last letter of the word: {string[last_letter]}")