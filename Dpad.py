from build123d import* 
from ocp_vscode import show

chamfer_s= 10

with BuildPart() as retropad:
    with BuildSketch(Plane.XY) as rect:
        Rectangle(294,94)
        Rectangle(94,264)
    extrude(amount= 155, mode= Mode.ADD)

    top_face = retropad.faces().sort_by(Axis.Z)[-1]
    chamfer(top_face.edges(), length=chamfer_s)

    with BuildSketch(Plane.XY.offset(20)) as ellipse:
        Ellipse(160,140)
    extrude(amount= 45, mode= Mode.ADD)
result_part = retropad.part
show(result_part)


export_stl(result_part, "/Users/softage/Downloads/codedcad/Dpad_Coded.stl")