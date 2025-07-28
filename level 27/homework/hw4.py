# 4) შექმენით ფუნქცია, რომელსაც გადაეცემა რიცხვების სია. გადაუარეთ ამ სიას for ციკლით და ჩაამატეთ მხოლოდ ლუწი რიცხვები ახალ სიაში. საბოლოოდ დააბრუნეთ ეს სია

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 200, 100, 101]
print(num_list)

def even_numbers(num_list):
    even_numbers = []
    for even in num_list:
        if even % 2 == 0:
            even_numbers.append(even)
    return even_numbers

print(even_numbers(num_list))

