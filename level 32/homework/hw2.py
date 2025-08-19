# 2)მოცემულია ორი სეტი: A = {1, 2, 3} და B = {3, 4, 5}.
# იპოვე ამ სეტების გაერთიანება.                                             1)
# იპოვე ამ სეტების გადაკვეთა.                                               2)
# იპოვე სეტ A-დან ის ელემენტები, რომლებიც არ ეკუთვნის სეტ B-ს.           3)

A = {1, 2, 3}
B = {3, 4, 5}

# 1)
result1 = A.union(B)
print(result1)

# 2)
result2 = A.intersection(B)
print(result2)

# 3)
result3 = A.difference(B)
print(result3)

