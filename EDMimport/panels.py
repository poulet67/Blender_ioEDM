import bpy


class EDMDataPanel(bpy.types.Panel):
  bl_idname = "OBJECT_PT_edmtools"
  bl_label = "EDM Tools"
  bl_space_type = 'PROPERTIES'
  bl_region_type = 'WINDOW'
  bl_context = "data"

  @classmethod
  def poll(cls, context):
    return context.object.type == 'EMPTY'  

  def draw(self, context):
    self.layout.prop(context.object, "is_connector")

class DopeActionProperties(bpy.types.Panel):
  """Creates a Panel in the Object properties window"""
  bl_label = "EDM Action Properties"
  bl_idname = "OBJECT_PT_dope_action"
  bl_space_type = 'DOPESHEET_EDITOR'
  bl_region_type = 'UI'
  bl_context = "action"

  @classmethod
  def poll(self, context):
    try:
      return context.object.animation_data.action != None
    except AttributeError:
        return False

  def draw(self, context):
    row = self.layout.row()
    row.prop(context.object.animation_data.action, "argument")

def register():
  bpy.utils.register_class(EDMDataPanel)
  bpy.utils.register_class(DopeActionProperties)

def unregister():
  bpy.utils.unregister_class(DopeActionProperties)
  bpy.utils.unregister_class(EDMDataPanel)




#   import bpy

# #bpy.types.Object.is_connector = bpy.props.BoolProperty(
# ##      default=False, 
# #      name="Is Connector?", 
# #      description="Is this empty a connector object?")

# 

# def register():
#     bpy.utils.register_class(HelloWorldPanel)


# def unregister():
#     bpy.utils.unregister_class(HelloWorldPanel)


# if __name__ == "__main__":
#     register()