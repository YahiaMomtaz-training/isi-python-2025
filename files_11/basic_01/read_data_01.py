# program to read and print the content of a text file
"""
to read a text files
1- open the file
2- read the content
3- close the file
"""
print('---- First way ----')
my_file_reference = open('C:\\MY_FILES\\read_data.txt', 'r')
content = my_file_reference.read()
print(content)
my_file_reference.close()

print('---- Second Way using with clause ignore close() ----')
with open('C:\\MY_FILES\\read_data.txt', 'r') as my_file_reference:
    content = my_file_reference.read()
    print(content)





