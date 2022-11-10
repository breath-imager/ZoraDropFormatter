import os
import hashlib
import string
import shutil 
import random
import sys
import json
import csv
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# search folder and copy any json + png that match into a new temp folder
def filter_json(target_dir):
    
    temp_dir = id_generator()
    os.mkdir(temp_dir)
    for filename in os.listdir(target_dir):
        if (filename.endswith(".png")):
            print(filename)
            filename_list = filename.split(".")
            json_filename = filename_list[0] + ".attributes.json"
            json_filename_path = target_dir + filename_list[0] + ".attributes.json"
            print(json_filename)
            if (os.path.exists(json_filename_path)):
                shutil.copy(json_filename_path, temp_dir)
                shutil.copy(target_dir + filename,  temp_dir)
         
# construct master csv using all individual jsons in target folder
def make_csv(target_dir):

    data_file = open('data_file.csv', 'w')
    csv_writer = csv.writer(data_file)

    temp_dir = id_generator()
    #os.mkdir(temp_dir)
    json_path = "json/"
    # index for keeping track of file count
    index = 1
    csv_writer.writerow(["name","description","attributes[Effects]","attributes[Textures]","attributes[Slider 1]","attributes[Slider 2]"])
    for filename in os.listdir(json_path):
        filename = str(index) + ".attributes.json"
        # Opening JSON file and loading the data
        # into the variable data
        with open(json_path + filename) as json_file:
            data = json.load(json_file)

        attribute_data = data
        print(attribute_data)
        name = "Refract Pass #" + str(index)
        description = "The REFRACT Pass will act as the main point of access to RefractionDAO. It is an evolving NFT that will offer long-term, expanded utilities for our members.The Pass was created by Refraction using our generative art app, Generate. 1000 editions will be available, each with a unique gradient design."
        csv_writer.writerow([name, description, attribute_data[0]['value'],attribute_data[1]['value'],attribute_data[2]['value'],attribute_data[3]['value']])
        index += 1

 

# rename all files in target folder in contiguous, sequential order
def rename_files(target_dir):
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



if len(sys.argv) < 2:
    print("Need target directory!")
else:
    target_dir = "./" + sys.argv[2] + "/"

match sys.argv[1]:
    case "filter":
        filter_json(target_dir)    
    case "rename":
        rename_files(target_dir)   
    case "makecsv":
        make_csv(target_dir)  
    case _:
        print("need argument 1 (filter / rename)")


