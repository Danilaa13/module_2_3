my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
count = 0
while count < len(my_list):
    n = my_list[count]
    count += 1
    if n == 0:
        continue
    elif n < 0:
        break
    elif n > 0:
        print(n)