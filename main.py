"""
Nested List
"""

# for list in nested_list:
#     for num in list:
#         print(num)

# nested_list = [[j for j in range(1, 4)] for i in range(1, 4)]

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat_list = [item for row in nested_list for item in row]

print(nested_list)
print(flat_list)
