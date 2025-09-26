from xml.sax.handler import property_dom_node

import pandas as pd
# from pandas import DataFrame, read_csv

"""
# dict of lists to create a dataframe
df = pd.DataFrame(
    {
    "Name": ["Ali", "Sara", "Omar"],
    "Age": [25, 30, 22],
    "City": ["Cairo", "Alex", "Giza"]
}
)
"""
df = pd.read_csv("C:\\MY_FILES\\people.csv")
print('---- print all data-----')
print(df)   # print all data
print('---- print first 3 rows ------')
print(df.head(3))   # print first 3 rows
print('------ print last 3 rows ----')
print(df.tail(3))   # print last 3 rows
print('----- print a column -----')
print(df["Name"]) # print a column
# print(df[["Name", "Age", "City"]].head()) # print Multi column
print('----- print count of rows -----')
print(len(df)) # print count of rows
print('----- print count not null values of each column -----')
print(df["City"].count())   # print count not null values of each column
print('------print count of each value in a column ----')
print(df["City"].value_counts()) # print count of each value in a column
print('-------print sorted data frame ---')
print(df.sort_values(by="Age", ascending=False)) # print sorted data frame
print('------ print data frame where age > 25 ----')
print(df[df["Age"] > 25])   # print data frame where age > 25
print('----- print data frame where age > 25 and city = Cairo -----')
print(df[(df["Age"] > 25) & (df["City"] == "Cairo")]) # print data frame where age > 25 and city = Cairo
print('----- print data frame where age > 25 or city = Cairo -----')
print(df[(df["Age"] > 25) | (df["City"] == "Cairo")]) # print data frame where age > 25 or city = Cairo
print('----- print data frame where age > 25 and sort by age -----')
print(df[(df["Age"] > 25)].sort_values(by="Age", ascending=True)) # print data frame where age > 25 and sort by age
print('--------- Loop over DF -------------')
for index, row in df.iterrows():
    df.loc[index, "Age"] = row["Age"] + 20      # row = index, column = Age
    print(index, row["Name"], row["Age"], row["City"])
print('----- push DF to Lists of Lists -----')
rows_list = df.values.tolist()
print(rows_list)
print('----- Modify DF and push it to another CSV file -----')
df["Age"] = df["Age"] + 1          # increase all ages by 1
df = df.sort_values("Age")         # sort by age ascending

print("Modified DataFrame:")
print(df)
df.to_csv("C:\\MY_FILES\\people_modified_pandas.csv", index=False) # push DF to another CSV file