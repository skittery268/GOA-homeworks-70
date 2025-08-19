# 2)შექენით სეტები და განიხილეთ ოპერატორები (union,intersection,difference,symmetric_difference,clear,add,remove) ახსენით ასევე კომენტარებით და გააკეთეთ ორივე ხერხით როგორც ტექსტიტ ისე სიმბოლოთი.

# .union()                ან                    |          -         set-ების გაერთიანება
a = {1, 2, 3}
b = {3, 4, 5}

result1 = a.union(b)
result2 = a | b

print(result1)
print(result2)

# .intersection()          ან                  &           -         set-ების თანაკვეთა
a1 = {1, 2, 3}
b2 = {3, 4, 5}

result01 = a1.intersection(b2)
result02 = a1 & b2

print(result01)
print(result02)

# .add()                                                  -          set-ში რაიმეს დამატება
set_1 = {1, 2, 3, 4}

set_1.add(10)

print(set_1)

# .remove()                                               -          set-იდან რაიმეს წაშლა
my_set = {1, 2, 3, 4, 5}

my_set.remove(2)

print(my_set)

# .difference()             ან           -                   -          set-ს გამოვაკლოთ set-ი
set_a = {1, 2, 3, 4}
set_b = {4, 5, 6, 7}

result001 = set_a.difference(set_b)
result002 = set_a - set_b

print(result001)
print(result002)

# .clear()                                                -         set-ის გასუფთავება
new_set = {1, 2, 3, 4, 5, 6, 7}

new_set.clear()

print(new_set)

# .symmetric_difference()         ან          ^                -         set-ს გამოვაკლოთ სხვა სეტთან საორთო სიმბოლო.
my_set01 = {1, 2, 3, 4, 5}
my_set02 = {5, 6, 7, 8, 9}

result0001 = my_set01.symmetric_difference(my_set02)
result0002 = my_set01 ^ my_set02

print(result0001)
print(result0002)

