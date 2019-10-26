import re

class Claim:
    def __init__ (self, claimid, xcoord, ycoord, width, height):
        self.id = claimid
        self.coords = [xcoord, ycoord]
        self.width = width
        self.height = height

    def __repr__(self):
        return "#{0} @{1},{2}: {3}x{4}".format(self.id,self.coords[0],self.coords[1],self.width, self.height)


def read_claims():
    input_arr = open('input.txt').read().split('\n')
    claims_list = list()

    if input_arr[len(input_arr)-1] == '':
        input_arr.pop()

    for row in input_arr:
        match = re.search(
                r'#(\d*).@.(\d{1,3}),(\d{1,3}):.(\d{1,3})x(\d{1,3})', row)

        values = match.groups()
        claims_list.append(Claim(*values))

    return claims_list


        
claims = read_claims()



