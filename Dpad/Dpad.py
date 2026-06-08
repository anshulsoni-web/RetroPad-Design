from build123d import* 
from ocp_vscode import show

chamfer_s= 1.0

with BuildPart() as retropad:
    with BuildSketch(Plane.XY) as rect:
        Rectangle(29.4,9.4)
        Rectangle(9.4,26.4)
    extrude(amount= 15.5, mode= Mode.ADD)

    top_face = retropad.faces().sort_by(Axis.Z)[-1]
    chamfer(top_face.edges(), length=chamfer_s)

    with BuildSketch(Plane.XY.offset(2.0)) as ellipse:
        Ellipse(16.0,14.0)
    extrude(amount= 4.5, mode= Mode.ADD)
result_part = retropad.part
show(result_part)


export_stl(result_part, "/Users/softage/Retropad-Design/Dpad/Dpad_generated.stl")