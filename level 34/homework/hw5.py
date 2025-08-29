# 5)შექმენით tuple სადაც შეინახავთ სიტყვებს შემდეგ დაწერე პროგრამა, რომელიც დაითვლის, რამდენჯერ მეორდება რომელიმე სიტყვა ტაპლში.

my_tuple = ("Hello", "Hello", "Tuple", "Tuple")

result1 = my_tuple.count("Hello")
result2 = my_tuple.count("Tuple")

print(f"სიტყვა hello მეორდება {result1}-ჯერ")
print(f"სიტყვა tuple მეორდება {result2}-ჯერ")

