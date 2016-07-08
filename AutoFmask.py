# -----------------------------------------------------------------
# Automate cloud masking using Fmask windows standalone application
# -----------------------------------------------------------------

# created by: Jaime Hoffman

# adapted from:
# http://stackoverflow.com/questions/450285/executing-command-line-programs-from-within-python
# http://stackoverflow.com/questions/9531683/problems-using-subprocess-call-in-python-2-7-2-on-windows
# http://stackoverflow.com/questions/13744473/command-line-execution-in-different-folder

# usage:
# 1) place all TIF files for each landsat scene in separate folders
# 2) set scenePath to directory containing scene folders
# 3) make sure no other folders are present in the directory
# 4) requires the installation of Fmask - set cmd to the Fmask path
# 5) requires the installation of Matlab Compiler Runtime (MCR)

# --------------------------------

# import subprocess and os modules
import subprocess, os

# command to run Fmask.exe
cmd = r'C:\Fmask\Fmask.exe'

# path to folders containing TIFFs for landsat scene
scenePath = r'C:\Users\SUST heavyweight\Desktop\LandsatDaytime_BulkDownload\L8_OLI_TIRS'

# loop through items in folder containing all scenes
for aPath in os.listdir(scenePath):

	# set path to current item
	path = "{0}\{1}".format(scenePath, aPath)

	# check if current item is a directory
	if os.path.isdir(path):

		process = subprocess.Popen(
			[cmd],						# command to run
			cwd=path					# directory to run from
		)

		# wait for process to finish
		process.wait()

		# print success message
		print '\nFmask complete for scene {0}.\n'.format(path)

print '\nEnd of script.'