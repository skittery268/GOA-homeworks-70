# 3) შექმენით ფუნქცია, რომელსაც გადაეცემა რიცხვების სია. გადაუარეთ ამ სიას while ციკლით და ჩაამატეთ გაორმაგებული რიცხვები ახალ სიაში. საბოლოოდ დააბრუნეთ ეს სია

numbers = [5, 6, 10, 4, 3, 8, 10]
print(numbers)

def doubled_numbers(num_list):
    new_list = []
    number = 0
    while number < len(num_list):
        doubled_number = num_list[number] * 2
        new_list.append(doubled_number)
        number += 1
    return new_list

print(doubled_numbers(numbers))

