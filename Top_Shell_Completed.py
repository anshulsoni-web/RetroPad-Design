from build123d import *
from ocp_vscode import show

length = 1350
width = 530
chamfer_size = 100
bottom_thickness = 30
bottom_chamfer= 30
wall_thickness = 10
wall_height = 98.238
hole_dia = 52

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
        with Locations((0, (width/2 ) - 15)):
            Rectangle(370, 30)
    extrude(amount=-wall_height - bottom_thickness , mode=Mode.SUBTRACT)




    # extrude(amount=-bottom_thickness, mode= Mode.SUBTRACT) 
# making a cylinder
    with BuildSketch(Plane.XY.offset(30)) as cy_sketch:
        with Locations((0,-125)):
            Circle(radius= hole_dia/2)
            offset(amount= 14)
        with Locations((525,125),(525,-125),(-525,-125),(-525,125)):
            Circle(radius= 11)
            offset(amount= 14)
        # with Locations((0,140)):
        #     Rectangle(312,190)
        #     offset(amount= 2)

    extrude(amount= 20 + wall_height, mode= Mode.ADD) 

# another cy with -24 extrusion wallheight+base-24
    with BuildSketch(Plane.XY.offset(30)) as an_cy_sketch:
        with Locations((-480,0),(-380,85),(-280,0),(-380,-85)):
            Circle(radius= 50)
            offset(amount= 10)
        with Locations((380,0)):
            Ellipse(x_radius=172.5, y_radius=155)  # outer
            Ellipse(x_radius=162.5, y_radius=145, mode=Mode.SUBTRACT)  # inner cutout
    extrude(amount= wall_height-24, mode= Mode.ADD) 
# 4cy mai rectangular hole 
    with BuildSketch(Plane.XY.offset(30)) as an_cycut_sketch:
        with Locations((-480,0),(-380,85),(-280,0),(-380,-85)):
            Rectangle(120,20)
            Rectangle(20,120)
    extrude(amount= wall_height-24, mode= Mode.SUBTRACT)



# cylinder mai hole 
    with BuildSketch(Plane.XY.offset(30)) as cyhole_sketch:
        with Locations((0,-125)):
            Circle(radius= hole_dia/2)
        with Locations((0,-125),(525,125),(525,-125),(-525,-125),(-525,125)):
            Circle(radius= 11)

    extrude(amount=bottom_thickness + wall_height, mode= Mode.SUBTRACT)

# cDpad and button k lie hole 
    with BuildSketch(Plane.XY) as cyhole_sketch:

        with Locations((-480,0),(-380,85),(-280,0),(-380,-85)):
            Circle(radius= 50)
        with Locations((380,0)):
            Rectangle(300,100)
            Rectangle(100,270)

    extrude(amount=bottom_thickness + wall_height+30, mode= Mode.SUBTRACT)



# Rectangle of U shaped 
    with BuildSketch(Plane.XY.offset(bottom_thickness)) as u_sketch:
        with Locations((0, 120)):
            Rectangle(352, 230)
        with Locations((0, 140)):
            Rectangle(312, 230, mode=Mode.SUBTRACT)
    extrude(amount=wall_height + 20)  # ✅ outside BuildSketch, inside BuildPart

result_part = part.part
show(result_part)

export_stl(result_part, "/Users/softage/Downloads/codedcad/top_shell_completed.stl")