# Read the input for the day
opcodes = open("D5-input.txt").read().strip().split(',')
for i in range(len(opcodes)):
    opcodes[i] = int(opcodes[i])

###################################
#                                 #
#    Computer helper functions    #
#                                 #
###################################

# Function that returns a fresh copy of the program from 'disk'
def copy_memory():
    global opcodes
    res = opcodes.copy() 
    return res

def parse_param_modes(opcode):
    digits = [int(i) for i in str(opcode)]
    digits = digits[:-2]

    while len(digits) < 3:
        digits.insert(0,0)
    return digits

def parse_opcode(opcode):
    split_code = [int(i) for i in str(opcode)]
    if len(split_code) == 1:
        return opcode
    else:
        return split_code[-1]

def get_param(param, mode, memory):
    return param if mode == 1 else memory[param]

###############################
#                             #
#    Computer instructions    # 
#                             #
###############################
def add(memory, a1, a2, a3, pmode):
    arg1 = get_param(a1, pmode[-1], memory)
    arg2 = get_param(a2, pmode[-2], memory)
    memory[a3] = arg1 + arg2

def mul(memory, a1, a2, a3, pmode):
    arg1 = get_param(a1, pmode[-1], memory)
    arg2 = get_param(a2, pmode[-2], memory)
    memory[a3] = arg1 * arg2

def get_value(memory, a1, pmode):
    val = int(input("Enter input:"))
    memory[a1] = val

def output_value(memory, a1, pmode):
    value = get_param(a1, pmode[-1], memory)
    print(value)

def jump_if_true(memory, a1, a2, pmode):
    condition = get_param(a1, pmode[-1], memory)
    if condition != 0:
        return get_param(a2, pmode[-2], memory)
    else:
        return 0

def jump_if_false(memory, a1, a2, pmode):
    condition = get_param(a1, pmode[-1], memory)
    if condition == 0:
        return get_param(a2, pmode[-2], memory)
    else:
        return 0

def less_than(memory, a1, a2, a3, pmode):
    arg1 = get_param(a1, pmode[-1], memory)
    arg2 = get_param(a2, pmode[-2], memory)
    if (arg1 < arg2):
        memory[a3] = 1
    else:
        memory[a3] = 0

def equals(memory, a1, a2, a3, pmode):
    arg1 = get_param(a1, pmode[-1], memory)
    arg2 = get_param(a2, pmode[-2], memory)
    if (arg1 == arg2):
        memory[a3] = 1
    else:
        memory[a3] = 0

###########################
#                         #
#     Run program lopp    #
#                         #
###########################

PC = 0
# Runs the program given by copy_memory
def run_program(a1 = None, a2 = None):
    global PC 
    memory = copy_memory()
    PC = 0
    if a1 is not None:
        memory[1] = a1
    if a2 is not None:
        memory[2] = a2

    while memory[PC] != 99:
        p_modes = parse_param_modes(memory[PC]) 
        opcode = parse_opcode(memory[PC])
        # Load the arguments
        a1, a2, a3 = memory[PC+1:PC+4]

        if opcode == 1:
            add(memory, a1, a2, a3, p_modes)
            PC += 4
        elif opcode == 2:
            mul(memory, a1, a2, a3, p_modes)
            PC += 4
        elif opcode == 3:
            get_value(memory, a1, p_modes)
            PC += 2
        elif opcode == 4:
            output_value(memory, a1, p_modes)
            PC += 2
        elif opcode == 5:
            res = jump_if_true(memory, a1, a2, p_modes)
            if res != 0:
                PC = res
            else:
                PC += 3
        elif opcode == 6:
            res = jump_if_false(memory, a1, a2, p_modes)
            if res != 0:
                PC = res
            else:
                PC += 3
        elif opcode == 7:
            less_than(memory, a1, a2, a3, p_modes)
            PC += 4
        elif opcode == 8:
            equals(memory, a1, a2, a3, p_modes)
            PC += 4
    return memory[0]

#Task 1
run_program()
