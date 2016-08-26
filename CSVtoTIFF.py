# --------------------------------------------------------------
# Convert csv file from FLIR thermal camera to tiff image format
# --------------------------------------------------------------

# created by: Jaime Hoffman

# adapted from:
# http://gis.stackexchange.com/questions/62343/how-can-i-convert-a-ascii-file-to-geotiff-using-python
# http://stackoverflow.com/questions/4315506/load-csv-into-2d-matrix-with-numpy-for-plotting

# Usage:
# 1) export images from FLIRTools
# 2) set csvPath to folder with all csv files
# 3) set tifPath to folder for new TIFF files
# 4) set baseName for output
# 5) set image width and height parameters
# 6) set skipRows to 2* or 10**

# *object parameters not included during FLIRTools export
# **object parameters included during FLIRTools export

# ------------------------------------

# import gdal, numpy, and os modules
from osgeo import gdal
import numpy, os
import traceback

# path to files
csvPath = r"C:\Users\SUST heavyweight\Documents\Photoscan\Test\Tree\Thermal\CSV"
tifPath = r"C:\Users\SUST heavyweight\Documents\Photoscan\Test\Tree\Thermal\TIFF"

# image parameters
imgWidth = 320
imgHeight = 240

# loop through files in csvPath
for csv in os.listdir(csvPath):
	try:
		# set input and output files
		inPath = "{0}\{1}".format(csvPath, csv)
		outPath = "{0}\{1}.tif".format(tifPath, csv[:csv.index('.')])

		# csv load parameters (change according to image size and csv format)
		skipRows = 2
		colRange = xrange(1,321)

		# load csv file as numpy array
		dataArray = numpy.loadtxt(
			open(inPath, 'rb'), 		# file to open
			delimiter = ',',			# csv delimiter
			skiprows = skipRows,		# skip header rows
			usecols = colRange			# skip first column
		)

		# get gdal geoTIFF driver
		driver = gdal.GetDriverByName('GTiff')

		# create output dataset
		dst_ds = driver.Create(
			outPath,					# path\filename
			imgWidth,					# image width
			imgHeight,					# image height
			1,							# number of bands
			gdal.GDT_Float32			# data type
		)

		# write numpy array to output dataset as raster band and close
		dst_ds.GetRasterBand(1).WriteArray(dataArray)
		dst_ds = None

	except Exception:
		# give error message
		print traceback.format_exc()
		print "\nThe file {0} could not be converted.".format(inPath)

	else:
		# give success message
		print "\nFile {0} successfully converted.".format(inPath)

print "\nEnd of script."