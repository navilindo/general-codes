from google.colab import drive
#drive.mount('/content/gdrive')  original code..
drive.mount('/content/drive')

fileurl = input("enter URL : ")

import requests
file_url = "%s" % fileurl
	
r = requests.get(file_url, stream = True)
#put name (full path) of the file btn brackets
with open("/content/drive/MyDrive/Colab Notebooks/path-to-file/name", "wb") as file:
	for block in r.iter_content(chunk_size = 1024):
		if block:
			file.write(block)
      
# extraction of the zipped files
!unzip "/file-path"

