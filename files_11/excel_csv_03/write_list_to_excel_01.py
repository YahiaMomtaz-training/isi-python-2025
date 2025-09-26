# program to write list content to a csv file
import csv

people_list = [
    ['Name', 'Age', 'City'],
    ['Adham', 25, 'Assuit'],
    ['Esam', 30, 'Cairo'],
    ['Shady', 28, 'Mansoura']
]

with open('C:\\MY_FILES\\people.csv', 'w', newline='') as my_file_reference:
    write_pen = csv.writer(my_file_reference)
    for item in people_list:
        write_pen.writerow(item)

    """
    write_pen.writerow(['id', 'Name', 'Salary'])
    write_pen.writerow( [101, 'yahia', 7000] )
    write_pen.writerow([102, 'omar', 5000])
    write_pen.writerow([103, 'Hoda', 9000])
    """
