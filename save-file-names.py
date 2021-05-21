import os
import json

filenames = []

with open("output.json", "w") as a:
    for path, subdirs, files in os.walk(r'C:\Users\tengs\PycharmProjects\vuejs-pdfjs-viewer\public\lib\web\textbook'):
       for filename in files:
           filenames.append(filename)
    json.dump(filenames, a)  #TODO there is a bug, it has a bracket at the end