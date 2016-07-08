# ----------------------------------------------------------------
# Revert to original Landsat Naming convention with YYYYDDD format
# ----------------------------------------------------------------

# created by: Jaime Hoffman

# adapted from:
# http://stackoverflow.com/questions/30307164/convert-yyyymmdd-filename-to-yyyyjd

# usage:
# 1) set filePath to directory containing landsat TIF files
# 2) set sceneID to match the beginning of the original Landsat file names*
# 3) set dateFormat to the format of your choice
# 4) set currentName to match the beginning of the current file names

# *this will be the platform identifier followed by the WRS path and row.
# The identifiers for landsat 5, 7, and 8 are LT5, LE7, and LC8

# ------------------------------------

# import datetime, glob and os modules
from datetime import datetime
from glob import glob
import os

# location of TIFF files to be renamed 
filePath = r'C:\Users\Sustainability\Desktop\Summer\LandsatData\NightTimeBulkDownload\B10_TIFFs'
sceneID = 'LC8139208'
currentName = 'L8_Night'
dateFormat = '%Y%j'
baseName = 'LC8139208{0}LGN00_B10.TIF'

# loop through files with L8 standard name
for fileName in glob(os.path.join(filePath, '{0}*.TIF'.format(currentName))):

	# get date as YYYYMMDD from file name and create new file name with YYYYJD
	date = datetime.strptime(os.path.basename(fileName), '{0}_%Y%m%d_B10.TIF'.format(currentName))
	newName = os.path.join(filePath, baseName.format(date.strftime(dateFormat)))

	# rename the file
	os.rename(fileName, newName)

print "\nEnd of script."
