# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy

bl_info = {
    "name" : "asswecan_test",
    "author" : "boynextdoor",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

class AssWeCanPanel(bpy.types.Panel):
    bl_idname = "ASS_WE_CAN"
    bl_label = "Ass we can"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Ass"

    # Draw the panel UI
    def draw(self, context):
        pass

classes = (
    AssWeCanPanel,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

# if __name__ == "__main__":
#     register()
