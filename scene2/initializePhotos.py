import bpy

for obj in bpy.data.objects:
    if (obj.name != "Camera" and obj.name != "Lamp"):
        bpy.data.materials[obj.name].use_shadeless = True
        bpy.data.materials[obj.name].use_transparency = True
        bpy.data.materials[obj.name].transparency_method = 'RAYTRACE'
        bpy.data.materials[obj.name].alpha = 0
        bpy.data.materials[obj.name].texture_slots[0].use_map_alpha = True
        
for img in bpy.data.images:
    bpy.data.images[img.name].use_alpha = True
