modules = open('D1-Input.txt').read().strip().split('\n')

print(modules)
total_fuel=0
for module in modules:
    module_fuel = 0

    weight = module
    fuel = (int(module)// 3) - 2
    while fuel > 0:
        module_fuel += fuel
        weight = fuel
        fuel = (int(weight)// 3) - 2

    total_fuel += module_fuel



print(total_fuel)
