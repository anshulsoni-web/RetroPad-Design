# RetroPad-Design
Design of a RetroPad using the build123d Python library. 
This document contains a replica of a RetroPad design. The design was created using the Build123D Python library. 
First, build123d was imported into VSCode, then the OCP viewer was imported to help us visualize the design in real time. 
Then, assigned values to key variables such as length, height, and thickness that will be used to define the body further. 
First, build the base sketch using the "buildsketch" command for 'Top Shell', part of the design, then chamfer the edges by simply selecting the base sketch. Then, extrude it by defining it as a base body using the "buildpart" command. After that, using the base sketch as a base plane, moving ahead with drawing sketches and extruding them to shape the body as desired. 
To extrude, "mode.ADD" is used, and to extrude cut, "mode.SUBTRACT" is used. This is an important part, and if we do not define mode, the library by default considers "mode.ADD" with extrude. 
To apply a chamfer or fillet, the plane is defined first, and then the "chamfer" command is simply applied. 
To make a cylinder, circle, rectangle, ellipse, or any shape, its "centre point" is fed a "location" command and then defining the extrude or extrude cut using extrude mode.ADD or mode.subtract command.
For a rectangle, the centre point rectangle is by default considered in this library. Later, in parentheses, the first "length of rectangle along X axis" is fed and the latter is considered as "width along Y axis". This is the same for an ellipse, the first radius is processed along the X axis and then next along Y axis, separated by a comma. 
At last, extracting the solid body from the buildpart context manager using the name used to define the body in the beginning and storing it in a variable named result_part.
Using the show(result_part) feature of the OCP viewer, the body was visualised in VS Code.  
Using the same method, the Button, D-Pad and Bottom shell is made. 
# Assembly
All the designs are assembled in a new file. 
Beginning by importing the library and OCP viewer, the Python module was imported by mode.sys. Path to the files/parts is given by sys.path, so it extracts the files from the desired folder. The folder path is fed in .append(). 
Next, all the desired parts are imported one by one using their file name.
The assembly combines its axis and origin with the axis and origin on first part. So, now all the parts are to be assembled according to the origin of the first part and the origin of their parts themselves. 
To flip an object along any axis, it can be defined in the joint command by varying the location of part in while defining the join_part variable, i.e., joining w.r.to part itself. The location is defined while defining the join_base variable, i.e., joining w.r.to base body. 
Used the show command with all the mates in parentheses to show them in real time in the OCP viewer. 

