def read_input_to_array(path):
    input_file = open(path)
    input_arr = input_file.read().split('\n')
    input_file.close()

    if input_arr[len(input_arr) - 1] is '\n':
        input_arr.pop()

    return input_arr

def checksum(array):
    strings_with_duplicates = 0 
    strings_with_triplets = 0

    for string in array:
        character_map = dict()
        doubles = 0
        triplets = 0

        for char in string:
            if char in character_map:
                character_map[char] += 1
            elif char not in character_map:
                character_map[char] = 1

        for char in character_map:
            if character_map[char] is 3:
                triplets = 1
            elif character_map[char] is 2:
                doubles = 1

        strings_with_triplets += triplets
        strings_with_duplicates += doubles

    return strings_with_duplicates * strings_with_triplets


print('The checksum is:',checksum(read_input_to_array('input.txt')))
