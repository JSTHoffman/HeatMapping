# ------------------------------------------------
# Rename Landsat images using YYYYMMDD date format
# ------------------------------------------------

# created by: Jaime Hoffman

# adapted from:
# http://stackoverflow.com/questions/30307164/convert-yyyymmdd-filename-to-yyyyjd

# usage:
# 1) set filePath to directory containing landsat TIF files
# 2) set sceneID to match the beginning of the original file names*
# 3) set dateFormat to the format of your choice
# 4) set baseName to the output file name of your choice, placing a zero
#    inside curly braces ({0}) where you would like the date to be.
#    Make sure to include the .TIF file extension

# *this will be the platform identifier followed by the WRS path and row.
# The identifiers for landsat 5, 7, and 8 are LT5, LE7, and LC8

# ------------------------------------

# import datetime, glob and os modules
from datetime import datetime
from glob import glob
import os

# location of TIFF files to be renamed 
filePath = r'C:\Users\Sustainability\Desktop\Summer\LandsatData\NightTimeBulkDownload\test'
sceneID = 'LC8139208'
dateFormat = '%Y%m%d'
baseName = 'L8_Night_{0}_B10.TIF'

# loop through files with L8 standard name
for fileName in glob(os.path.join(filePath, '{0}*.TIF'.format(sceneID))):

	# get date as YYYYJD from file name and create new file name with YYYYMMDD
	date = datetime.strptime(os.path.basename(fileName), '{0}%Y%jLGN00_B10.TIF'.format(sceneID))
	newName = os.path.join(filePath, baseName.format(date.strftime(dateFormat)))

	# rename the file
	os.rename(fileName, newName)

print "\nEnd of script."
