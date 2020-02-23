# ==========================z
#
#	Effects
#
#	These functions produce various visual effects.
#	Try experimenting by combining these in different orders,
#	and see what it produces!
#
# ==========================z

import pipe_test

def fadeOutIn():
	# Creates a football-shaped waveform
	# Seems to brighten the selected part of the image
	pipe_test.do_command("FadeOut")
	pipe_test.do_command("FadeIn")

def reverse():
	pipe_test.do_command("Reverse")

def echo():
	pipe_test.do_command("Echo: Delay=5 Decay=0.8")

def saveMultipleFrames():
	pass
	# For however many frames we want...
		# Apply Effects...
		# Export file...
		# Undo effects...
		# Redo effects, but increment the intensity...

print("\nApplying effects to selection...\n")
fadeOutIn()
echo()
