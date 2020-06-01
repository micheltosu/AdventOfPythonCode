import re

input_arr = open('D14-test.txt').read().strip().split('\n')


class Reaction:
    required_materials = list()
    produced_material = None

    def __init__(self, produced, required):
        self.required_materials = required
        self.produced_material = produced
        print(self)

    def __str__(self):
        return 'produces: {0}, required: {1}'.format(self.produced_material, self.required_materials)

    def __repr__(self):
        return 'produces: {0}, required: {1}'.format(self.produced_material, self.required_materials)  

class MaterialQuantity:
    material = None
    quantity = 0

    def __init__(self, material, quantity):
        self.material = material
        self.quantity = quantity

    def __str__(self):
        return '{0} of {1}'.format(self.quantity, self.material)
    
    def __repr__(self):
        return '{0} of {1}'.format(self.quantity, self.material)

class MaterialsCollection:
    quantities = dict()

    def add_quantity(self, material_quantity):
        mat = material_quantity.material
        if mat in self.quantities:
            self.quantities[mat] += material_quantity.quantity
        else:
            self.quantities[mat] = material_quantity.quantity

class Material:
    name = None

    def __init__(self, name):
        self.name = str(name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __hash__(self):
        return self.name.__hash__()


class Factory:
    reactions = dict()

    def add_reaction(self, reaction):
        print('Reaction for {0} added typeof {1}.'
        .format(reaction.produced_material.material, type(reaction.produced_material.material)))
        self.reactions[reaction.produced_material.material] = reaction

    def get_material_parts(self, material):
        return self.reactions[material]

    def __str__(self):
        return 'Factory knows: \n' + '\n'.join([str(self.reactions[r]) for r in self.reactions])


factory = Factory()

for react_string in input_arr:
    req, prod = react_string.split('=>')

    req_list = list()
    for material in req.split(','):
        quant, desc = re.search(r'(\d+)\s(\w+)', material).groups()
        material = Material(desc)
        req_list.append(MaterialQuantity(material, quant))
     
    produced_match = re.search(r'(\d+)\s(\w+)', prod).groups()
    produced_material = MaterialQuantity(Material(produced_match[1]), produced_match[0])
    reaction = Reaction(produced_material, req_list)
    factory.add_reaction(reaction)

print(factory)

# Task 1 - figure out how many ORE is needed
print(factory.get_material_parts(Material('B')))