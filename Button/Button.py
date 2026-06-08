from build123d import *
from ocp_vscode import show

chamfer_size = 1.0
base_diameter= 9.6
cy_h= 15.5
rect_h= 5.6

with BuildPart() as button:
    with BuildSketch(Plane.XY) as cy:
        Circle(radius= base_diameter/2)
    extrude(amount=cy_h)

# chamfer on top edge 
    top_edge = button.edges().sort_by(Axis.Z)[-1]
    chamfer(top_edge, length= chamfer_size)
# rectangle in bottom
    with BuildSketch (Plane.XY) as rect:
        Rectangle(11.8,1.8)
        Rectangle(1.8,11.8)
    extrude(amount= rect_h, mode= Mode.ADD)
result_part = button.part
show(result_part)


vol = button.part.volume
print(f"Volume = {vol:.2f} mm³")
export_stl(result_part, "/Users/softage/RetroPad-Design/Button/button_generated.stl")
