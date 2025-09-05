# 6) dictionary ფასებით:

# products = {
#     "apple": 3,
#     "banana": 2,
#     "milk": 5
# }


# დაბეჭდე ყველა პროდუქტი for loop-ით.

# მომხმარებლისგან შეიყვანე პროდუქტი, თუ არსებობს → დაბეჭდე ფასი.

# დაამატე ახალი პროდუქტი update()-ით.

# ბოლოს გამოიყენე clear() ჩასაშენებლად, მაგალითად, ცარიელი dictionary-ს დაბეჭდვა დასუფთავების შემდეგ.

products = {
    "apple": 3,
    "banana": 2,
    "milk": 5
}

for key, value in products.items():
    print(key)

product = input("Please select a product: ")

if product in products:
    print(f"Its price: {products[product]}")
else:
    print("We don't have such a product.")

products.update({"Orange": 3, "Ice creem": 4})

products.clear()

print(products)