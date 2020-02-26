# ==========================
#
#	Editor
#
#	These functions handle actions in the audacity editor, such as I/O and selection
#
# ==========================

exec( open("pipe_test.py" ).read() )

import json

def importRaw():
	do("ImportRaw") # Requires manual input

	"""
	# TODO: Try to script the raw file import process by using SoX
	# Convert Raw -> Wav w/ SoX, then import to Audacity

	./sox -e u-law --endian big -c 1 -r 44100 blep2.raw blep.wav

	-e u-law     # Encoding:    U-Law
	--endian big # Byte Order:  Big-endian
	-c 1         # Channels:    1 Channel (mono)
	-r 44100     # Sample Rate: 44100 Hz
	"""
	# input_path = "/Users/glojonat/Documents/audacity-glitcher/tmp/blep.wav"
	# do("Import2: Filename={}".format(input_path)) # Won't work unless file is converted to .wav first

def exportFile():
	# TODO: Script Export with presets:
	# File type: Other uncompressed files
	# Header:    RAW (header-less)
	# Encoding:  U-Law
	do("Export")

def fitWindow():
	do("FitInWindow") # Fit the track to the width of the screen
	do("FitV")        # Fit the track to the height of the screen

def undo():
	do("Undo")

# Select the entire track except for the first few seconds - that's where the image header data is stored.
def selectAll():
	fitWindow()
	trackInfo = getTrackInfo()
	end       = trackInfo.get('end')
	newStart  = float(float(end) * float(0.015)) # Find the timestamp @ 1% of the total track time
	do("SelectTime: Start={} End={}".format(newStart, end))


# Get the attributes of a single track in JSON format
# Parses JSON out of the string response from the command
def getTrackInfo(trackIndex=0):
	response = do("GetInfo: Type=Tracks")
	response = response.replace("BatchCommand finished: OK", "").strip()
	tracks   = json.loads(response)
	return tracks[trackIndex]


def startProject():
	importRaw()
	fitWindow()
	selectAll()
