old_list = [x**3 + 17 for x in range(1, 1001, 2)]
my_list = []
i = 0
while i < len(old_list):
    my_sum = 0
    y = old_list[i]
    while y > 0:
        number = y % 10
        my_sum = my_sum + number
        y = y // 10
    if my_sum % 7 == 0:
        my_list.append(old_list[i])
    i += 1
print(old_list)
print(sum(my_list))
