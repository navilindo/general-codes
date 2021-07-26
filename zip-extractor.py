# gen#01
# code snippet to extract files using python

import zipfile
#
zippedFile = 'path_to_file/file.zip'
with zipfile.ZipFile(zippedFile,"r") as zip_ext:
   zip_ext.extractall('destination')
