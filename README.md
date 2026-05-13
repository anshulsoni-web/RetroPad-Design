# RetroPad-Design
Design of a RetroPad using build123d python library. 
This document contains replica of a RetroPad design. The design was created using build123d python libray. 
First, build123d was imported in VScode, then OCP viewer was imported to help us visualize the design in real time. 
Then assigned values to key variables such as lenght, heigh, thickness that will be used to define the body further. 
First bulding the base sketch using "buildsketch" command for 'Top Shell', part of design, then chamfering the edges by simply selecting the base sketch. Then, extruding it by defining it as a base body using "buildpart" command. After that, using base sketch as base plane, moving ahead with derawing sketches and extruding them to shape the body as desired. 
To extrude, "mode.ADD" is used and to extrude cut, "mode.SUBTRACT" is used. This is important part and if we do not define mode, the library by deafult considers "mode.ADD" with extrude. 
To apply chamfer or fillet, the plane is be defined first and then, simply "chamfer" command is applied. 
To make cylinder, circle, rectangle, ellipse or any shape, their "centre point" is fed "with location" command  and then defining the extrude or extrude cut using extrude mode.ADD or mode.subtract command.
For rectangle, centre point rectangle is by default consideration of this libtrary, later in parethesis first "length of rectangle along X axis" is fed and the latter is considered as "width along Y axis". This is same for ellipse, the first radiuse is processed along X axis and then next along Y axis separated by a coma. 
At last, extracting the solid body from buildpart context manager using the name used to define the body in begining and storing it in a variable named result_part.
Using show(result_part) feature of OCP viewer, the body was visualised in VS code.  
Using the same method, Button, D-Pad and Bottom shell is made. 
# Assembly
