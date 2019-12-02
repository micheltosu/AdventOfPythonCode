opcodes = open("D2-input.txt").read().strip().split(',')
for i in range(len(opcodes)):
    opcodes[i] = int(opcodes[i])
print(opcodes)


#program loop
opcodes[1] = 12
opcodes[2] = 2
PC = 0
def forward():
    global PC 
    PC += 4

while True:
    a1, a2, a3 = opcodes[PC+1:PC+4]
    if opcodes[PC] == 1:
        print("Opcode 1")
        opcodes[a3] = opcodes[a1] + opcodes[a2]
    elif opcodes[PC] == 2:
        print("Opcode 2")
        opcodes[a3] = opcodes[a1] * opcodes[a2]
    elif opcodes[PC] == 99:
        print("End program")
        break

    forward()
print("Position 0:{0}".format(opcodes[0]))
