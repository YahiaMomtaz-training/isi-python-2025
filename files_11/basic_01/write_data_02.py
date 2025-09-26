# program to write data to a text files

print('-------- first way ---------')

my_file_reference = open('C:\\MY_FILES\\write_data.txt', 'w')
my_file_reference.write('I Like programming\n')
my_file_reference.write('I Like Football\n')
my_file_reference.write('Python is my Favourite programming language\n')
my_file_reference.close()

print('----- Second way --- using with ---- ')
with open('C:\\MY_FILES\\write_data.txt', 'a') as my_file_reference:
    my_file_reference.write('\n')
    my_file_reference.write('My city is Cairo\n')
    my_file_reference.write('My city is Alex\n')
    my_file_reference.write('Iam an Engineer')
