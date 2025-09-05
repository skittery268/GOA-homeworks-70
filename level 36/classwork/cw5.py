# 5) უკვე შექმნილ Dictionary-დან, შეცვალე key ისე, რომ value იგივე დარჩეს და დაბეჭდე Dictionary საბოლოო   სახით (გააკეთეთ pop-ით)

my_dict = {
    "name": "Saba",
    "surename": "Dzidzikashvili",
    "age": 15
}

my_dict["წლოვანება"] = my_dict.pop("age")

print(my_dict)

