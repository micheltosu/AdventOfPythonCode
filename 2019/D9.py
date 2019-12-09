import Computer
input_array = open('D9-input.txt').read().strip().split(',')
for i in range(len(input_array)):
    input_array[i] = int(input_array[i])



com = Computer.Computer([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99])
com2 = Computer.Computer([1102,34915192,34915192,7,4,7,99,0])
com3 = Computer.Computer([104,1125899906842624,99])
task1 = Computer.Computer(input_array)
com.run_program()
print(com.get_out_stream().getvalue())

print(com2.run_program())
print(com3.run_program())

print(task1.run_program())
