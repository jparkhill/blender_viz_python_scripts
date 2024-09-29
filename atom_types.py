import bpy

elements = {
    "H": {
        "atomic_number": 1,
        "vdw_radii": 120,
        "name": "Hydrogen",
        "standard_mass": 1.00794,
    },
    "He": {
        "atomic_number": 2,
        "vdw_radii": 140,
        "name": "Helium",
        "standard_mass": 4.002602,
    },
    "Li": {
        "atomic_number": 3,
        "vdw_radii": 182,
        "name": "Lithium",
        "standard_mass": 6.941,
    },
    "Be": {
        "atomic_number": 4,
        "vdw_radii": 153,
        "name": "Beryllium",
        "standard_mass": 9.012182,
    },
    "B": {
        "atomic_number": 5,
        "vdw_radii": 192,
        "name": "Boron",
        "standard_mass": 10.811,
    },
    "C": {
        "atomic_number": 6,
        "vdw_radii": 170,
        "name": "Carbon",
        "standard_mass": 12.0107,
    },
    "N": {
        "atomic_number": 7,
        "vdw_radii": 155,
        "name": "Nitrogen",
        "standard_mass": 14.0067,
    },
    "O": {
        "atomic_number": 8,
        "vdw_radii": 152,
        "name": "Oxygen",
        "standard_mass": 15.9994,
    },
    "F": {
        "atomic_number": 9,
        "vdw_radii": 147,
        "name": "Fluorine",
        "standard_mass": 18.9984032,
    },
    "Ne": {
        "atomic_number": 10,
        "vdw_radii": 154,
        "name": "Neon",
        "standard_mass": 20.1797,
    },
    "Na": {
        "atomic_number": 11,
        "vdw_radii": 227,
        "name": "Sodium",
        "standard_mass": 22.98977,
    },
    "Mg": {
        "atomic_number": 12,
        "vdw_radii": 173,
        "name": "Magnesium",
        "standard_mass": 24.305,
    },
    "Al": {
        "atomic_number": 13,
        "vdw_radii": 184,
        "name": "Aluminium",
        "standard_mass": 26.981538,
    },
    "Si": {
        "atomic_number": 14,
        "vdw_radii": 210,
        "name": "Silicon",
        "standard_mass": 28.0855,
    },
    "P": {
        "atomic_number": 15,
        "vdw_radii": 180,
        "name": "Phosphorus",
        "standard_mass": 30.973761,
    },
    "S": {
        "atomic_number": 16,
        "vdw_radii": 180,
        "name": "Sulfur",
        "standard_mass": 32.065,
    },
    "Cl": {
        "atomic_number": 17,
        "vdw_radii": 175,
        "name": "Chlorine",
        "standard_mass": 35.453,
    },
    "Ar": {
        "atomic_number": 18,
        "vdw_radii": 188,
        "name": "Argon",
        "standard_mass": 39.948,
    },
    "K": {
        "atomic_number": 19,
        "vdw_radii": 275,
        "name": "Potassium",
        "standard_mass": 39.0983,
    },
    "Ca": {
        "atomic_number": 20,
        "vdw_radii": 231,
        "name": "Calcium",
        "standard_mass": 40.078,
    },
    "Sc": {
        "atomic_number": 21,
        "vdw_radii": 211,
        "name": "Scandium",
        "standard_mass": 44.95591,
    },
    "Ti": {
        "atomic_number": 22,
        "vdw_radii": 147,
        "name": "Titanium",
        "standard_mass": 47.867,
    },
    "V": {
        "atomic_number": 23,
        "vdw_radii": 134,
        "name": "Vanadium",
        "standard_mass": 50.9415,
    },
    "Cr": {
        "atomic_number": 24,
        "vdw_radii": 128,
        "name": "Chromium",
        "standard_mass": 51.9961,
    },
    "Mn": {
        "atomic_number": 25,
        "vdw_radii": 127,
        "name": "Manganese",
        "standard_mass": 54.938049,
    },
    "Fe": {
        "atomic_number": 26,
        "vdw_radii": 126,
        "name": "Iron",
        "standard_mass": 55.845,
    },
    "Co": {
        "atomic_number": 27,
        "vdw_radii": 125,
        "name": "Cobalt",
        "standard_mass": 58.9332,
    },
    "Ni": {
        "atomic_number": 28,
        "vdw_radii": 163,
        "name": "Nickel",
        "standard_mass": 58.6934,
    },
    "Cu": {
        "atomic_number": 29,
        "vdw_radii": 140,
        "name": "Copper",
        "standard_mass": 63.546,
    },
    "Zn": {
        "atomic_number": 30,
        "vdw_radii": 139,
        "name": "Zinc",
        "standard_mass": 65.409,
    },
    "Ga": {
        "atomic_number": 31,
        "vdw_radii": 187,
        "name": "Gallium",
        "standard_mass": 69.723,
    },
    "Ge": {
        "atomic_number": 32,
        "vdw_radii": 211,
        "name": "Germanium",
        "standard_mass": 72.64,
    },
    "As": {
        "atomic_number": 33,
        "vdw_radii": 185,
        "name": "Arsenic",
        "standard_mass": 74.9216,
    },
    "Se": {
        "atomic_number": 34,
        "vdw_radii": 190,
        "name": "Selenium",
        "standard_mass": 78.96,
    },
    "Br": {
        "atomic_number": 35,
        "vdw_radii": 185,
        "name": "Bromine",
        "standard_mass": 79.904,
    },
    "Kr": {
        "atomic_number": 36,
        "vdw_radii": 202,
        "name": "Krypton",
        "standard_mass": 83.798,
    },
    "Rb": {
        "atomic_number": 37,
        "vdw_radii": 303,
        "name": "Rubidium",
        "standard_mass": 85.4678,
    },
    "Sr": {
        "atomic_number": 38,
        "vdw_radii": 249,
        "name": "Strontium",
        "standard_mass": 87.62,
    },
    "Y": {
        "atomic_number": 39,
        "vdw_radii": 180,
        "name": "Yttrium",
        "standard_mass": 88.90585,
    },
    "Zr": {
        "atomic_number": 40,
        "vdw_radii": 160,
        "name": "Zirconium",
        "standard_mass": 91.224,
    },
    "Nb": {
        "atomic_number": 41,
        "vdw_radii": 146,
        "name": "Niobium",
        "standard_mass": 92.90638,
    },
    "Mo": {
        "atomic_number": 42,
        "vdw_radii": 239,
        "name": "Molybdenum",
        "standard_mass": 95.94,
    },
    "Tc": {
        "atomic_number": 43,
        "vdw_radii": 136,
        "name": "Technetium",
        "standard_mass": 98.9062,
    },
    "Ru": {
        "atomic_number": 44,
        "vdw_radii": 134,
        "name": "Ruthenium",
        "standard_mass": 101.07,
    },
    "Rh": {
        "atomic_number": 45,
        "vdw_radii": 137,
        "name": "Rhodium",
        "standard_mass": 102.9055,
    },
    "Pd": {
        "atomic_number": 46,
        "vdw_radii": 144,
        "name": "Palladium",
        "standard_mass": 106.42,
    },
    "Ag": {"atomic_number": 47, "name": "Silver", "standard_mass": 107.8682},
    "Cd": {"atomic_number": 48, "name": "Cadmium", "standard_mass": 112.411},
    "In": {"atomic_number": 49, "name": "Indium", "standard_mass": 114.818},
    "Sn": {"atomic_number": 50, "name": "Tin", "standard_mass": 118.71},
    "Sb": {"atomic_number": 51, "name": "Antimony", "standard_mass": 121.76},
    "Te": {"atomic_number": 52, "name": "Tellurium", "standard_mass": 127.6},
    "I": {"atomic_number": 53, "name": "Iodine", "standard_mass": 126.90447},
    "Xe": {"atomic_number": 54, "name": "Xenon", "standard_mass": 131.293},
    "Cs": {"atomic_number": 55, "name": "Caesium", "standard_mass": 132.90545},
    "Ba": {"atomic_number": 56, "name": "Barium", "standard_mass": 137.327},
    "La": {"atomic_number": 57, "name": "Lanthanum", "standard_mass": 138.9055},
    "Ce": {"atomic_number": 58, "name": "Cerium", "standard_mass": 140.116},
    "Pr": {"atomic_number": 59, "name": "Praseodymium", "standard_mass": 140.90765},
    "Nd": {"atomic_number": 60, "name": "Neodymium", "standard_mass": 144.24},
    "Pm": {"atomic_number": 61, "name": "Promethium", "standard_mass": 145},
    "Sm": {"atomic_number": 62, "name": "Samarium", "standard_mass": 150.36},
    "Eu": {"atomic_number": 63, "name": "Europium", "standard_mass": 151.964},
    "Gd": {"atomic_number": 64, "name": "Gadolinium", "standard_mass": 157.25},
    "Tb": {"atomic_number": 65, "name": "Terbium", "standard_mass": 158.92534},
    "Dy": {"atomic_number": 66, "name": "Dysprosium", "standard_mass": 162.5},
    "Ho": {"atomic_number": 67, "name": "Holmium", "standard_mass": 164.93032},
    "Er": {"atomic_number": 68, "name": "Erbium", "standard_mass": 167.259},
    "Tm": {"atomic_number": 69, "name": "Thulium", "standard_mass": 168.93421},
    "Yb": {"atomic_number": 70, "name": "Ytterbium", "standard_mass": 173.04},
    "Lu": {"atomic_number": 71, "name": "Lutetium", "standard_mass": 174.967},
    "Hf": {"atomic_number": 72, "name": "Hafnium", "standard_mass": 178.49},
    "Ta": {"atomic_number": 73, "name": "Tantalum", "standard_mass": 180.9479},
    "W": {"atomic_number": 74, "name": "Tungsten", "standard_mass": 183.84},
    "Re": {"atomic_number": 75, "name": "Rhenium", "standard_mass": 186.207},
    "Os": {"atomic_number": 76, "name": "Osmium", "standard_mass": 190.23},
    "Ir": {"atomic_number": 77, "name": "Iridium", "standard_mass": 192.217},
    "Pt": {"atomic_number": 78, "name": "Platinum", "standard_mass": 195.078},
    "Au": {"atomic_number": 79, "name": "Gold", "standard_mass": 196.96655},
    "Hg": {"atomic_number": 80, "name": "Mercury", "standard_mass": 200.59},
    "Tl": {"atomic_number": 81, "name": "Thallium", "standard_mass": 204.3833},
    "Pb": {"atomic_number": 82, "name": "Lead", "standard_mass": 207.2},
    "Bi": {"atomic_number": 83, "name": "Bismuth", "standard_mass": 208.98038},
    "Po": {"atomic_number": 84, "name": "Polonium", "standard_mass": 209},
    "At": {"atomic_number": 85, "name": "Astatine", "standard_mass": 210},
    "Rn": {"atomic_number": 86, "name": "Radon", "standard_mass": 222},
    "Fr": {"atomic_number": 87, "name": "Francium", "standard_mass": 223},
    "Ra": {"atomic_number": 88, "name": "Radium", "standard_mass": 226.0254},
    "Ac": {"atomic_number": 89, "name": "Actinium", "standard_mass": 227},
    "Th": {"atomic_number": 90, "name": "Thorium", "standard_mass": 232.0381},
    "Pa": {"atomic_number": 91, "name": "Protactinium", "standard_mass": 231.03588},
    "U": {"atomic_number": 92, "name": "Uranium", "standard_mass": 238.02891},
    "Np": {"atomic_number": 93, "name": "Neptunium", "standard_mass": 237.0482},
    "Pu": {"atomic_number": 94, "name": "Plutonium", "standard_mass": 244},
    "Am": {"atomic_number": 95, "name": "Americium", "standard_mass": 243},
    "Cm": {"atomic_number": 96, "name": "Curium", "standard_mass": 243},
    "Bk": {"atomic_number": 97, "name": "Berkelium", "standard_mass": 247},
    "Cf": {"atomic_number": 98, "name": "Californium", "standard_mass": 251},
    "Es": {"atomic_number": 99, "name": "Einsteinium", "standard_mass": 254},
    "Fm": {"atomic_number": 100, "name": "Fermium", "standard_mass": 254},
    "Md": {"atomic_number": 101, "name": "Mendelevium", "standard_mass": 258},
    "No": {"atomic_number": 102, "name": "Nobelium", "standard_mass": 259},
    "Lr": {"atomic_number": 103, "name": "Lawrencium", "standard_mass": 262},
}

