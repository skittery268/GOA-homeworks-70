# 2) შექმენით ფუნქცია, რომელსაც გადაეცემა ორი რიცხვების სია, გადაურეთ ორივეს for ციკლით და გაიგეთ თითოეულ სიაში რიცხვების ჯამი(შეინახეთ ცალკე ცვლადებში), გაამრავლეთ ორივე ერთმანეთზე და დააბრუნეთ

numbers1 = [10, 20, 30, 40, 50]
numbers2 = [100, 200, 10, 40, 20]

def two_list_sum(num1, num2):
    sum1 = 0
    for numbers1 in num1:
        sum1 += numbers1
    
    sum2 = 0
    for numbers2 in num2:
        sum2 += numbers2
    
    return sum1 * sum2

print(two_list_sum(numbers1, numbers2))

