


from build123d import * 
from ocp_vscode import show 

length = 135.0
width = 53.0
chamfer_size = 10.0
bottom_thickness = 3.0
bottom_chamfer= 3.0
wall_thickness = 2.0
wall_height = 16.4238
hole_dia = 5.2

with BuildSketch() as base_sketch:
    Rectangle(length, width)
    chamfer(base_sketch.vertices(), length=chamfer_size)

with BuildPart() as base_body:
    add(base_sketch)
    extrude(amount=bottom_thickness)

    # Step 2: Wall on top face
    top_face = base_body.faces().sort_by(Axis.Z)[-1]
    with BuildSketch(top_face) as wall_sketch:
        outer = Rectangle(length, width)
        chamfer(wall_sketch.vertices(), length=chamfer_size)
        offset(amount=-wall_thickness, mode=Mode.SUBTRACT)
    extrude(amount=wall_height)

    # 10mm wall trimming
    with BuildSketch(Plane.XY.offset(19.4238)) as trim_sketch:
        Rectangle(length, width)
        chamfer(trim_sketch.vertices(), length=chamfer_size)
        offset(amount=-1.0, mode=Mode.SUBTRACT)
    extrude(amount=-9.8238, mode=Mode.SUBTRACT)

    # ✅ FIX 1: extrude moved OUTSIDE BuildSketch (was incorrectly indented inside it)
    # ✅ FIX 2: Y location changed from 255 to 245, and height increased from 20 to 40
    #           so the rectangle (Y=225 to Y=265) clearly cuts through the wall
    #           without just grazing the boundary edge

    # Bottom chamfer
    bottom_edges = base_body.faces().sort_by(Axis.Z)[0].edges()
    chamfer(bottom_edges, length=bottom_chamfer)
# Top notch - cut through the end wall face
    with BuildSketch(Plane.XY.offset(bottom_thickness + wall_height)) as cut_sketch:
        with Locations((0, width/2 - 10)):  # Y=240, rectangle spans Y=225 to Y=255
             Rectangle(37.0, 2.0)
    extrude(amount=-wall_height+1.6, mode=Mode.SUBTRACT)

# bottom cylinder 80 and 50
 #30mm wala
    with BuildSketch (Plane.XY.offset(bottom_thickness)) as big_cy:
        with Locations((0,-12.5)):
            Circle(radius= 4.0)
    extrude(amount= 3.0, mode=Mode.ADD)
 #134mm wala
    with BuildSketch (Plane.XY.offset(bottom_thickness+bottom_thickness)) as bigthin_cy:
        with Locations((0,-12.5)):
            Circle(radius= 2.6)
    extrude(amount= 13.4, mode=Mode.ADD)

# bottom cylinder 50 and 20
    with BuildSketch (Plane.XY.offset(bottom_thickness)) as small_cy:
        with Locations((-52.5,-12.5), (-52.5,12.5)):
            Circle(radius= 2.5)
    extrude(amount= 3.0, mode=Mode.ADD)
    mirror(about=Plane.YZ)
 #134mm wala
    with BuildSketch (Plane.XY.offset(bottom_thickness+bottom_thickness)) as smlthin_cy:
        with Locations((-52.5,-12.5), (-52.5,12.5)):
            Circle(radius= 1.0)
    extrude(amount= 13.4, mode=Mode.ADD)
    mirror(about=Plane.YZ)

# Ellipse 
    with BuildSketch(Plane.XY.offset(bottom_thickness)) as ellipse_sketch:
        with Locations((-38.0,0)):
            Ellipse(x_radius=10.5, y_radius=9.0)
            Ellipse(x_radius=9.5, y_radius=8.0 , mode=Mode.SUBTRACT)
    extrude(amount= 3.0, mode=Mode.ADD)
    mirror(about=Plane.YZ)

result_part = base_body.part
show(result_part)

export_stl(result_part, "/Users/softage/RetroPad-Design/Bottom_part/bottom_part_generated.stl")