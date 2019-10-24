# This is a script for solving challange 2 day 1 of 2018 Advent of Code
try: 
    inputFile = open('input1-1.txt')
except IOError:
    print('Could not read file input1-1.txt')
else:
    frequency = 0
    frequencyChanges = list()
    frequencyHistory = set()

    for freq in inputFile:
        try:
            change = int(freq)
        except ValueError:
            print('Skipping line containing: ', repr(freq))
        else:
            frequencyChanges.append(change)
            frequency += change
            frequencyHistory.add(frequency)

    inputFile.close()
    print('Read all the frequencies, scanning for repeating...')
    print('The frequency after first lap is: ', frequency)

    foundRepeating = False

    while not foundRepeating:
        for change in frequencyChanges:
            frequency += change
            if frequency not in frequencyHistory:
                frequencyHistory.add(frequency)
            else:
                print('Found repeating frequency: ', frequency)
                foundRepeating = True
                break
