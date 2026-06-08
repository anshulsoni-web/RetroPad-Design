from build123d import *
from ocp_vscode import show

chamfer_size = 10
base_diameter= 96
cy_h= 155
rect_h= 56

with BuildPart() as button:
    with BuildSketch(Plane.XY) as cy:
        Circle(radius= base_diameter/2)
    extrude(amount=cy_h)

# chamfer on top edge 
    top_edge = button.edges().sort_by(Axis.Z)[-1]
    chamfer(top_edge, length= chamfer_size)
# rectangle in bottom
    with BuildSketch (Plane.XY) as rect:
        Rectangle(118,18)
        Rectangle(18,118)
    extrude(amount= rect_h, mode= Mode.ADD)
result_part = button.part
show(result_part)

export_stl(result_part, "/Users/softage/Downloads/codedcad/button_coded.stl")
