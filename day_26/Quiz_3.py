with open('./day_26/file1.txt', 'r') as first_file:
    first_file_ns = first_file.readlines()

with open('./day_26/file2.txt', 'r') as second_file:
    second_file_ns = second_file.readlines()

result = [int(n) for n in first_file_ns if n in second_file_ns]
print(result)