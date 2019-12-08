import io

# Read the input for the day
opcodes = open("D7-input.txt").read().strip().split(',')
for i in range(len(opcodes)):
    opcodes[i] = int(opcodes[i])
class Computer:
    class NoMoreSteps(Exception):
        pass
    class NoInput(Exception):
        pass


    memory = None
    PC = 0
    read_pos = 0
    in_stream = None
    out_stream = None

    def __init__(self, int_array = None):
        if int_array is not None:
            self.copy_memory(int_array)
            self.in_stream = io.StringIO()
            self.out_stream = io.StringIO()

    ###################################
    #                                 #
    #    Computer helper functions    #
    #                                 #
    ###################################

    # Function that returns a fresh copy of the program from 'disk'
    def copy_memory(self, int_array):
        self.memory = int_array.copy()

    def parse_param_modes(self, opcode):
        digits = [int(i) for i in str(opcode)]
        digits = digits[:-2]

        while len(digits) < 3:
            digits.insert(0,0)
        return digits

    def parse_opcode(self, opcode):
        split_code = [int(i) for i in str(opcode)]
        if len(split_code) == 1:
            return opcode
        else:
            return split_code[-1]

    def get_param(self, param, mode, memory):
        return param if mode == 1 else memory[param]

    def set_in_stream(self, in_stream = None):
        self.in_stream = in_stream

    def set_out_stream(self, out_stream = None):
        self.out_stream = out_stream


    ###############################
    #                             #
    #    Computer instructions    # 
    #                             #
    ###############################
    def add(self, memory, a1, a2, a3, pmode):
        arg1 = self.get_param(a1, pmode[-1], memory)
        arg2 = self.get_param(a2, pmode[-2], memory)
        memory[a3] = arg1 + arg2

    def mul(self, memory, a1, a2, a3, pmode):
        arg1 = self.get_param(a1, pmode[-1], memory)
        arg2 = self.get_param(a2, pmode[-2], memory)
        memory[a3] = arg1 * arg2

    def get_value(self, memory, a1, pmode):
        val = int(input("Enter input:"))
        memory[a1] = val

    def output_value(self, memory, a1, pmode):
        value = self.get_param(a1, pmode[-1], memory)

    def jump_if_true(self, memory, a1, a2, pmode):
        condition = self.get_param(a1, pmode[-1], memory)
        if condition != 0:
            return self.get_param(a2, pmode[-2], memory)
        else:
            return 0

    def jump_if_false(self, memory, a1, a2, pmode):
        condition = self.get_param(a1, pmode[-1], memory)
        if condition == 0:
            return self.get_param(a2, pmode[-2], memory)
        else:
            return 0

    def less_than(self, memory, a1, a2, a3, pmode):
        arg1 = self.get_param(a1, pmode[-1], memory)
        arg2 = self.get_param(a2, pmode[-2], memory)
        if (arg1 < arg2):
            memory[a3] = 1
        else:
            memory[a3] = 0

    def equals(self, memory, a1, a2, a3, pmode):
        arg1 = self.get_param(a1, pmode[-1], memory)
        arg2 = self.get_param(a2, pmode[-2], memory)
        if (arg1 == arg2):
            memory[a3] = 1
        else:
            memory[a3] = 0

    def get_value_stream(self, memory, a1, stream, read_pos):
        inpt = stream.getvalue().strip().split('\n')
        if (read_pos >= len(inpt)):
            raise Computer.NoInput('novalue')

        val = inpt[read_pos]
        if val != '' and val != '\n':
            memory[a1] = int(val)
        else:
            raise Computer.NoInput('no value')


    def output_value_stream(self, memory, a1, pmode, stream):
        stream.write(str(self.get_param(a1, pmode[-1], memory)) + '\n')

    ###########################
    #                         #
    #     Run program lopp    #
    #                         #
    ###########################

    def __perform_cycle__(self):
        memory = self.memory
        i = ''.join(self.in_stream.getvalue().split('\n'))
        o = ''.join(self.out_stream.getvalue().split('\n'))

        p_modes = self.parse_param_modes(memory[self.PC]) 
        opcode = self.parse_opcode(memory[self.PC])
        # Load the arguments

        if opcode == 99:
            print("Should exit")
            raise Computer.NoMoreSteps('At program end')

        elif opcode == 1:
            a1, a2, a3 = memory[self.PC+1:self.PC+4]
            self.add(memory, a1, a2, a3, p_modes)
            self.PC += 4
        elif opcode == 2:
            a1, a2, a3 = memory[self.PC+1:self.PC+4]
            self.mul(memory, a1, a2, a3, p_modes)
            self.PC += 4
        elif opcode == 3:
            a1 = memory[self.PC+1]
            try:
                self.get_value_stream(memory, a1, self.in_stream, self.read_pos)
                self.read_pos += 1
                self.PC += 2
            except Computer.NoInput:
                return
        elif opcode == 4:
            a1 = memory[self.PC+1]
            self.output_value_stream(memory, a1, p_modes, self.out_stream)
            self.PC += 2
        elif opcode == 5:
            a1, a2, a3 = memory[self.PC+1:self.PC+4]
            res = self.jump_if_true(memory, a1, a2, p_modes)
            if res != 0:
                self.PC = res
            else:
                self.PC += 3
        elif opcode == 6:
            a1, a2, a3 = memory[self.PC+1:self.PC+4]
            res = self.jump_if_false(memory, a1, a2, p_modes)
            if res != 0:
                self.PC = res
            else:
                self.PC += 3
        elif opcode == 7:
            a1, a2, a3 = memory[self.PC+1:self.PC+4]
            self.less_than(memory, a1, a2, a3, p_modes)
            self.PC += 4
        elif opcode == 8:
            a1, a2, a3 = memory[self.PC+1:self.PC+4]
            self.equals(memory, a1, a2, a3, p_modes)
            self.PC += 4
        else:
            raise Computer.NoMoreSteps('At program end')

    def step(self):
        self.__perform_cycle__()

    # Runs the program from start to end
    def run_program(self, *args):

        arg_arr = [str(args[i]) for i in range(len(args))]
        self.in_stream.write('\n'.join(arg_arr))
        

        while self.memory[self.PC] != 99:
            self.__perform_cycle__()

        if (len(self.out_stream.getvalue()) == 0):
            return self.memory[0]
        else:
            return int(self.out_stream.getvalue())

