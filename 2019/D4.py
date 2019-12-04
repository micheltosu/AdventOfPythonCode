start = 109165
stop = 576723

#
# The constraint created in part 2 really just meant that
# there HAS to be a group of two numbers. Any other group
# is fine as long as the group of 2 is there. And also 
# there must not be no group at all.
#
def has_group_of_two(tup):
    group_count = 0
    groups = dict()
    # First loop and create the groups
    for i in range(5):
        if tup[i] == tup[i+1]:
            if group_count == 0:
                group_count = 2
            else:
                group_count += 1 
            groups[tup[i]] = group_count
        else:
            group_count = 0

    # Loop through the groups.
    for group in groups:
        if groups[group] == 2:
            # Group of two were found.
            return True

    # If there was no group or no group of 2
    return False

# One digit cannot be lower than the digit before. 
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
    if never_decreasing(num_arr) and has_group_of_two(num_arr):
        count += 1

print("There are {0} numbers".format(count))
