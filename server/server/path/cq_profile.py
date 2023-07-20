import cadquery as cq

from ocp_freecad_cam import Endmill, Job
from .utils import save_gcode, export_stl

def run_cq_profile(diameter: int):
	wp = cq.Workplane().box(5, 5, 2)
	filename = "profile_shape"
	export_stl(wp, filename)

	top = wp.faces(">Z").workplane()
	profile_shape = wp.faces("<Z")

	tool = Endmill(diameter=diameter)
	job = Job(top, wp, "grbl", units="metric").profile(profile_shape, tool)
	save_gcode(job, filename)
