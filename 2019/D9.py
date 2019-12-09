import Computer
import io
input_array = open('D9-input.txt').read().strip().split(',')
for i in range(len(input_array)):
    input_array[i] = int(input_array[i])

# Today i used the test-cases. Easier to copy-paste the program code like this instead
# of storing them in files
com = Computer.Computer([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99])
com2 = Computer.Computer([1102,34915192,34915192,7,4,7,99,0])
com3 = Computer.Computer([104,1125899906842624,99])
print(com.run_program())
print(com2.run_program())
print(com3.run_program())
# This is the computer with the real program. Both tasks can be performed interactively.
task1 = Computer.Computer(input_array)
print(task1.run_program())
# Another way would be to do it like this
print(task1.run_program('1', program = input_array, interactive = False))
print(task1.run_program('2', program = input_array, interactive = False))

