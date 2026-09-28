########################################################################################################################
# Imports
########################################################################################################################


import bpy


########################################################################################################################
# Classes
########################################################################################################################


class BLENVTOOLS_OT_copy_transforms(bpy.types.Operator):
    '''Copy transforms from one collection of objects to another'''

    bl_idname = 'blenvtools.copy_transforms'
    bl_label = 'Batch Copy Transforms'

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=400)

    def draw(self, context):
        lay = self.layout
        lay.use_property_split = True
        lay.prop(context.scene.blenvtools.batch_copy_transforms, 'collection_a')
        lay.prop(context.scene.blenvtools.batch_copy_transforms, 'collection_b', text='To')

    def execute(self, context):
        scene_props = context.scene.blenvtools
        if len(scene_props.batch_copy_transforms.collection_a.objects) != len(
            scene_props.batch_copy_transforms.collection_b.objects
        ):
            self.report({'ERROR'}, "Collections must have the same number of objects")
            return {'CANCELLED'}
        for index, ob in enumerate(scene_props.batch_copy_transforms.collection_a.objects):
            target_ob = scene_props.batch_copy_transforms.collection_b.objects[index]
            target_ob.location = ob.location
            target_ob.rotation_euler = ob.rotation_euler
            target_ob.scale = ob.scale
        return {'FINISHED'}


########################################################################################################################
# Registration
########################################################################################################################


classes = (BLENVTOOLS_OT_copy_transforms,)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
