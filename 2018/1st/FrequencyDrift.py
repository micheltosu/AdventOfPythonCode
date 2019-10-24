# This is a script for solving challange 1 day 1 of 2018 Advent of Code
try: 
    inputFile = open("input1-1.txt")

    frequency = 0

    for freq in inputFile:
        if freq.startswith('+'):
            frequency += int(freq.lstrip('+'))
        elif freq.startswith('-'):
            frequency -= int(freq.lstrip('-'))

    print 'The frequency you need is: ', frequency
    inputFile.close()

except IOError:
    print 'Could not read file input1-1.txt'

