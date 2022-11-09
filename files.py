import os
import hashlib
import string
import shutil 
import random
import sys

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# search folder and copy any json + png that match into a new temp folder
def filter_json(target_dir):
    
    unique = []
    tempdir = id_generator()
    os.mkdir(tempdir)
    print(target_dir)
    for filename in os.listdir(target_dir):
        if (filename.endswith(".png")):
            print(filename)
            filename_list = filename.split(".")
            json_filename = filename_list[0] + ".attributes.json"
            json_filename_path = target_dir + filename_list[0] + ".attributes.json"
            print(json_filename)
            if (os.path.exists(json_filename_path)):
                shutil.copy(json_filename_path, tempdir)
                shutil.copy(target_dir + filename,  tempdir)
        
def rename_files(target_dir):
    unique = []
    temp_dir = id_generator()
    os.mkdir(temp_dir)
    index = 1
    
    for filename in sorted(os.listdir(target_dir)):
        filename_split = filename.split(".")
        if (filename.endswith(".png")):
            print(filename)
            new_image = "./" + temp_dir + "/" + str(index) + ".png"
            new_metadata = "./" + temp_dir + "/" + str(index) + ".attributes.json"
            shutil.copyfile(target_dir + filename, new_image)
            shutil.copyfile(target_dir + filename_split[0] + ".attributes.json", new_metadata)
            index += 1            



target_dir = "./" + sys.argv[2] + "/"

match sys.argv[1]:
    case "filter":
        filter_json(target_dir)    
    case "rename":
        rename_files(target_dir)     
    case _:
        print("need argument 1 (filter / rename)")


