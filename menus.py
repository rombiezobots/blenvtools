########################################################################################################################
# Imports
########################################################################################################################


import bpy


########################################################################################################################
# Functions
########################################################################################################################


def draw_menu_view3d(self, context):
    '''Draw the viewport's context menu'''
    lay = self.layout
    lay.separator()
    lay.menu('VIEW3D_MT_blenvtools')


########################################################################################################################
# Classes
########################################################################################################################


class VIEW3D_MT_blenvtools(bpy.types.Menu):
    bl_label = 'blenvtools'

    def draw(self, context):
        lay = self.layout
        lay.operator('blenvtools.copy_transforms')


########################################################################################################################
# Registration
########################################################################################################################


classes = [
    VIEW3D_MT_blenvtools,
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.VIEW3D_MT_object_context_menu.append(draw_menu_view3d)


def unregister():
    bpy.types.VIEW3D_MT_object_context_menu.remove(draw_menu_view3d)
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
