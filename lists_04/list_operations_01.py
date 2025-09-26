# Using Lists
print('---- 1. Creating, Printing List ---- ')
my_list = [13, 6, 8, 2, 10]
print(my_list)
print(type(my_list))

print('---- 2. adding element to list [ append function , insert function ] --- ')
my_list.append(14)
my_list.insert(0, 22)
print(my_list)

print('---- 3. Access element by index and change it -----')
print(my_list[3])
my_list[3] = my_list[3] + 2
print(my_list)


print('----- 4. count elements of list _ Len function : General Function -------')
print(len(my_list))


print('-------- 5. delete element from the list -- remove() , pop() functions -----')
my_list.remove(14) # by value
my_list.pop(1) # by index
print(my_list)

print('-------- 6. reverse list ----------')
my_list_bkp = my_list.copy()
my_list.reverse()
print(my_list)
print(my_list_bkp)

print('------- 7. sort list -------------')
my_list.sort() # asc
print(my_list)
my_list.sort(reverse=True) # desc
print(my_list) 