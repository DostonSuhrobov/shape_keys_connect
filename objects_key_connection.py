# Add driver from 'selected' object to target 'active' object.
# Target values are shape_key values
# 
# ShapeKeys must be named after Object for the script to work:
#
#      selected Object     = Cube
#      selected Shape Keys = Cube_abcd
#
#      active Object       = Sphere
#      active Shape Keys   = Sphere_abcd
#      
# 1. Select all object candidates to receive a driver.
# 2. Select 'active' object as driver target. 
# 3. Run script. 

import bpy

selected_obj = bpy.context.selected_objects
active_obj = bpy.context.active_object
shapekey_list_string = str(active_obj.data.shape_keys.key_blocks.keys())


for obj in selected_obj:
    if not obj == active_obj:
        for key in obj.data.shape_keys.key_blocks:
            if key.name.lstrip(obj.name) in shapekey_list_string:
                if not key.name == "Basis":
                    skey_driver = key.driver_add('value')
                    skey_driver.driver.type = 'AVERAGE'
                   # skey_driver.driver.show_debug_info = True
                    newVar = skey_driver.driver.variables.new()
                    newVar.name = "var"
                    newVar.type = 'SINGLE_PROP'
                    newVar.targets[0].id_type = 'KEY'
                    newVar.targets[0].id = active_obj.data.shape_keys
                    newVar.targets[0].data_path = 'key_blocks["' + key.name.lstrip(obj.name)+ '"].value' 
                    # litlle change was made here by deleting the active object name for the path  
                    
                  