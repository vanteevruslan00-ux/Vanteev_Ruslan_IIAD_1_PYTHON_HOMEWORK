# Вантеев Руслан ИИАД_1
nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]


flat_list = [num for block in nice_list for row in block for num in row]

print(flat_list)
