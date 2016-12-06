"""
Check if the String for a chemical reaction is balanced and return the according boolean

2 H2 + O2 -> 2 H2O
true

NaCl + AgNO3 -> NaNO3 + Ag
false
"""
import re

reactantsd = {}
productsd = {}


def is_balanced(str_input):
    reactants = str_input.split("->")[0].strip(" ")
    products = str_input.split("->")[1].strip(" ")
    reactant_molecules = reactants.split("+")
    products_molecules = products.split("+")

    for r in reactant_molecules:
        for key, val in parse_molecule(r).iteritems():
            if key not in reactantsd:
                reactantsd[key] = val;
            else:
                reactantsd[key] = reactantsd[key] + val

    for p in products_molecules:
        for key, val in parse_molecule(p).iteritems():
            if key not in productsd:
                productsd[key] = val;
            else:
                productsd[key] = productsd[key] + val

    print (reactantsd)
    print (productsd)

    return (reactantsd == productsd)

def parse_molecule(str_input):
    molec_data = {}
    molec = str_input.strip(" ")
    coefficent = molec.split(" ")

    if len(coefficent) == 2:
        coefficent = coefficent[0]
    else:
        coefficent = 1

    mole_parse = re.findall(r'([A-Z][a-z]*)(\d*)', molec)

    for each in mole_parse:
        if each[1] == '':
            molec_data[each[0]] = int(coefficent)
        else:
            molec_data[each[0]] = int(each[1]) * int(coefficent)

    return (molec_data)

def main():
    rxn = "2 H2 + O2 -> 2 H2O"
    print(is_balanced(rxn))

    reaction = "NaCl + AgNO3 -> NaNO3 + Ag"
    print(is_balanced(reaction))

main()