iupac_colors_rgb = {
    "H": (255, 255, 255),  # Hydrogen
    "He": (217, 255, 255),  # Helium
    "Li": (204, 128, 255),  # Lithium
    "Be": (194, 255, 0),  # Beryllium
    "B": (255, 181, 181),  # Boron
    "C": (144, 144, 144),  # Carbon
    "N": (48, 80, 248),  # Nitrogen
    "O": (255, 13, 13),  # Oxygen
    "F": (144, 224, 80),  # Fluorine
    "Ne": (179, 227, 245),  # Neon
    "Na": (171, 92, 242),  # Sodium
    "Mg": (138, 255, 0),  # Magnesium
    "Al": (191, 166, 166),  # Aluminum
    "Si": (240, 200, 160),  # Silicon
    "P": (255, 128, 0),  # Phosphorus
    "S": (255, 255, 48),  # Sulfur
    "Cl": (31, 240, 31),  # Chlorine
    "K": (143, 64, 212),  # Potassium
    "Ar": (128, 209, 227),  # Argon
    "Ca": (61, 255, 0),  # Calcium
    "Sc": (230, 230, 230),  # Scandium
    "Ti": (191, 194, 199),  # Titanium
    "V": (166, 166, 171),  # Vanadium
    "Cr": (138, 153, 199),  # Chromium
    "Mn": (156, 122, 199),  # Manganese
    "Fe": (224, 102, 51),  # Iron
    "Ni": (199, 138, 138),  # Nickel
    "Co": (255, 217, 143),  # Cobalt
    "Cu": (200, 128, 51),  # Copper
    "Zn": (125, 128, 176),  # Zinc
    "Ga": (194, 143, 143),  # Gallium
    "Ge": (102, 143, 143),  # Germanium
    "As": (189, 128, 227),  # Arsenic
    "Se": (255, 161, 0),  # Selenium
    "Br": (166, 41, 41),  # Bromine
    "Kr": (92, 184, 209),  # Krypton
    "Rb": (112, 46, 176),  # Rubidium
    "Sr": (0, 255, 0),  # Strontium
    "Y": (148, 255, 255),  # Yttrium
    "Zr": (148, 224, 224),  # Zirconium
    "Nb": (115, 194, 201),  # Niobium
    "Mo": (84, 181, 181),  # Molybdenum
    "Tc": (59, 158, 158),  # Technetium
    "Ru": (36, 125, 125),  # Ruthenium
    "Rh": (10, 125, 140),  # Rhodium
    "Pd": (0, 105, 133),  # Palladium
    "Ag": (192, 192, 192),  # Silver
    "Cd": (255, 217, 143),  # Cadmium
    "In": (166, 117, 115),  # Indium
    "Sn": (102, 128, 128),  # Tin
    "Sb": (158, 99, 181),  # Antimony
    "Te": (212, 122, 0),  # Tellurium
    "I": (148, 0, 148),  # Iodine
    "Xe": (66, 158, 176),  # Xenon
    "Cs": (87, 23, 143),  # Cesium
    "Ba": (0, 201, 0),  # Barium
    "La": (112, 212, 255),  # Lanthanum
    "Ce": (255, 255, 199),  # Cerium
    "Pr": (217, 255, 199),  # Praseodymium
    "Nd": (199, 255, 199),  # Neodymium
    "Pm": (163, 255, 199),  # Promethium
    "Sm": (143, 255, 199),  # Samarium
    "Eu": (97, 255, 199),  # Europium
    "Gd": (69, 255, 199),  # Gadolinium
    "Tb": (48, 255, 199),  # Terbium
    "Dy": (31, 255, 199),  # Dysprosium
    "Ho": (0, 255, 156),  # Holmium
    "Er": (0, 230, 117),  # Erbium
    "Tm": (0, 212, 82),  # Thulium
    "Yb": (0, 191, 56),  # Ytterbium
    "Lu": (0, 171, 36),  # Lutetium
    "Hf": (77, 194, 255),  # Hafnium
    "Ta": (77, 166, 255),  # Tantalum
    "W": (33, 148, 214),  # Tungsten
    "Re": (38, 125, 171),  # Rhenium
    "Os": (38, 102, 150),  # Osmium
    "Ir": (23, 84, 135),  # Iridium
    "Pt": (208, 208, 224),  # Platinum
    "Au": (255, 209, 35),  # Gold
    "Hg": (184, 184, 208),  # Mercury
    "Tl": (166, 84, 77),  # Thallium
    "Pb": (87, 89, 97),  # Lead
    "Bi": (158, 79, 181),  # Bismuth
    "Th": (255, 161, 0),  # Thorium
    "Pa": (255, 161, 0),  # Protactinium
    "U": (255, 161, 0),  # Uranium
    "Np": (255, 161, 0),  # Neptunium
    "Pu": (255, 161, 0),  # Plutonium
    "Am": (255, 161, 0),  # Americium
    "Cm": (255, 161, 0),  # Curium
    "Bk": (255, 161, 0),  # Berkelium
    "Cf": (255, 161, 0),  # Californium
    "Es": (255, 161, 0),  # Einsteinium
    "Fm": (255, 161, 0),  # Fermium
    "Md": (255, 161, 0),  # Mendelevium
    "No": (255, 161, 0),  # Nobelium
    "Lr": (255, 161, 0),  # Lawrencium
    "Rf": (204, 0, 89),  # Rutherfordium
    "Db": (209, 0, 79),  # Dubnium
    "Sg": (217, 0, 69),  # Seaborgium
    "Bh": (224, 0, 56),  # Bohrium
    "Hs": (230, 0, 46),  # Hassium
    "Mt": (235, 0, 38),  # Meitnerium
    "Ds": (240, 0, 33),  # Darmstadtium
    "Rg": (241, 0, 30),  # Roentgenium
    "Cn": (242, 0, 26),  # Copernicium
    "Nh": (242, 0, 26),  # Nihonium
    "Fl": (242, 0, 26),  # Flerovium
    "Mc": (242, 0, 26),  # Moscovium
    "Lv": (242, 0, 26),  # Livermorium
    "Ts": (242, 0, 26),  # Tennessine
    "Og": (242, 0, 26),  # Oganesson
}

