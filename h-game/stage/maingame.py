from py4godot.classes import gdclass
from py4godot.classes.Control import Control
from .charactor import Globals

@gdclass
class maingame(Control):
	def _ready(self):
		Globals.init_character()

		print(f"Level: {Globals.level}")
		print(f"EXP: {Globals.exp}/{Globals.exp_req}")
		print(f"Total EXP: {Globals.exp_total}")
	def _on_skip_pressed(self):
		print("skip")


	def _on_next_pressed(self):
		print("next")
		Globals.gain_exp(50)
		print(f"Level: {Globals.level}")
		print(f"EXP: {Globals.exp}/{Globals.exp_req}")
		print(f"Total EXP: {Globals.exp_total}")
