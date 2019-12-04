start = 109165
stop = 576723

def contains_duplicates(tup):
    for i in range(5):
        if tup[i] == tup[i+1]:
            return True
    return False

def not_just_large_group(tup):
    group_num = None
    group_count = 0
    groups = dict()
    for i in range(5):
        if tup[i] == tup[i+1]:
            if group_count == 0:
                group_count = 2
            else:
                group_count += 1 
            groups[tup[i]] = group_count
        else:
            group_count = 0
                
    if len(groups) > 1:
        for group in groups:
            if groups[group] == 2:
                return True
        return False
    elif len(groups) == 1:
        for group in groups:
            if groups[group] >= 3:
                return False
    return True

def never_decreasing(tup):
    last_digit = tup[0]
    for i in range(1,6):
        if tup[i] < last_digit:
            return False
        else:
            last_digit = tup[i]
    return True

count = 0
for i in range(start,stop):
    num_arr = [int(j) for j in str(i)]
    if (contains_duplicates(num_arr)
            and never_decreasing(num_arr)
            and not_just_large_group(num_arr)):
        count += 1

print("There are {0} numbers".format(count))
