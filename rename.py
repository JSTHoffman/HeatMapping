import os

filePath = r'C:\Users\SUST heavyweight\Documents\Photoscan\Test\Tree\Thermal\RGB\\'

# loop through files with L8 standard name
for file in os.listdir(filePath):
	print file
	os.rename('{0}{1}'.format(filePath, file), '{0}{1}.jpg'.format(filePath, file).replace('- photo', ''))

print "\nEnd of script."
