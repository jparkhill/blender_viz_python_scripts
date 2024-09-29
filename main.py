import bpy

# Clear existing scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

import numpy as np
import mathutils, pickle

# Blender imports are nonstd and I'm too lazy to fix them.
exec(bpy.data.texts['atom_types.py'].as_string())

# Load your numpy arrays here
#with open('/Users/john/matteo.pkl','rb') as f:
#with open('/Users/john/matteo2.pkl','rb') as f: 
with open('/Users/john/matteo3.pkl','rb') as f: 
    data = pickle.load(f)

mol_idx = 3
row = data[mol_idx]

atoms = row['atoms']
coords = row['coords'] # frames X atoms X 3
residue_ids = row.get('residue_ids', np.zeros_like(atoms))
free_atoms = row.get('free_atoms', np.ones_like(atoms))
n_frames = coords.shape[0]

is_lig = (residue_ids == 0)
lig_atoms = atoms[is_lig]
lig_coords = coords[:,is_lig]
n_lig = lig_atoms.shape[0]

has_protein = 'residue_ids' in row
if has_protein: 
    is_pro = np.logical_not(is_lig)
    pro_atoms = atoms[is_pro]
    pro_coords = coords[:,is_pro]
    pro_free = free_atoms[is_pro]

    # Only do protein atoms within a cutoff of the ligand. 
#    cutoff = 15.
    cutoff = 20.
    dists = np.sqrt(np.power(lig_coords[0][np.newaxis,:,:] - pro_coords[0][:,np.newaxis,:],2.0).sum(-1)).min(-1) < cutoff
    pro_atoms = pro_atoms[dists].copy()
    pro_coords = pro_coords[:,dists,:].copy()
    pro_free = pro_free[dists].copy()
    n_pro = pro_atoms.shape[0]
else: 
    n_pro = 0 

# Create spheres for ligand atoms. 
lig_spheres = []
for i in range(lig_atoms.shape[0]):
    atom_type = int(lig_atoms[i])
    radius = atom_to_radius[atom_type] / 215. 
    print(f'atom_type {atom_type}')
    bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, 
                                radius=radius, location=(0, 0, 0))
    sphere = bpy.context.active_object
    sphere.name = f"lig_{i}_{atom_type}"#_{mat.name}"
    mat = ATOM_MATERIALS[atom_type]
#    sphere.active_material = mat
    sphere.data.materials.append(mat)
    lig_spheres.append(sphere)

pro_spheres = []
for i in range(pro_atoms.shape[0]):
    atom_type = int(pro_atoms[i])
    radius = atom_to_radius[atom_type] / 215. 
    print(f'atom_type {atom_type}')
    bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, 
                                radius=radius, location=(0, 0, 0))
    sphere = bpy.context.active_object
    sphere.name = f"pro_{i}_{atom_type}"#_{mat.name}"
    mat = TRANSPARENT_MATERIALS[atom_type]
    sphere.data.materials.append(mat)
    pro_spheres.append(sphere)

# Set up animation
bpy.context.scene.frame_start = 0
bpy.context.scene.frame_end = n_frames - 1

for frame in range(n_frames):
    bpy.context.scene.frame_set(frame)

    for i, sphere in enumerate(lig_spheres):
        # Update position 
        sphere.location = mathutils.Vector(lig_coords[frame, i])
        sphere.keyframe_insert(data_path="location", frame=frame)

    if (has_protein): 
        for i, sphere in enumerate(pro_spheres):
            # Update position 
            if frame == 0 or pro_free[i]:
                sphere.location = mathutils.Vector(pro_coords[frame, i])
                sphere.keyframe_insert(data_path="location", frame=frame)


# Set up camera
bpy.ops.object.camera_add(location=(70, 0, 00))
camera = bpy.context.active_object
camera.name = "Camera"
camera.data.lens = 25
camera.rotation_euler = mathutils.Euler((0, 1.57, 0), 'XYZ')
# Set the camera as active
bpy.context.scene.camera = camera

# Set up lighting
bpy.ops.object.light_add(type='SUN', location=(45, 15, 15))
sun = bpy.context.active_object
sun.rotation_euler = mathutils.Euler((0, 1.57, 0), 'XYZ')
sun.name = "Sun"
sun.data.energy = 5


print("Animation setup complete!")
