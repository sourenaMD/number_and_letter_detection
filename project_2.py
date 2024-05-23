import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('C://Users//soure//Desktop//مباحث ویژه(ترم 8)//project_2//digits.csv')

columns_except_last = data.columns[:-1]

# saving all of the values in a list
list_of_values = []
for index, row in data.iterrows():
    for column in columns_except_last:
        value = row[column]
        list_of_values.append(value)

# reshape each row of the data into a matrix        
re_shaped = []
for i in range(0 , len(list_of_values) , 64):
    re_shaped.append(np.reshape(np.array(list_of_values[i : i + 64]), (8 , 8)))
print(re_shaped[2])

# counting the zeros and ones of each row
zeros_of_rows = []
ones_of_rows = []    
second_length = len(re_shaped[0][0])    
for i in range(len(re_shaped)):
    matrix = re_shaped[i]
    zeros_of_matrixes = []
    ones_of_matrixes = []
    for j in range(second_length):
        zeros_row = sum(1 for x in re_shaped[i][j] if x == 0)
        ones_row = second_length - zeros_row
        zeros_of_matrixes.append(zeros_row)
        ones_of_matrixes.append(ones_row)
    zeros_of_rows.append(zeros_of_matrixes)
    ones_of_rows.append(ones_of_matrixes)
    
# counting the zeros and ones of each row
zeros_of_cols = []
ones_of_cols = []
for i in range(0 , len(list_of_values) , 64):
    matrix = list_of_values[i : i + 64]
    n = 0
    zeros_of_matrixes = []
    ones_of_matrixes = []
    for j in range(second_length):
        zeros_cols = sum(1 for x in matrix[n::8] if x == 0 )
        ones_cols = second_length - zeros_cols
        zeros_of_matrixes.append(zeros_cols)
        ones_of_matrixes.append(ones_cols)
        n += 1
    zeros_of_cols.append(zeros_of_matrixes)
    ones_of_cols.append(ones_of_matrixes)

# get the mean of each row
means_of_rows_of_matrixes = []
for i in range(len(re_shaped)):
    matrix = re_shaped[i]
    list_of_means_of_rows = []
    for j in range(second_length):
        row_mean = np.mean(re_shaped[i][j])
        list_of_means_of_rows.append(row_mean)
    means_of_rows_of_matrixes.append(list_of_means_of_rows)
    
# get the mean of each column
means_of_cols_of_matrixes = []
for i in range(0 , len(list_of_values) , 64):
    matrix = list_of_values[i : i + 64]
    n = 0
    list_of_means_of_cols = []
    for j in range(second_length):
        cols_values = [x for x in matrix[n::8]]
        list_of_means_of_cols.append(np.mean(cols_values))
        n += 1
    means_of_cols_of_matrixes.append(list_of_means_of_cols)

# get the max and min of each row
max_of_rows_of_matrixes = []
min_of_rows_of_matrixes = []
for i in range(len(re_shaped)):
    matrix = re_shaped[i]
    list_of_max_of_rows = []
    list_of_min_of_rows = []
    for j in range(second_length):
        row_max = max(re_shaped[i][j])
        row_min = min(re_shaped[i][j])
        list_of_max_of_rows.append(row_max)
        list_of_min_of_rows.append(row_min)
    max_of_rows_of_matrixes.append(list_of_max_of_rows)
    min_of_rows_of_matrixes.append(list_of_min_of_rows)

# get the max and min of each column
max_of_cols_of_matrixes = []
min_of_cols_of_matrixes = []
for i in range(0 , len(list_of_values) , 64):
    matrix = list_of_values[i : i + 64]
    n = 0
    list_of_max_of_cols = []
    list_of_min_of_cols = []
    for j in range(second_length):
        cols_values = [x for x in matrix[n::8]]
        col_max = max(cols_values)
        col_min = min(cols_values)
        list_of_max_of_cols.append(col_max)
        list_of_min_of_cols.append(col_min)
        n += 1
    max_of_cols_of_matrixes.append(list_of_max_of_cols)
    min_of_cols_of_matrixes.append(list_of_min_of_cols)

# get the number of zero and non-zero values on the main diameter of the matrix
zeros_of_main_diameter = []
non_zeros_of_main_diameter = []
for i in range(0 , len(list_of_values) , 64):
    now = list_of_values[i : i + 64]
    main_diameter_values = []
    for j in range(second_length):
        main_values = now[j * 9]
        if main_values == 0:
            main_diameter_values.append(main_values)
    main_diameter_zeros = sum(1 for x in main_diameter_values if x == 0) 
    main_diameter_non_zeros = second_length - main_diameter_zeros
    zeros_of_main_diameter.append(main_diameter_zeros)
    non_zeros_of_main_diameter.append(main_diameter_non_zeros)

# get the number of zero and non-zero values on the minor diameter of the matrix
zeros_of_minor_diameter = []
non_zeros_of_minor_diameter = []
for i in range(0 , len(list_of_values) , 64):
    now = list_of_values[i : i + 64]
    minor_diameter_values = []
    for j in range(second_length):
        minor_values = now[0 + (j + 1) * 7]
        if minor_values == 0 and (0 + (j + 1) * 7) != len(now) - 1:
            minor_diameter_values.append(minor_values)
    minor_diameter_zeros = sum(1 for x in minor_diameter_values if x == 0)
    minor_diameter_non_zeros = second_length - minor_diameter_zeros
    zeros_of_minor_diameter.append(minor_diameter_zeros)
    non_zeros_of_minor_diameter.append(minor_diameter_non_zeros)

# do the ARR algorithm on the matrixes
first_list = []
second_list = []
third_list = []
for i in range(0 ,len(list_of_values) ,64):
    for j in range(i ,i + 64 ,8):
        first_list.append(list_of_values[j : j + 3])
        second_list.append(list_of_values[j + 3 : j + 6])
        third_list.append(list_of_values[j + 6 : j + 8])
first_list_numbers = []
for i in range(0 ,len(first_list) ,8):
    for j in range(i ,i + 8 , 2):
        for k in first_list[j : j + 2]:
            c= sum(1 for x in k if x != 0)
            first_list_numbers.append(c)
second_list_numbers = []
for i in range(0 ,len(second_list) ,8):
    for j in range(i ,i + 8 , 2):
        for k in second_list[j : j + 2]:
            c= sum(1 for x in k if x != 0)
            second_list_numbers.append(c)
third_list_numbers = []
for i in range(0 ,len(third_list) ,8):
    for j in range(i ,i + 8 , 2):
        for k in third_list[j : j + 2]:
            c= sum(1 for x in k if x != 0)
            third_list_numbers.append(c)

        