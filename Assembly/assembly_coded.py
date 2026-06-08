from build123d import *
from ocp_vscode import show

import sys
sys.path.append("/Users/softage/RetroPad-Design/Top_shell")
sys.path.append("/Users/softage/RetroPad-Design/Button")
sys.path.append("/Users/softage/RetroPad-Design/Dpad")
sys.path.append("/Users/softage/RetroPad-Design/Bottom_part")

from Top_Shell_Completed import result_part as ts
from Button import result_part as btn
from Dpad import result_part as dpad
from bottom_part import result_part as btm

# ── Find mating points ────────────────────────────────────────
btn_bottom = btn.faces().sort_by(Axis.Z)[0].center()
btm_top = btm.faces().sort_by(Axis.Z)[-1].center()
# ── Button 1 ──────────────────────────────────────────────────
btn1 = btn.moved(Location((0, 0, 0)))  # copy using moved()
j_ts1  = RigidJoint("hole_1", ts,   Location((-38, 8.5, 9)))
j_btn1 = RigidJoint("bottom", btn1, Location(btn_bottom, (1, 0, 0), 180))
j_ts1.connect_to(j_btn1)

# ── Button 2 ──────────────────────────────────────────────────
btn2 = btn.moved(Location((0, 0, 0)))  # another copy
j_ts2  = RigidJoint("hole_2", ts,   Location((-38, -8.5, 9)))
j_btn2 = RigidJoint("bottom", btn2, Location(btn_bottom, (1, 0, 0), 180))
j_ts2.connect_to(j_btn2)

# ── Button 3 ──────────────────────────────────────────────────
btn3 = btn.moved(Location((0, 0, 0)))  # copy using moved()
j_ts3  = RigidJoint("hole_3", ts,   Location((-48, 0, 9)))
j_btn3 = RigidJoint("bottom", btn3, Location(btn_bottom, (1, 0, 0), 180))
j_ts3.connect_to(j_btn3)

# ── Button 4 ──────────────────────────────────────────────────
btn4 = btn.moved(Location((0, 0, 0)))  # another copy
j_ts4  = RigidJoint("hole_4", ts,   Location((-28, 0, 9)))
j_btn4 = RigidJoint("bottom", btn4, Location(btn_bottom, (1, 0, 0), 180))
j_ts4.connect_to(j_btn4)


# ── D-pad ──────────────────────────────────────────────────
dpad = dpad.moved(Location((0, 0, 0)))  # another copy
j_ts5  = RigidJoint("hole_5", ts,   Location((38, 0, 9.5)))
j_dpad = RigidJoint("bottom", dpad, Location(btn_bottom, (1, 0, 0), 180))
j_ts5.connect_to(j_dpad)

# ── Bottom part mated to top shell ────────────────────────────
btm_height = 12.8238 + 19.4238 - 9.8238

# Flip BTM around X and move it below TS
btm1 = btm.moved(Location((0, 0, 0), (1, 0, 0), 180))  # flip X
btm1 = btm.moved(Location((0, 0, 0), (0, 1, 0), 180))  # flip Y
btm1 = btm1.moved(Location((0, 0, btm_height)))        # place below TS


# ── Show ──────────────────────────────────────────────────────
show(ts, btn1, btn2, btn3, btn4, dpad, btm1)

assembly = Compound([ts, btn1, btn2, btn3, btn4, dpad, btm1])
export_stl(assembly, "/Users/softage/RetroPad-Design/assembly_generated.stl")
