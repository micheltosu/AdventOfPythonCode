import io

# Read the input for the day
opcodes = open("D7-input.txt").read().strip().split(',')
for i in range(len(opcodes)):
    opcodes[i] = int(opcodes[i])
class Computer:
    memory = None
    PC = 0
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
        print(value)

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
        streampos = stream.tell()
        stream.seek(read_pos)
        val = stream.readline()
        if val != '':
            memory[a1] = int(val)

        stream.seek(streampos)

    def output_value_stream(self, memory, a1, pmode, stream):
        stream.write(str(self.get_param(a1, pmode[-1], memory)) + '\n')

    ###########################
    #                         #
    #     Run program lopp    #
    #                         #
    ###########################

    # Runs the program from start to end
    def run_program(self, *args):
        memory = self.memory

        arg_arr = [str(args[i]) for i in range(len(args))]
        self.in_stream.write('\n'.join(arg_arr))
        
        read_pos = 0

        while memory[self.PC] != 99:
            p_modes = self.parse_param_modes(memory[self.PC]) 
            opcode = self.parse_opcode(memory[self.PC])
            # Load the arguments
            a1, a2, a3 = memory[self.PC+1:self.PC+4]

            if opcode == 1:
                self.add(memory, a1, a2, a3, p_modes)
                self.PC += 4
            elif opcode == 2:
                self.mul(memory, a1, a2, a3, p_modes)
                self.PC += 4
            elif opcode == 3:
                self.get_value_stream(memory, a1, self.in_stream, read_pos)
                read_pos+=2
                print("read {0} from in stream".format(memory[a1]))
                self.PC += 2
            elif opcode == 4:
                print("put {0} in out stream".format(memory[a1]))
                self.output_value_stream(memory, a1, p_modes, self.out_stream)
                self.PC += 2
            elif opcode == 5:
                res = self.jump_if_true(memory, a1, a2, p_modes)
                if res != 0:
                    self.PC = res
                else:
                    self.PC += 3
            elif opcode == 6:
                res = self.jump_if_false(memory, a1, a2, p_modes)
                if res != 0:
                    self.PC = res
                else:
                    self.PC += 3
            elif opcode == 7:
                self.less_than(memory, a1, a2, a3, p_modes)
                self.PC += 4
            elif opcode == 8:
                self.equals(memory, a1, a2, a3, p_modes)
                self.PC += 4

        if (len(self.out_stream.getvalue()) == 0):
            return memory[0]
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
print(phase_test())

# Task 2
def feedback_test():
    signals = list()
    phases = list(itertools.permutations([9,8,7,6,5]))

    for phase in phases:
        streams = [io.StringIO() for _ in range(5)]
        for p in range(5):
            print ('Setup stream {0} with phase {1}'.format(p, phase[p]))
            streams[p].write(str(phase[p]) + '\n')
            if p == 4:
                streams[p].write(str(0) + '\n')
        for p in range(5):
            in_stream = (p + 4) % 5
            signal = run_program(streams[in_stream], streams[p])
        streams[4].seek(streams[4].tell() - 2)
        output = streams[4].readline()
        signals.append(int(output))

    return max(signals)
in_stream = io.StringIO()
in_stream.write('\n'.join(str(x) for x in [9,0]))
out_stream = io.StringIO()
run_program(in_stream, out_stream)
print(out_stream.getvalue())

feedback_test()



