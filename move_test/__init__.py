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
    "name" : "move_test",
    "author" : "boynextdoor",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

class MoveOperator(bpy.types.Operator):
    bl_label = "Move X by 1"
    bl_idname = "move.move_x_by_1"

    def execute(self, context):
        for object in bpy.context.selectable_objects:
            object.location.x += 1
        return {'FINISHED'}

class MoveTestPanel(bpy.types.Panel):
    bl_idname = "MOVE_TEST"
    bl_label = "Move Test"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Move"

    # Draw the panel UI
    def draw(self, context):
        layout = self.layout
        column = layout.column()
        column.label(text="xxxx")
        column.operator(MoveOperator.bl_idname, text="Move x by 1")

classes = (
    MoveTestPanel,
    MoveOperator,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
