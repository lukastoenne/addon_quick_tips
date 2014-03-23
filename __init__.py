### BEGIN GPL LICENSE BLOCK #####
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

bl_info = {
    "name": "Startup Tips and Tricks",
    "author": "Lukas Toenne",
    "version": (0, 1, 0),
    "blender": (2, 7, 0),
    "location": "Screen",
    "description": "Show tips and tricks for Blender usability on startup",
    "warning": "Attempts to draw in the splash screen are hampered by lack of notifiers and proper redraw",
    "category": "System"}

import bpy
import random
from startup_tips import ui
from startup_tips.tips import tips

# seed with system time
random.seed()

tip_index = random.randrange(len(tips))


class StartupTipsPreferences(bpy.types.AddonPreferences):
    bl_idname = "startup_tips"

    def tip_get(self):
        global tips, tip_index
        return tips[tip_index % len(tips)]
    def tip_set(self, value):
        # dummy setter to allow notifiers
        pass
    tip = bpy.props.StringProperty("Tip", get=tip_get, set=tip_set)

    # XXX This is ugly: We can't use real operator buttons in the splash screen,
    # they only work once due to missing redraws ...
    # Instead we use these "pseudo operator" bool properties

    def next_get(self):
        return False
    def next_set(self, value):
        global tip_index
        tip_index += 1
    index_next = bpy.props.BoolProperty("Next", get=next_get, set=next_set)

    def prev_get(self):
        return False
    def prev_set(self, value):
        global tip_index
        tip_index -= 1
    index_prev = bpy.props.BoolProperty("Previous", get=prev_get, set=prev_set)

    def random_get(self):
        return False
    def random_set(self, value):
        global tip_index
        tip_index = random.randrange(len(tips))
    index_random = bpy.props.BoolProperty("Random", get=random_get, set=random_set)


def register():
    bpy.utils.register_class(StartupTipsPreferences)
    ui.register()

def unregister():
    bpy.utils.unregister_class(StartupTipsPreferences)
    ui.unregister()

if __name__ == "__main__":
    register()
