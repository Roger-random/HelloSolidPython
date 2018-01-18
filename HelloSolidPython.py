# Hello, SolidPython!

from solid import *
from solid.utils import *

d = difference() (
  cube(10),
  sphere(15)
)

print(scad_render(d))
