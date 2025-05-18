# 5)მომხმარებელმა უნდა შეიყვანოს რიცხვი n. პროგრამამ while ციკლით უნდა დაითვალოს 1-დან n-მდე რიცხვების ჯამი.

n = int(input("Please enter a number: ")) 

count = 1
sum = 0

while count <= n:
    sum += count
    count += 1
print(sum)