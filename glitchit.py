import pipe_test

def openRaw():
	print("\nSelect a raw file to start with.\n")

	print("\nNote: The images that tend to work best are large in size, and in .bmp, .tiff, or .raw format.\n")

	print("* ====== Recommended settings: ===== *")
	print("* Encoding:         U-Law            *")
	print("* Byte Order:       Big-Endian       *")
	print("* Channels:         1 Channel (Mono) *")
	print("* Start Offset:     0 bytes          *")
	print("* Amount to import: 100%             *")
	print("* Sample Rate:      44100 Hz         *")
	print("* ================================== *\n")

	# pipe_test.do_command("New")
	pipe_test.do_command("ImportRaw")


def exportRaw():
	# For one track...
	pipe_test.do_command("Export")

	# For Multiple tracks... (Batch operation?)
	pipe_test.do_command("ExportMultiple")


def prepWindow():
	print("\nPreparing workspace...\n")
	pipe_test.do_command("FitInWindow")  # Fit the track to the width of the screen
	pipe_test.do_command("FitV")         # Fit the track to the height of the screen
	pipe_test.do_command("SelectAll")    # Select the entire track
	pipe_test.do_command("SelCntrRight") # Move beginning of selection until the file header is no longer selected (??? Percent of total time)


def startProject():
	openRaw()
	prepWindow()


# ===== Start Script =====

startProject()
