# დავალება 5: ასაკი და კვება
# მომხმარებელი შეიყვანს ასაკს. პროგრამა გასცემს კვების რეკომენდაციას:

# 0–12 → "ბევრი ვიტამინიანი საკვები"

# 13–25 → "ენერგიის მომცემი საკვები"

# 26–59 → "ბალანსირებული რაციონი"

# 60+ → "დაბალკალორიული და მსუბუქი საკვები"

age = int(input("გთხოვთ შეიყვანოთ თქვენი ასაკი: "))

if age <= 0:
    print("თქვენ შეიყვანეთ არასწორი ასაკი. ")
elif age <= 12:
    print("ბევრი ვიტამინიანი საკვები. ")
elif age <= 25:
    print("ენერგიის მომცემი საკვები. ")
elif age <= 59:
    print("ბალანსირებული რაციონი. ")
elif age >= 60:
    print("დაბალკალორიული და მსუბუქი საკვები. ")