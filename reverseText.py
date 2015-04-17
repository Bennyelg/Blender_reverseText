import bpy  
bl_info = {
    "name": "Reverse The text",
    "description": "Reverse the selected text , built due to requestes of Blender.org.il users.",
    "data": "6.3.2014",
    "author": "Benny Elgazar",
    "version": (0, 1),
    "blender": (2, 69,11),
    "location": "Object > Reverse Text",
    "warning": "The use is only on your responsibility.",
    "contact info": "http://forum.blender.org.il/member.php?action=profile&uid=141"
                "or at elgazarbenny@gmail.com",
    "category": "Helpfull addon to right to left users"}
    
class ReverseText(bpy.types.Operator):  
    """Reverse Text"""  
    bl_idname = "object.reverse_text"  
    bl_label = "Reverse Text"
     
    def execute(self, context):
        for obj in bpy.data.objects:
            if obj.type == 'FONT' and obj.select == True:
                curve_text = obj.data
                curve_text.body = curve_text.body[::-1]
        return {'FINISHED'}
      
def add_object_button(self, context):  
    self.layout.operator(  
    ReverseText.bl_idname,  
    text=ReverseText.__doc__)  
    
    
def register():
    bpy.utils.register_class(ReverseText)  
    bpy.types.VIEW3D_MT_object.append(add_object_button)  
if __name__ == "__main__":  
    register()  