#Task 1
import itertools
def phase_test():
    signals = list()
    phases = list(itertools.permutations([4,3,2,1,0]))
    for phase in phases:
        signal = 0
        for p in range(5):
            computer = Computer(opcodes)
            computer.copy_memory(opcodes)
            signal = computer.run_program(phase[p], signal)
            print("Signal: ", signal)
        signals.append(signal)

    return max(signals)
#print(phase_test())

# Task 2
def feedback_test():
    signals = list()
    phases = list(itertools.permutations([9,8,7,6,5]))

    for phase in phases:
        streams = [io.StringIO() for _ in range(5)]
        computers = [Computer(opcodes) for _ in range(5)]
        for p in range(5):
            print ('Setup stream {0} with phase {1}'.format(p, phase[p]))
            streams[p].write(str(phase[p]) + '\n')
            if p == 4:
                streams[p].write(str(0) + '\n')

        for com in range(5):
            in_stream = (com + 4) % 5
            computers[com].set_in_stream(streams[in_stream])
            computers[com].set_out_stream(streams[com])


        running_computers = computers.copy()
        running = 5
        while running > 0:
            for c in running_computers:
                try:
                    c.step()
                except Computer.NoMoreSteps:
                    running_computers.remove(c)
                    running -= 1

        print("Done.")
        


        out_arr = streams[4].getvalue().strip().split('\n')
        out_val = out_arr[len(out_arr) - 1]
        signals.append(int(out_val))

    return max(signals)

print(feedback_test())



