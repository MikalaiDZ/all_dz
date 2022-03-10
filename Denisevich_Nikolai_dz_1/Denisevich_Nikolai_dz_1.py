sec = int(input('Введите секунды:'))

day = sec // (24*3600)
sec %= 24*3600
hours = sec // 3600
sec %= 3600
min = sec // 60
sec %=60

print(day, 'д', hours, 'ч', min, 'мин', sec, 'сек')