import io
class Computer:
    class NoMoreSteps(Exception):
        pass
    class NoInput(Exception):
        pass


    memory = None
    PC = 0
    read_pos = 0
    relative_base = 0
    in_stream = None
    out_stream = None
    in_stream_set = False

    def __init__(self, int_array = None):
        if int_array is not None:
            self.copy_memory(int_array)
            self.out_stream = io.StringIO()
            self.in_stream = io.StringIO()

    ###################################
    #                                 #
    #    Computer helper functions    #
    #                                 #
    ###################################

    # Function that returns a fresh copy of the program from 'disk'
    def copy_memory(self, int_array):
        self.memory = int_array.copy()
        self.memory.extend([0 for _ in range(len(self.memory) * 10)])

    def parse_param_modes(self, opcode):
        digits = [int(i) for i in str(opcode)]
        digits = digits[:-2]

        while len(digits) < 3:
            digits.insert(0,0)
        return digits

    def parse_opcode(self, opcode):
        split_code = [int(i) for i in str(opcode)]
        if len(split_code) == 1:
            return int(opcode)
        else:
            code = int(''.join([str(i) for i in split_code[-2:]]))
            return code

    def set_in_stream(self, in_stream = None):
        self.in_stream = in_stream
        self.in_stream_set = True

    def set_out_stream(self, out_stream = None):
        self.out_stream = out_stream

    def get_out_stream(self):
        return self.out_stream

    def get_memval(self, location, mode):
        #print('get_memval: loc, mode', location, mode)
        if location < 0 and mode == 0:
            raise Exception('No negative memory locations')

        if mode == 0:
            return self.memory[location]
        elif mode == 1:
            return location
        elif mode == 2:
            return self.memory[location + self.relative_base]
    def set_memval(self, location, mode, value):
        #print('set memval: loc, mode, valu ', location, mode, value)
        if location < 0 and mode != 2:
            raise Exception('No negative memory locations')

        if mode == 0:
            self.memory[location] = value
        elif mode == 2:
            self.memory[location + self.relative_base] = value
        else:
            raise Exception('Unrecognized memory mode for write')


    def set_relative_base(self, val):
        self.relative_base += val



    ###############################
    #                             #
    #    Computer instructions    # 
    #                             #
    ###############################
    def add(self, a1, a2, a3, pmode):
        arg1 = self.get_memval(a1, pmode[-1])
        arg2 = self.get_memval(a2, pmode[-2])
        self.set_memval(a3, pmode[-3], arg1 + arg2)

    def mul(self, a1, a2, a3, pmode):
        arg1 = self.get_memval(a1, pmode[-1])
        arg2 = self.get_memval(a2, pmode[-2])
        self.set_memval(a3, pmode[-3], arg1 * arg2)

    def get_value(self, a1, pmode):
        val = int(input("Enter input:"))
        self.set_memval(a1, pmode[-1], val)

    def jump_if_true(self, a1, a2, pmode):
        condition = self.get_memval(a1, pmode[-1])
        if condition != 0:
            return self.get_memval(a2, pmode[-2])
        else:
            return -1

    def jump_if_false(self, a1, a2, pmode):
        condition = self.get_memval(a1, pmode[-1])
        if condition == 0:
            return self.get_memval(a2, pmode[-2])
        else:
            return -1

    def less_than(self, a1, a2, a3, pmode):
        arg1 = self.get_memval(a1, pmode[-1])
        arg2 = self.get_memval(a2, pmode[-2])
        if (arg1 < arg2):
            self.set_memval(a3, pmode[-3], 1)
        else:
            self.set_memval(a3, pmode[-3], 0)

    def equals(self, a1, a2, a3, pmode):
        arg1 = self.get_memval(a1, pmode[-1])
        arg2 = self.get_memval(a2, pmode[-2])
        if (arg1 == arg2):
            self.set_memval(a3, pmode[-3], 1)
        else:
            self.set_memval(a3, pmode[-3], 0)

    def get_value_stream(self, a1, stream, read_pos):
        inpt = stream.getvalue().strip().split('\n')
        if (read_pos >= len(inpt)):
            raise Computer.NoInput('novalue')

        val = inpt[read_pos]
        if val != '' and val != '\n':
            self.set_memval(a1, 0, int(val))
        else:
            raise Computer.NoInput('no value')


    def output_value_stream(self, a1, pmode, stream):
        stream.write(str(self.get_memval(a1, pmode[-1])) + '\n')

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
            raise Computer.NoMoreSteps('At program end')

        elif opcode == 1: # Add
            a1, a2, a3 = memory[self.PC+1:self.PC+4]
            self.add(a1, a2, a3, p_modes)
            self.PC += 4
        elif opcode == 2:
            a1, a2, a3 = memory[self.PC+1:self.PC+4]
            self.mul(a1, a2, a3, p_modes)
            self.PC += 4
        elif opcode == 3: # Get input from stream
            a1 = memory[self.PC+1]
            try:
                if self.in_stream_set is False:
                    self.get_value(a1, p_modes)
                else:
                    self.get_value_stream(a1, self.in_stream, self.read_pos)
                    self.read_pos += 1
                self.PC += 2
            except Computer.NoInput:
                return
        elif opcode == 4: # Print to stream
            a1 = memory[self.PC+1]
            self.output_value_stream(a1, p_modes, self.out_stream)
            self.PC += 2
        elif opcode == 5:
            a1, a2, a3 = memory[self.PC+1:self.PC+4]
            res = self.jump_if_true(a1, a2, p_modes)
            if res != -1:
                self.PC = res
            else:
                self.PC += 3
        elif opcode == 6: # Jump if false
            a1, a2, a3 = memory[self.PC+1:self.PC+4]
            res = self.jump_if_false(a1, a2, p_modes)
            if res != -1:
                self.PC = res
            else:
                self.PC += 3
        elif opcode == 7:
            a1, a2, a3 = memory[self.PC+1:self.PC+4]
            self.less_than(a1, a2, a3, p_modes)
            self.PC += 4
        elif opcode == 8: # Check if equals
            a1, a2, a3 = memory[self.PC+1:self.PC+4]
            self.equals(a1, a2, a3, p_modes)
            self.PC += 4
        elif opcode == 9:
            a1 = memory[self.PC+1]
            param = self.get_memval(a1, p_modes[-1])
            self.set_relative_base(param)
            self.PC += 2
        else:
            raise Exception('Unknown opcode: ', opcode)

    def step(self):
        self.__perform_cycle__()

    # Runs the program from start to end
    def run_program(self, *args):

        arg_arr = [str(args[i]) for i in range(len(args))]
        self.in_stream.write('\n'.join(arg_arr))
        

        while self.memory[self.PC] != 99:
            try:
                self.__perform_cycle__()
            except Computer.NoMoreSteps:
                print('Program finished')
                break

        if (len(self.out_stream.getvalue()) == 0):
            return self.memory[0]
        else:
            return self.out_stream.getvalue()
