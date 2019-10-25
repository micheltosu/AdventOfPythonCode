import checksum

box_ids = checksum.read_input_to_array("input.txt")

for s1 in box_ids:
    if s1 == '':
        continue

    for s2 in box_ids:
        if s2 == '':
            continue
        elif s1 is s2:
            continue

        same_letters = list()
        try:
            for i in range(0, len(s1)):
                if s1[i] == s2[i]:
                    same_letters.append(s1[i])

            if len(same_letters) == (len(s1) - 1):
                print('String', s1, 'and', s2, 'differs in one character. \nCharacters:', ''.join(same_letters), 'are the same.')
        except IndexError:
            print('Error comparng two strings:', repr(s1), repr(s2))





