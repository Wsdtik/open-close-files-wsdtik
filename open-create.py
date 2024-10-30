files_to_process = ['1.txt', '2.txt', '3.txt'] 

file_info = []


for file_name in files_to_process:
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        line_count = len(lines)
        file_info.append((file_name, line_count, lines))


file_info.sort(key=lambda x: x[1])


result_file_name = 'result.txt'


with open(result_file_name, 'w', encoding='utf-8') as result_file:
    for file_name, line_count, lines in file_info:
        
        result_file.write(f'{file_name}n{line_count}n')
        
        result_file.writelines(lines)
