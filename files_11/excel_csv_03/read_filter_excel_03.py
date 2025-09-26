# program to read a csv file, Filter data cy city = Cairo then write only these data to another excel csf
import csv

with (open('C:\\MY_FILES\\people.csv', 'r') as my_file_reference1,
      open('C:\\MY_FILES\\people_cairo.csv', 'w', newline='') as my_file_reference2):
    reader_pen = csv.reader(my_file_reference1)  # List of rows
    writer_pen = csv.writer(my_file_reference2)
    writer_pen.writerow(['Name', 'Age', 'City'])
    for row in reader_pen:
        if row[2].lower() == 'cairo':
            writer_pen.writerow(row)
