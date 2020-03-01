# ==========================
#
#	Effects
#
#	These functions produce various visual effects.
#	Try experimenting by combining these in different orders,
#	and see what it produces!
#
# ==========================

exec( open("pipe_test.py" ).read() )


def saveMultipleFrames(commandStrings, reversed=False):
	"""
	Does a stack of commands frame by frame and
	opens the export window every time to assist
	with saving a sequence of commands
	"""
	if reversed:
		commandStrings = reversed(commandStrings)
	for command in commandStrings:
		do(command)
		do("Export")


# Shuffle around chunks of the image
def cutAndPaste():
	"""
	start = 0 # get end of file header
	end   = 100 # end of file

	# Divide the track into X even sections
	# Tuples w/ start and end timestamp
	sections = [
		(0, 20),
		(20, 40),
		(40, 60),
		(60, 80),
		(80, 100),
	]

	# Cut each section and paste it at the end of the next one?
	for s in sections:
		do("Select: Start={} End={}".format(s[0], s[1]))
		do("Cut")
		do("Select: Start={} End={}".format(s[1], s[1]))
		do("Paste")
	"""
	pass


# Creates a football-shaped waveform
# Seems to brighten the selected part of the image in a gradient
def fadeOutIn():
	do("FadeOut")
	do("FadeIn")

def reverb():
	do("Reverb: RoomSize=75 Delay=10 Reverberance=50 HfDamping=50 ToneLow=100 ToneHigh=100 WetGain=-1 DryGain=-1 StereoWidth=100 WetOnly=False")

def phaser():
	do("Phaser: Stages=2 DryWet=128 Freq=0.4 Phase=0 Depth=100 Feedback=0 Gain=-6")

def wahwah():
	do("Wahwah: Freq=1.5 Phase=0 Depth=70 Resonance=2.5 Offset=30 Gain=-6")

def filterCurve():
	do("FilterCurve")

def graphicEQ():
	do("GraphicEQ")

def reverse():
	do("Reverse")

# Glitch effects scratchpad function - do whatever here
def glitchit():

	fadeOutIn = [
		"FadeOut",
		"FadeIn",
	]

	echoEcho = [
		"Echo: Delay=0 Decay=0.5",
		"Echo: Delay=5 Decay=0.5",
		"Echo: Delay=10 Decay=0.5",
	]

	progressiveReverb = [
		# "Reverb: RoomSize=75 Delay=10 Reverberance=50 HfDamping=50 ToneLow=100 ToneHigh=100 WetGain=-1 DryGain=-1 StereoWidth=100 WetOnly=False",
		"Reverb: RoomSize=70 Delay=10 Reverberance=0 HfDamping=50 ToneLow=100 ToneHigh=100 WetGain=-1 DryGain=-1 StereoWidth=100 WetOnly=False",
		"Reverb: RoomSize=60 Delay=10 Reverberance=10 HfDamping=40 ToneLow=100 ToneHigh=100 WetGain=-1 DryGain=-3 StereoWidth=100 WetOnly=False",
		"Reverb: RoomSize=50 Delay=10 Reverberance=20 HfDamping=30 ToneLow=100 ToneHigh=100 WetGain=-1 DryGain=-5 StereoWidth=100 WetOnly=False",
		"Reverb: RoomSize=40 Delay=10 Reverberance=30 HfDamping=20 ToneLow=100 ToneHigh=100 WetGain=-1 DryGain=-1 StereoWidth=100 WetOnly=False",
		"Reverb: RoomSize=30 Delay=10 Reverberance=40 HfDamping=10 ToneLow=100 ToneHigh=100 WetGain=-1 DryGain=-2 StereoWidth=100 WetOnly=False",
		"Reverb: RoomSize=20 Delay=10 Reverberance=50 HfDamping=00 ToneLow=100 ToneHigh=100 WetGain=-1 DryGain=-1 StereoWidth=100 WetOnly=False",
	]

	effectsStack = ["Reverse"] + echoEcho + progressiveReverb

	saveMultipleFrames(effectsStack)
	# saveMultipleFrames(effectsStack, reversed=True)
