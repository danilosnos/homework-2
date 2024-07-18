atoms = {
    'H': 1.008,
    'O': 15.999,
    'S': 32.066,
    'Na': 22.990,
    'Cl': 35.453,
    'K': 39.098,
    'H2': 2.016,
    'O4': 63.996
}

molecules = ['H2-S-O4', 'H2-O', 'Na-Cl', 'H-Cl', 'K-Cl']

def calculate_molar_mass(molecule):
    elements = molecule.split('-')
    total_mass = sum([atoms[element] for element in elements])
    return round(total_mass, 3)

molecules.sort(key=lambda x: calculate_molar_mass(x))

for molecule in molecules:
    print(f'{molecule.replace("-", ""):8} {calculate_molar_mass(molecule)}')