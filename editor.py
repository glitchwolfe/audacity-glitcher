# ==========================
#
#	Editor
#
#	These functions handle actions in the audacity editor, such as I/O and selection
#
# ==========================
import sys
import pipe_test
import json

def do(cmd):
	print("\nEDITOR COMMAND: "+cmd+"\n")
	try:
		response = pipe_test.do_command(cmd)
		print("======================")
		return response
	except:
		print("Oops!", sys.exc_info()[0], "occurred. [", cmd,"]")

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
	# input_path = "/test/directory/blep.wav"
	# do("Import2: Filename={}".format(input_path)) # Won't work unless file is converted to .wav first

def exportFile():
	# TODO: Script Export with presets:
	# File type: Other uncompressed files
	# Header:    RAW (header-less)
	# Encoding:  U-Law
	
	# NOTE: SEEMS TO HAVE TO BE DONE MANUALLY AT THE MOMENT
	# "Export" will default to exporting audio
	# CTRL+SHIFT+E seems to be the only way to open the export dialog
	# do("Export")
	pass

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
	
	# newStart  = float(float(end) * float(0.015)) # Find the timestamp @ 1% of the total track time
	
	# Find the timestamp @ 1% of the total track time
	# ADJUSTING FOR 29MB .TIF FILE MADE IN GIMP
	newStart  = float(float(end) * float(0.017)) 
	

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