atom_to_color = {elements[ele]['atomic_number']:iupac_colors_rgb[ele]  for ele in elements if elements[ele]['atomic_number'] < 84}
atom_to_radius = {elements[ele]['atomic_number']:elements[ele]['vdw_radii']  for ele in elements if elements[ele]['atomic_number'] < 84 and 'vdw_radii' in elements[ele]}

def get_atom_color_and_radius(atom): 
    if (atom < 0): 
        return (0.,0.,0.), 0.1
    if atom in atom_to_radius: 
        return atom_to_color[atom], atom_to_radius[atom]
    else:
        return atom_to_color[atom], 100.

def add_background(filepath = '/Users/john/blender1/chips.png'):
    img = bpy.data.images.load(filepath)
#    for area in bpy.context.screen.areas:
#        if area.type == 'VIEW_3D':
#            space_data = area.spaces.active
#            bg = space_data.background_images.new()
#            bg.image = img
#            space_data.show_background_images = True
#            break

    texture = bpy.data.textures.new("Texture.001", 'IMAGE')
    texture.image = img
    bpy.data.worlds['World'].active_texture = texture
    bpy.context.scene.world.texture_slots[0].use_map_horizon = True

# Create a material function
def create_material(color, alpha = 1.):
    material = bpy.data.materials.new(name=f"Sphere_Material_{color}")
#    material.use_nodes = False
#    nodes = material.node_tree.nodes
#    nodes.clear()
#    node_principled = nodes.new(type='ShaderNodeBsdfPrincipled')
#    node_output = nodes.new(type='ShaderNodeOutputMaterial')
    material.use_nodes = True
    rgba = [c /255. for c in color[:3]] + [alpha]
    material.node_tree.nodes["Principled BSDF"].inputs['Alpha'].default_value = alpha
    material.node_tree.nodes["Principled BSDF"].inputs['Base Color'].default_value = rgba
#    material.diffuse_color = rgba
    material.roughness = .1
#    material.use_transparency = True #  renders trans
    material.use_raytrace_refraction = True
#    node_principled.inputs[0].default_value = rgba
#    material.node_tree.links.new(node_principled.outputs[0], node_output.inputs[0])
    return material

ATOM_MATERIALS = []
for atom in atom_to_color: 
    ATOM_MATERIALS.append(create_material(atom_to_color[atom]))

TRANSPARENT_MATERIALS = []
for atom in atom_to_color: 
    TRANSPARENT_MATERIALS.append(create_material(atom_to_color[atom], .1))

