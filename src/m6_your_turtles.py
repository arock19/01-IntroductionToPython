"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Achintya Gupta.
"""
###############################################################################
# TO: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# TO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module
##############################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
window.delay(20)
t1 = rg.SimpleTurtle('turtle')
t2 = rg.SimpleTurtle('turtle')
t1.speed = 200
t2.speed = 200
t1.pen = rg.Pen('blue',2)
a = 3
t2.pen = rg.Pen('red',a)
for k in range(100):
    a=a**0.9
    t1.draw_circle(42-k/3)
    t1.left(30)
    t2.pen_down()
    t2.forward(30)
    t2.left(5*k)

window.close_on_mouse_click()
