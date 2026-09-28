########################################################################################################################
# Imports
########################################################################################################################


import bpy


########################################################################################################################
# Classes
########################################################################################################################


class BatchCopyTransformsProperties(bpy.types.PropertyGroup):
    collection_a: bpy.props.PointerProperty(type=bpy.types.Collection, name="Copy Transforms From")
    collection_b: bpy.props.PointerProperty(type=bpy.types.Collection, name="Copy Transforms To")


class BlenvtoolsSceneProperties(bpy.types.PropertyGroup):
    batch_copy_transforms: bpy.props.PointerProperty(name='Batch Copy Transforms', type=BatchCopyTransformsProperties)


########################################################################################################################
# Registration
########################################################################################################################


classes = [
    BatchCopyTransformsProperties,
    BlenvtoolsSceneProperties,
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.blenvtools = bpy.props.PointerProperty(type=BlenvtoolsSceneProperties, name='blenvtools')


def unregister():
    del bpy.types.Scene.blenvtools
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
