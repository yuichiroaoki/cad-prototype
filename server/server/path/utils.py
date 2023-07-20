import cadquery as cq
from ocp_freecad_cam import Job

def save_gcode(job: Job, filename: str):
	gcode = job.to_gcode()
	with open(f"data/{filename}.gcode", "w") as f:
		f.write(gcode)

def export_stl(shape: cq.Shape, filename: str):
	cq.exporters.export(shape, f"data/{filename}.stl")