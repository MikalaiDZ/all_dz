pro_list = [x for x in range(1,101)]
i = 0
while i < len(pro_list):
    if pro_list[i] in (1, 21, 31, 41, 51, 61, 71, 81, 91):
        print(pro_list[i], 'процент')
    elif pro_list[i] in (2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54, 62, 63, 64, 72, 73, 74,
                         82, 83, 84, 92, 93, 94):
        print(pro_list[i], 'процента')
    else:
        print(pro_list[i], 'процентов')
    i+=1

print(pro_list)