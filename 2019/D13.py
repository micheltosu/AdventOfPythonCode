import Computer 
program = open('D13-input.txt').read().strip().split(',')
for i in range(len(program)):
    program[i] = int(program[i])

comp = Computer.Computer(program)

print(comp.run_program(interactive=True))
