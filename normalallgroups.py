bl_info = {
    "name": "Beef's Blender Tools",
    "description": "Tools and scripts to help with VRChat avatar Creation.",
    "author": "Beef",
    "version": (1, 0),
    "blender": (3, 4, 0),
    "location": "View3D > Object",
    "category": "Object", 
}

import bpy

class OBJECT_PT_beef_toolkit(bpy.types.Panel):
    
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    bl_category = "Beef ToolKit"
    bl_label = "The Beef Toolkit."

    def draw(self, context):
        # Layout of the panel
        row = self.layout.row()
        row.operator("object.normalize_all_locked", text= "Normalize All Locked Vertex Groups")

class NormalizeAllLocked(bpy.types.Operator):
    """Normalize All locked vertex groups of a given Mesh"""
    bl_idname = "object.normalize_all_locked"
    bl_label = "Normalize All Locked Vertex Groups"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Get the active object
        obj = bpy.context.object

        # Check if the active object is a mesh
        if obj.type == 'MESH':

            # Get the vertex groups of the active object
            vertex_groups = obj.vertex_groups

            # Loop through each vertex group
            for group in vertex_groups:
                # Check if the vertex group is locked
                if group.lock_weight:
                    # Select the locked vertex group
                    bpy.ops.object.vertex_group_set_active(group=group.name)
                    
                    # Normalize all vertices in the locked group manually
                    bpy.ops.object.mode_set(mode='WEIGHT_PAINT')
                    bpy.ops.object.vertex_group_normalize_all(lock_active=True)
                    bpy.ops.object.mode_set(mode='OBJECT')
        
        return{'FINISHED'}
    
def menu_func(self, context):
    self.layout.operator(NormalizeAllLocked.bl_idname)

def register():
    bpy.utils.register_class(NormalizeAllLocked)
    bpy.utils.register_class(OBJECT_PT_beef_toolkit)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(NormalizeAllLocked)
    bpy.utils.unregister_class(OBJECT_PT_beef_toolkit)

if __name__ == "__main__":
    register()