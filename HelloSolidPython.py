# Hello, SolidPython!

from solid import *
from solid.utils import *

d = difference() (
  cube(10),
  sphere(15)
)

scad_render_to_file(d, "generated.scad")