# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

import bpy
import random

def get_preferences(context=bpy.context):
    return context.user_preferences.addons["startup_tips"].preferences


# XXX unused
class TipsAndTricksChange(bpy.types.Operator):
    """Tips and Tricks for Blender usability"""
    bl_idname = "wm.tips_and_tricks_change"
    bl_label = "Tips and Tricks"
    bl_options = {'REGISTER', 'UNDO'}

    mode_items = [('NEXT', 'Next', ''), ('PREV', 'Previous', ''), ('RANDOM', 'Random', '')]
    mode = bpy.props.EnumProperty(name="Mode", items=mode_items, default='NEXT')

    def execute(self, context):
        global tips, tip_index

        if self.mode == 'NEXT':
            tip_index += 1
        elif self.mode == 'PREV':
            tip_index -= 1
        elif self.mode == 'RANDOM':
            tip_index = random.randrange(len(tips))

        return {'FINISHED'}


def draw_tips_and_tricks(self, context):
    layout = self.layout
    prefs = get_preferences(context)

    box = layout.box()

    split = box.split(percentage=0.3)
    split.label("Did you know:", icon='LAMP')
    # XXX another dirty trick: changing highlight color allows some redrawing,
    # at least for the tip string. emboss=False would disable button highlight, so can't use it ...
    #row.prop(prefs, "tip", text="", emboss=False)
    split.prop(prefs, "tip", text="")

    row = layout.row()
    row.prop(prefs, "index_prev", text="Previous", toggle=True)
    row.prop(prefs, "index_next", text="Next", toggle=True)
    row.separator()
    row.prop(prefs, "index_random", text="Random", toggle=True)
    #row.operator("wm.tips_and_tricks_change", text="Previous").mode = 'PREV'
    #row.operator("wm.tips_and_tricks_change", text="Next").mode = 'NEXT'
    #row.operator("wm.tips_and_tricks_change", text="Random").mode = 'RANDOM'


def register():
    #bpy.utils.register_class(TipsAndTricksChange)
    bpy.types.USERPREF_MT_splash.append(draw_tips_and_tricks)

def unregister():
    #bpy.utils.unregister_class(TipsAndTricksChange)
    bpy.types.USERPREF_MT_splash.remove(draw_tips_and_tricks)

if __name__ == "__main__":
    register()
