modules = open('D1-Input.txt').read().strip().split('\n')
# The formula for the fuel needed for a mass.
def fuel_for_mass(mass):
    return ( mass // 3) - 2

# Task 1 - calculate fuel for each module of the spacecraft
total_fuel=0
for module in modules:
    total_fuel += fuel_for_mass(int(module))

print('Fuel needed is {0}'.format(total_fuel))

# Task 2 - The total amount of fuel will have to include fuel to 
#   make up for the fuel. The rule is that when the fuel requirement
#   for a mass is 0 of negative we can just 'wish' really hard to 
#   create lift.
corrected_fuel = 0
for module in modules:
    module_fuel = 0

    fuel = fuel_for_mass(int(module))
    while fuel > 0:
        module_fuel += fuel
        fuel = fuel_for_mass(fuel)

    corrected_fuel += module_fuel


print('Including fuel weight the needed fuel is {0}'.format(corrected_fuel))
