# 1) შექმენი dictionary, სადაც key = სტუდენტის სახელი, value = ქულა.
# შემდეგ loop-ით დაბეჭდე ყველა სტუდენტი და ქულა.

# dictionary (შეგიძლიათ გამოიყენოთ) :
# scores = {
#     "Ana": 95,
#     "Giorgi": 88,
#     "Luka": 76
# }


scores = {
    "Ana": 95,
    "Giorgi": 88,
    "Luka": 76
}

for name, score in scores.items():
    print(f"სტუდენტი: {name}, მისი ქულა: {score}.")

