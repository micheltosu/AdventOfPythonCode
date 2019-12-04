start = 109165
stop = 576723
def contains_duplicates(tup):
    for i in range(5):
        if tup[i] == tup[i+1]:
            return True
    return False

def never_decreasing(tup):
    last_digit = tup[0]
    for i in range(1,6):
        if tup[i] < last_digit:
            return False
        else:
            last_digit = tup[i]
    return True



count = 0
for i in range (1,6):
    j_stop = 8 if i == 5 else 10
    for j in range (i, j_stop):
        k_stop = 7 if j == 7 else 10
        for k in range (j, k_stop):
            for l in range(k,10):
                for m in range(l,10):
                    for n in range(m,10):
                        if contains_duplicates((i,j,k,l,m,n)):
                            count += 1

print("There are {0} numbers".format(count))
print("---- New attempt ----")
count = 0
for i in range(109165,576723):
    num_arr = [int(j) for j in str(i)]
    if contains_duplicates(num_arr) and never_decreasing(num_arr):
        count += 1

print("There are {0} numbers".format(count))
