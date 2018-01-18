from solid import *
from solid.utils import *

difference() {
  cube(10)
  sphere(15)
}

print scad_render(py_scad_obj)
