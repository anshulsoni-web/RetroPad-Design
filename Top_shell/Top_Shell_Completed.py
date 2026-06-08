from build123d import *
from ocp_vscode import show

length = 135
width = 53
chamfer_size = 10
bottom_thickness = 3
bottom_chamfer= 3
wall_thickness = 1
wall_height = 9.8238
hole_dia = 5.2

# Step 1: Bottom base - chamfered rectangle extruded 30mm
with BuildSketch() as base_sketch:
    Rectangle(length, width)
    chamfer(base_sketch.vertices(), length=chamfer_size)


with BuildPart() as part:
    add(base_sketch)
    extrude(amount=bottom_thickness)

    # Step 2: Wall on top face
    top_face = part.faces().sort_by(Axis.Z)[-1]
    with BuildSketch(top_face) as wall_sketch:
        # Outer profile
        outer = Rectangle(length, width)
        chamfer(wall_sketch.vertices(), length=chamfer_size)
        # Inner profile - offset inward to create wall thickness
        offset(amount=-wall_thickness, mode=Mode.SUBTRACT)

    extrude(amount=wall_height)
    #     # Step 4: Bottom chamfer
    bottom_edges = part.faces().sort_by(Axis.Z)[0].edges()
    chamfer(bottom_edges, length=bottom_chamfer)


   # Step 5: Cut a 370x30 rectangle along the length (centered on top edge)

    with BuildSketch(part.faces().sort_by(Axis.Z)[-1]) as cut_sketch:
        with Locations((0, (width/2 ) - 1.5)):
            Rectangle(37, 3)
    extrude(amount=-wall_height - bottom_thickness , mode=Mode.SUBTRACT)




    # extrude(amount=-bottom_thickness, mode= Mode.SUBTRACT)
# making a cylinder
    with BuildSketch(Plane.XY.offset(3)) as cy_sketch:
        with Locations((0,-12.5)):
            Circle(radius= hole_dia/2)
            offset(amount= 1.4)
        with Locations((52.5,12.5),(52.5,-12.5),(-52.5,-12.5),(-52.5,12.5)):
            Circle(radius= 1.1)
            offset(amount= 1.4)
        # with Locations((0,140)):
        #     Rectangle(312,190)
        #     offset(amount= 2)

    extrude(amount= 2 + wall_height, mode= Mode.ADD)

# another cy with -24 extrusion wallheight+base-24
    with BuildSketch(Plane.XY.offset(3)) as an_cy_sketch:
        with Locations((-48,0),(-38,8.5),(-28,0),(-38,-8.5)):
            Circle(radius= 5)
            offset(amount= 1)
        with Locations((38,0)):
            Ellipse(x_radius=17.25, y_radius=15.5)  # outer
            Ellipse(x_radius=16.25, y_radius=14.5, mode=Mode.SUBTRACT)  # inner cutout
    extrude(amount= wall_height-2.4, mode= Mode.ADD)
# 4cy mai rectangular hole
    with BuildSketch(Plane.XY.offset(3)) as an_cycut_sketch:
        with Locations((-48,0),(-38,8.5),(-28,0),(-38,-8.5)):
            Rectangle(12,2)
            Rectangle(2,12)
    extrude(amount= wall_height-2.4, mode= Mode.SUBTRACT)



# cylinder mai hole
    with BuildSketch(Plane.XY.offset(3)) as cyhole_sketch:
        with Locations((0,-12.5)):
            Circle(radius= hole_dia/2)
        with Locations((0,-12.5),(52.5,12.5),(52.5,-12.5),(-52.5,-12.5),(-52.5,12.5)):
            Circle(radius= 1.1)

    extrude(amount=bottom_thickness + wall_height, mode= Mode.SUBTRACT)

# cDpad and button k lie hole
    with BuildSketch(Plane.XY) as cyhole_sketch:

        with Locations((-48,0),(-38,8.5),(-28,0),(-38,-8.5)):
            Circle(radius= 5)
        with Locations((38,0)):
            Rectangle(30,10)
            Rectangle(10,27)

    extrude(amount=bottom_thickness + wall_height+3, mode= Mode.SUBTRACT)



# Rectangle of U shaped
    with BuildSketch(Plane.XY.offset(bottom_thickness)) as u_sketch:
        with Locations((0, 12)):
            Rectangle(35.2, 23)
        with Locations((0, 14)):
            Rectangle(31.2, 23, mode=Mode.SUBTRACT)
    extrude(amount=wall_height + 2)  # ✅ outside BuildSketch, inside BuildPart

result_part = part.part
show(result_part)

export_stl(result_part, "/Users/softage/RetroPad-Design/Top_shell/top_shell_generated.stl")
