def file_input(file_strings):
    result = file_strings[0]
    del file_strings[0]
    return result


with open('input.txt', 'r') as f:
    file_strings = f.read().splitlines()
while file_strings:
    print(file_input(file_strings))
