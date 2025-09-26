my_list = [13, 6, 8, 2, 10, 17]
print('--- for i loop ---')
total = 0
for i in range(len(my_list)):
    print(my_list[i])
    total = total + my_list[i]

print('Total = ', total)

print('--- for each loop ----')
total = 0 # reset value
for item in my_list:
    print(item)
    total = total + item

print('Total ', total)