import re

class Claim:
    def __init__ (self, claimid, xcoord, ycoord, width, height):
        self.id = int(claimid)
        self.coords = [int(xcoord), int(ycoord)]
        self.width = int(width)
        self.height = int(height)

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

fabric = [[''] * 1000 for i in range(1000)]
overlap_count = 0
non_overlapping_claim = [];

for claim in claims:
    for x in range(claim.coords[0], claim.coords[0] + claim.width):
        for y in range(claim.coords[1], claim.coords[1] + claim.height):
            if fabric[x][y] == 'x':
                fabric[x][y] = 'X'
                overlap_count += 1
            elif fabric[x][y] == '':
                fabric[x][y] = 'x'

for claim in claims:
    overlaps = False
    for x in range(claim.coords[0], claim.coords[0] + claim.width):
        for y in range(claim.coords[1], claim.coords[1] + claim.height):
            if fabric[x][y] == 'X':
                overlaps = True

    if overlaps is False:
        non_overlapping_claim.append(claim)


print('Overlap:', overlap_count, 'squared inches')
print('Claim number',non_overlapping_claim, 'doesn\'t overlap')
