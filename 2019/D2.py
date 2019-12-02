# Read the input for the day
opcodes = open("D2-input.txt").read().strip().split(',')
for i in range(len(opcodes)):
    opcodes[i] = int(opcodes[i])

# Function that returns a fresh copy of the program from 'disk'
def copy_memory():
    global opcodes
    res = opcodes.copy() 
    return res

PC = 0
# Procedure to increment program counter to next instruction
def forward():
    global PC 
    PC += 4

# Runs the program given by copy_memory
def run_program(a1, a2):
    global PC 
    memory = copy_memory()
    PC = 0
    memory[1] = a1
    memory[2] = a2

    while memory[PC] != 99:
        # Load the arguments
        a1, a2, a3 = memory[PC+1:PC+4]

        if memory[PC] == 1:
            memory[a3] = memory[a1] + memory[a2]
        elif memory[PC] == 2:
            memory[a3] = memory[a1] * memory[a2]
        forward()

    return memory[0]

#Task 1
print('The result for verb 12, noun 2: ', run_program(12,2))

# Task 2
print('Finding out which verb and noun gives 19690720')
out = 0
for i in range(len(opcodes) - 1):
    for j in range(len(opcodes) - 1):
        memory = copy_memory()
        out = run_program(i, j)

        if out == 19690720:
            print('verb: {0}, noun: {1}'.format(i, j))
            break
    if out == 19690720:
        break

