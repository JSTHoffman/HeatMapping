# -----------------------------------------------------------------
# Automate cloud masking using Fmask windows standalone application
# -----------------------------------------------------------------

# created by: Jaime Hoffman

# adapted from:
# http://stackoverflow.com/questions/450285/executing-command-line-programs-from-within-python
# http://stackoverflow.com/questions/9531683/problems-using-subprocess-call-in-python-2-7-2-on-windows
# http://stackoverflow.com/questions/13744473/command-line-execution-in-different-folder

# --------------------------------

# import subprocess and os modules
import subprocess, os

# command to run Fmask.exe
cmd = r'C:\Fmask\Fmask.exe'

# path to folders containing TIFFs for landsat scene
scenePath = r'C:\Users\Sustainability\Desktop\Summer\LandsatData\FmaskTest'

# loop through items in folder containing all scenes
for aPath in os.listdir(scenePath):

	# set path to current item
	path = "{0}\{1}".format(scenePath, aPath)

	# check if current item is a directory
	if os.path.isdir(path):

		process = subprocess.Popen(
			[cmd],						# command to run
			cwd = path					# directory to run from 
		)

		# wait for process to finish
		process.wait()

		# print success message
		print '\nFmask complete for scene {0}.\n'.format(path)

print '\nEnd of script.'