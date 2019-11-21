#
# Eshita Mittal
# CSCI 102 - Section E
# Python Workshop 12

num = int(input('Enter the range number: '))

n = 0
value_1 = 0
value_2 = 1

while (n < num):
    if (n <= 1):
        next_num = n
    else:
        next_num = value_1 + value_2
        value_1 = value_2
        value_2 = next_num
    print(next_num)
    n += 1




