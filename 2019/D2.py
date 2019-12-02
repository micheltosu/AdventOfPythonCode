opcodes = open("D2-input.txt").read().strip().split(',')
for i in range(len(opcodes)):
    opcodes[i] = int(opcodes[i])

def copy_memory():
    global opcodes
    res = opcodes.copy() 
    return res

memory = copy_memory()
print(memory)

#program loop
PC = 0
def forward():
    global PC 
    PC += 4
def run_program(a1, a2):
    global PC 
    global memory
    PC = 0
    memory[1] = a1
    memory[2] = a2

    while True:
        if memory[PC] == 99:
            print("End program")
            return memory[0]
        a1, a2, a3 = memory[PC+1:PC+4]

        if memory[PC] == 1:
            print("Opcode 1")
            memory[a3] = memory[a1] + memory[a2]
        elif memory[PC] == 2:
            print("Opcode 2")
            memory[a3] = memory[a1] * memory[a2]
        forward()


run_program(12,2)

out = 0
# Task 2
for i in range(len(opcodes) - 1):
    for j in range(len(opcodes) - 1):
        print('Run with {0}, {1}'.format(i, j))
        memory = copy_memory()
        out = run_program(i, j)

        if out == 19690720:
            print('verb: {0}, noun: {1}'.format(i, j))
            break
    if out == 19690720:
        break

