import pandas as pd 
from faker import Faker 
import random 
import re

df = pd.read_excel("Test_Input.xlsx",nrows=1, index = False)
#print(df)

##assign_Data_types

col_list = df.columns.tolist()

data_list = df.to_dict('r')

data_dict = data_list[0]
col_type_dict = {}
#print(data_dict)

##Data Types 

text_data = r"[a-zA-z]+"
numeric_data = r"^[-+]?[0-9]+$"
date_data = r"[\d]{1,2}-[\d]{1,2}-[\d]{2}"
bool_data = ["TRUE", "FALSE", "Y", "N"]

# # print(re.search(text_data, "Hi34"))
# # print(re.search(numeric_data, "12345Hi678"))
# # print(re.search(date_data, "2019-10-21"))

for col_name,col_value in data_dict.items():

    if (str(col_value).upper() == 'TRUE' or str(col_value).upper() == "FALSE" or str(col_value).upper() == "Y" or str(col_value).upper() == "N"):
        col_type_dict[col_name] = "Boolean" 
    elif(re.search(text_data,str(col_value)) != None):
        col_type_dict[col_name] = "Text"
    elif (re.search(numeric_data,str(col_value)) != None):
        col_type_dict[col_name] = "Number"
    elif (re.search(date_data,str(col_value))!= None):
        col_type_dict[col_name] = "Date"
    else: 
        col_type_dict[col_name] = "Others"

#print(col_type_dict)

output_dict = {}

output_list = []


row_num = 0
while row_num <=9 :
    

    for col_name in data_dict.keys():

        if col_type_dict [col_name] == "Boolean" : 
            output_dict[col_name] = random.choice([True, False])
        elif col_type_dict [col_name] == "Number" : 
            output_dict[col_name] = random.randint(1,99999)
        elif col_type_dict [col_name] == "Text" : 
            output_dict[col_name] = Faker().word()
        elif col_type_dict[col_name] == "Date" :
             output_dict[col_name] = Faker().date(pattern="%Y-%m-%d", end_datetime=None)
        else: 
            output_dict[col_name] = None
        output_tuple = tuple((val) for val in output_dict.values())
    output_list.append(output_tuple)
    row_num = row_num + 1
    

#print(output_list)

df_output_data = pd.DataFrame(output_list, columns = col_list)

print(df_output_data)

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('Test_Output.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.

df_output_data.to_excel(writer, sheet_name='Sheet1',index = False)

# Close the Pandas Excel writer and output the Excel file.
writer.save()