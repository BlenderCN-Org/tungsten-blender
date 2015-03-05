import bpy
from bl_ui import properties_world

from . import base
from .texture import ColorTextureProperty

base.compatify_class(properties_world.WORLD_PT_context_world)

def find_world_obj(x):
    for w in bpy.data.worlds:
        if w.tungsten == x:
            return w

@base.register_root_panel
class W_PT_world(properties_world.WorldButtonsPanel, base.RootPanel):
    bl_label = "Tungsten World"
    prop_class = bpy.types.World

    @classmethod
    def get_object(cls, context):
        return context.world

    PROPERTIES = {
        'emission': ColorTextureProperty(
            name='Emission',
            description='Emission',
            default=(0.8, 0.8, 0.8),
            get_obj=find_world_obj,
        ),
    }

    @classmethod
    def to_scene_data(self, scene, world):
        w = world.tungsten
        return {
            'type': 'infinite_sphere',
            'bsdf': {'type': 'null'},
            'emission': w.emission.to_scene_data(scene, w),
        }

    def draw_for_object(self, world):
        layout = self.layout
        w = world.tungsten

        w.emission.draw(layout, w)
