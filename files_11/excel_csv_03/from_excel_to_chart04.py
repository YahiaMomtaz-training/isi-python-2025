# program to read excel file csv and plot a chart
import csv
import matplotlib.pyplot as plt

with open('C:\\MY_FILES\\people.csv', 'r') as my_file_reference:
    reader_pen = csv.reader(my_file_reference)
    reader_pen.__next__() # skip the first row [ header ]
    x_axis = []  # names
    y_axis = []  # ages
    for row in reader_pen:
        x_axis.append(row[0])  # names
        y_axis.append(float(row[1]))  # ages

    plt.bar(x_axis, y_axis)
    plt.xlabel('Names')
    plt.ylabel('Ages')
    plt.title('Bar Chart from CSV Data')
    plt.xticks(rotation=45)
    plt.show()
