

import os
import shutil

folder = input("Enter folder path: ")

images_folder = os.path.join(folder, "images")
docs_folder = os.path.join(folder, "docs")

if not os.path.exists(images_folder):
    os.makedirs(images_folder)

if not os.path.exists(docs_folder):
    os.makedirs(docs_folder)

files = os.listdir(folder)

for file in files:
    full_path = os.path.join(folder, file)

    if os.path.isfile(full_path):

        if file.endswith(".jpg"):
          shutil.move(full_path, images_folder)
          print("Moved", file, "to images/")
      
        elif file.endswith(".txt"):
          shutil.move(full_path, docs_folder)
          print("Moved", file, "to docs/")

print("Done organizing!")
